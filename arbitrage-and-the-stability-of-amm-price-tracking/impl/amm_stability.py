import numpy as np

class AMMTracker:
    def __init__(self, init_price=1.0, drift_vol=0.05, arb_threshold=0.02, block_correction_rate=0.8):
        self.ref_price = init_price
        self.amm_price = init_price
        
        self.drift_vol = drift_vol # Random walk volatility of reference price
        self.arb_threshold = arb_threshold # Transaction fee / cost barrier
        self.block_correction_rate = block_correction_rate # How much of gap is corrected per block

    def simulate_blocks(self, blocks=100):
        ref_prices = []
        amm_prices = []
        
        for _ in range(blocks):
            # 1. External market drift (Reference Price changes)
            drift = np.random.normal(0, self.drift_vol)
            self.ref_price *= (1 + drift)
            
            # 2. Calculate Tracking Error (Gap)
            gap = (self.ref_price - self.amm_price) / self.amm_price
            
            # 3. Arbitrage Correction Phase (Within the block)
            if abs(gap) > self.arb_threshold:
                # Arbitrage is profitable. Arbitrageurs trade against AMM, pushing AMM price towards Ref.
                # The correction isn't perfect immediately due to block limits, fees, and liquidity depth.
                correction = gap * self.block_correction_rate
                self.amm_price *= (1 + correction)
            
            # Log state
            ref_prices.append(self.ref_price)
            amm_prices.append(self.amm_price)
            
        return ref_prices, amm_prices

if __name__ == "__main__":
    amm = AMMTracker()
    refs, amms = amm.simulate_blocks(blocks=50)
    
    print(f"{'Block':<6} | {'Ref Price':<12} | {'AMM Price':<12} | {'Gap %'}")
    print("-" * 50)
    for i in range(len(refs)):
        gap_pct = ((refs[i] - amms[i]) / amms[i]) * 100
        if i < 5 or i > 45: # Just print start/end to avoid spam
            print(f"{i:<6} | {refs[i]:<12.4f} | {amms[i]:<12.4f} | {gap_pct:+.2f}%")
        elif i == 5:
            print("...")
            
    print("\nSimulation complete. The AMM price tracks the reference price with bounded error due to arbitrage.")