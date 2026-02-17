import pandas as pd
import numpy as np

class Portfolio:
    """
    Portfolio engine for backtesting signals.
    - Converts signals to positions
    - Computes daily returns and cumulative P&L
    """

    def __init__(self, initial_capital=100000):
        self.initial_capital = initial_capital

    def generate_positions(self, signal_df):
        """
        Convert signal to positions:
        1 = long
        -1 = short
        0 = flat
        """
        df = signal_df.copy()
        df["Position"] = df["Signal"].shift(1).fillna(0)  # Hold previous day position
        return df

    def calculate_returns(self, df):
        """
        Calculate daily returns and cumulative portfolio value
        """
        df = df.copy()
        commission = 0.001  # 0.1% per trade
        df["Daily_Return"] = df["Position"].diff().abs() * (-commission) + df["Position"] * df["Adj Close"].pct_change()
        df["Cumulative_Return"] = (1 + df["Daily_Return"]).cumprod() * self.initial_capital
        return df

    def backtest_signal(self, signal_df):
        """
        Full backtest pipeline for one ticker
        """
        positions = self.generate_positions(signal_df)
        returns = self.calculate_returns(positions)
        return returns

    def backtest_multiple(self, signals_dict):
        """
        Backtest multiple tickers independently
        signals_dict: {ticker: signal_df}
        returns_dict: {ticker: backtest_df}
        """
        returns_dict = {}
        for ticker, df in signals_dict.items():
            returns_dict[ticker] = self.backtest_signal(df)
        return returns_dict
