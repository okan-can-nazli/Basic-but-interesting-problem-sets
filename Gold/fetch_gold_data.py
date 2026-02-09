"""
Synthetic Gold Price Generator (Geometric Brownian Motion)
==========================================================
Generates realistic FAKE gold price data from 1972 to Present.
Used for testing LSTM logic without internet/API dependency.

Mathematical Model:
   dS_t = μ*S_t*dt + σ*S_t*dW_t
   (Drift + Volatility + Random Walk)
"""

import numpy as np
import pandas as pd
import json
from datetime import datetime, timedelta

def generate_synthetic_data():
    print("=" * 60)
    print("GENERATING SYNTHETIC GOLD DATA (1972 - Present)")
    print("=" * 60)
    print("Model: Geometric Brownian Motion (GBM)")
    print("Goal: Mimic post-1971 volatility and inflation trend")
    print()

    # --- CONFIGURATION ---
    start_date = '1972-01-04'
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_price = 35.00  # Price of gold in 1971 ($35/oz)
    
    # Parameters to mimic gold's behavior
    mu = 0.08     # Annual drift (approx 8% return/year average)
    sigma = 0.18  # Annual volatility (18% standard deviation)
    dt = 1/252    # Daily time step (252 trading days/year)

    # --- GENERATION ---
    # Create business day range
    dates = pd.bdate_range(start=start_date, end=end_date)
    n_days = len(dates)
    
    print(f"Generating {n_days} days of market data...")
    
    # Generate random shocks (Wiener process)
    # np.random.normal(0, 1) generates standard normal distribution
    random_shocks = np.random.normal(0, 1, n_days)
    
    # Calculate price path using GBM formula
    # S_t = S_{t-1} * exp((mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z_t)
    drift_term = (mu - 0.5 * sigma**2) * dt
    shock_term = sigma * np.sqrt(dt) * random_shocks
    
    # Calculate daily returns (log returns)
    log_returns = drift_term + shock_term
    
    # Cumulative sum to get price trajectory
    cumulative_returns = np.cumsum(log_returns)
    
    # Calculate prices
    prices = start_price * np.exp(cumulative_returns)
    
    # Add some "market noise" / irrationality (Sine wave for cycles)
    # This simulates boom/bust cycles (like 1980 or 2011)
    t = np.linspace(0, 4*np.pi, n_days)
    cycle_multiplier = 1 + 0.2 * np.sin(t) # +/- 20% cyclical swing
    prices = prices * cycle_multiplier

    # --- SAVING ---
    # Convert to lists for JSON
    date_strings = dates.strftime('%Y-%m-%d').tolist()
    price_list = prices.tolist()
    
    # Round to 2 decimal places
    price_list = [round(p, 4) for p in price_list]

    print()
    print("=" * 60)
    print("✅ GENERATION SUCCESSFUL!")
    print("=" * 60)
    print(f"Data Summary:")
    print(f"  Start Date: {date_strings[0]} ($ {price_list[0]})")
    print(f"  End Date:   {date_strings[-1]} ($ {price_list[-1]})")
    print(f"  Total Data: {len(price_list)} points")
    print(f"  Max Price:  ${max(price_list)}")
    print()

    # Save to JSON matching your LSTM format
    data = {
        'dates': date_strings,
        'prices': price_list,
        'ticker': 'SYNTHETIC_GOLD_GBM',
        'description': 'Synthetic Data generated via Geometric Brownian Motion',
        'source': 'Local Python Script (GBM Model)',
        'fetched_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    filename = 'gold_prices.json'
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"✅ Saved to '{filename}'")
    print("🚀 You can now run your LSTM script immediately.")
    print("   (The model should learn this pattern easily!)")

if __name__ == "__main__":
    generate_synthetic_data()