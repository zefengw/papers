"""Toy KindHML-style model checking for smart contract transition systems."""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Dict, List, Set, Tuple, Union


Ast = Union[
    Tuple[str],
    Tuple[str, str],
    Tuple[str, object],
    Tuple[str, object, object],
    Tuple[str, str, object],
]


@dataclass
class LTS:
    """Finite labeled transition system with state propositions."""

    transitions: Dict[str, List[Tuple[str, str]]]
    propositions: Dict[str, Set[str]]


TOKEN_PATTERN = re.compile(r"\s*(tt|ff|[A-Za-z_][A-Za-z0-9_]*|[()!&|<>\[\]])")


class Parser:
    """Recursive-descent parser for a compact HML syntax.

    Grammar (informal):
      expr   := or_expr
      or_expr:= and_expr ('|' and_expr)*
      and_expr:= unary ('&' unary)*
      unary  := '!' unary
              | '<' IDENT '>' unary
              | '[' IDENT ']' unary
              | IDENT | 'tt' | 'ff' | '(' expr ')'
    """

    def __init__(self, text: str):
        self.tokens = [m.group(1) for m in TOKEN_PATTERN.finditer(text)]
        self.i = 0

    def peek(self) -> str | None:
        return self.tokens[self.i] if self.i < len(self.tokens) else None

    def eat(self, expected: str | None = None) -> str:
        tok = self.peek()
        if tok is None:
            raise ValueError("unexpected end of formula")
        if expected is not None and tok != expected:
            raise ValueError(f"expected '{expected}', got '{tok}'")
        self.i += 1
        return tok

    def parse(self) -> Ast:
        node = self.parse_or()
        if self.peek() is not None:
            raise ValueError(f"unexpected token '{self.peek()}'")
        return node

    def parse_or(self) -> Ast:
        node = self.parse_and()
        while self.peek() == "|":
            self.eat("|")
            rhs = self.parse_and()
            node = ("or", node, rhs)
        return node

    def parse_and(self) -> Ast:
        node = self.parse_unary()
        while self.peek() == "&":
            self.eat("&")
            rhs = self.parse_unary()
            node = ("and", node, rhs)
        return node

    def parse_unary(self) -> Ast:
        tok = self.peek()
        if tok == "!":
            self.eat("!")
            return ("not", self.parse_unary())
        if tok == "<":
            self.eat("<")
            action = self.eat()
            self.eat(">")
            return ("diamond", action, self.parse_unary())
        if tok == "[":
            self.eat("[")
            action = self.eat()
            self.eat("]")
            return ("box", action, self.parse_unary())
        if tok == "(":
            self.eat("(")
            node = self.parse_or()
            self.eat(")")
            return node
        if tok in {"tt", "ff"}:
            self.eat(tok)
            return (tok,)
        # Atomic proposition.
        atom = self.eat()
        return ("atom", atom)


def parse_formula(text: str) -> Ast:
    return Parser(text).parse()


def successors(lts: LTS, state: str, action: str) -> List[str]:
    return [dst for act, dst in lts.transitions.get(state, []) if act == action]


def satisfies(lts: LTS, state: str, formula: Ast) -> bool:
    """Evaluate whether state satisfies formula under HML semantics."""
    kind = formula[0]

    if kind == "tt":
        return True
    if kind == "ff":
        return False
    if kind == "atom":
        return formula[1] in lts.propositions.get(state, set())
    if kind == "not":
        return not satisfies(lts, state, formula[1])
    if kind == "and":
        return satisfies(lts, state, formula[1]) and satisfies(lts, state, formula[2])
    if kind == "or":
        return satisfies(lts, state, formula[1]) or satisfies(lts, state, formula[2])
    if kind == "diamond":
        action = formula[1]
        return any(satisfies(lts, s2, formula[2]) for s2 in successors(lts, state, action))
    if kind == "box":
        action = formula[1]
        succs = successors(lts, state, action)
        # Standard box semantics: vacuously true when no outgoing action-matching edge.
        return all(satisfies(lts, s2, formula[2]) for s2 in succs)

    raise ValueError(f"unknown AST node: {kind}")


def build_secure_escrow() -> LTS:
    transitions = {
        "init": [("deposit", "funded")],
        "funded": [("release", "released"), ("timeout", "timed_out")],
        "released": [("withdraw", "withdrawn")],
        "timed_out": [("refund", "refunded")],
        "withdrawn": [],
        "refunded": [],
    }
    props = {
        "init": {"start"},
        "funded": {"funded"},
        "released": {"funded", "released", "withdrawable"},
        "timed_out": {"funded", "refundable"},
        "withdrawn": {"terminal"},
        "refunded": {"terminal"},
    }
    return LTS(transitions=transitions, propositions=props)


def build_buggy_escrow() -> LTS:
    """Bug: allows direct withdrawal immediately after deposit."""
    secure = build_secure_escrow()
    bug_transitions = dict(secure.transitions)
    bug_transitions["funded"] = list(bug_transitions["funded"]) + [("withdraw", "withdrawn")]
    return LTS(transitions=bug_transitions, propositions=secure.propositions)


def evaluate_contract(lts: LTS) -> Dict[str, bool]:
    formulas = {
        # There exists a valid happy path to terminal settlement.
        "happy_path_exists": "<deposit><release><withdraw>terminal",
        # Refund path is available after timeout.
        "timeout_refund_exists": "<deposit><timeout><refund>terminal",
        # Safety: no direct withdrawal should be possible immediately after deposit.
        "no_direct_withdraw_after_deposit": "[deposit][withdraw]ff",
        # After release, every withdraw transition must end in terminal state.
        "withdraw_after_release_is_terminal": "[deposit][release][withdraw]terminal",
    }

    out: Dict[str, bool] = {}
    for name, text in formulas.items():
        ast = parse_formula(text)
        out[name] = satisfies(lts, "init", ast)
    return out


def run_demo() -> Dict[str, object]:
    secure = evaluate_contract(build_secure_escrow())
    buggy = evaluate_contract(build_buggy_escrow())

    return {
        "logic": "HML-subset",
        "secure_contract": secure,
        "buggy_contract": buggy,
        "key_observation": "The buggy model violates no_direct_withdraw_after_deposit, demonstrating a safety failure surfaced by logical model checking.",
    }
