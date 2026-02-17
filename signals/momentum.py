import pandas as pd
from .base_signal import BaseSignal

class MomentumSignal(BaseSignal):
    """
    Simple momentum strategy:
    - Buy when price is above N-day moving average
    - Sell when price is below N-day moving average
    """

    def __init__(self, lookback=20):
        super().__init__(name=f"Momentum_{lookback}d")
        self.lookback = lookback

    def generate_signal(self, df: pd.DataFrame):
        df = df.copy()

        # Ensure 'Adj Close' exists
        if "Adj Close" not in df.columns:
            raise ValueError("DataFrame must contain 'Adj Close' column")

        # Compute moving average
        df["MA"] = df["Adj Close"].rolling(window=self.lookback).mean()

        # Generate signals
        df["Signal"] = 0
        df.loc[df["Adj Close"] > df["MA"], "Signal"] = 1    # Buy
        df.loc[df["Adj Close"] < df["MA"], "Signal"] = -1   # Sell

        # Optional: drop rows with NaN MA
        df = df.dropna(subset=["MA"])

        return df[["Date", "Adj Close", "MA", "Signal"]]
