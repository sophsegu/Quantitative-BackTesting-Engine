import pandas as pd

class BaseSignal:
    def __init__(self, name="BaseSignal"):
        self.name = name

    def generate_signal(self, df: pd.DataFrame):
        """
        Input: df must contain 'Date' and 'Adj Close' columns
        Output: pandas DataFrame with 'Signal' column: 1=Buy, -1=Sell, 0=Hold
        """
        raise NotImplementedError("Must implement generate_signal")
