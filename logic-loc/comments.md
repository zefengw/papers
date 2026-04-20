# Critical Notes & Extensions

## Limitations
- Dependency on Fact Extraction: The quality of localization depends on the accuracy of the initial codebase-to-Datalog conversion (e.g., parsing call graphs).
- Datalog Complexity: Complex structural queries might lead to expensive joins in the Datalog engine for extremely large repos.

## Extension Ideas
- **Temporal Analysis**: Extend the Datalog facts to include git history (e.g., "Function A was modified in the same commit as Function B").
- **Hybrid Search**: Combine structural Datalog queries with semantic vector search for a "coarse-to-fine" localization pipeline.
