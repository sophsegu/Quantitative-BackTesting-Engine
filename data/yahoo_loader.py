import yfinance as yf
import pandas as pd
import os


class YahooFinanceLoader:

    def __init__(self, data_dir="data/raw"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)


    def _get_file_path(self, ticker):
        return os.path.join(self.data_dir, f"{ticker}.parquet")


    def download_ticker(self, ticker):

        try:

            print(f"Downloading {ticker}...")

            df = yf.download(
                ticker,
                period="5y",
                auto_adjust=False,
                progress=False
            )

            if df.empty:
                print(f"No data found for {ticker}")
                return None
            
            
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            df.reset_index(inplace=True)

            df = df.drop_duplicates(subset="Date")
            df = df.sort_values("Date")

            file_path = self._get_file_path(ticker)

            df.to_parquet(
                file_path,
                engine="pyarrow",
                compression="snappy",
                index=False
            )

            print(f"Saved {ticker}")

            return df

        except Exception as e:
            print(f"Error downloading {ticker}: {e}")
            return None


    def load_ticker(self, ticker):

        file_path = self._get_file_path(ticker)

        # Caching logic
        if os.path.exists(file_path):

            df = pd.read_parquet(file_path)
            return df

        else:

            print(f"{ticker} not found locally. Downloading...")
            return self.download_ticker(ticker)


    def download_multiple(self, tickers):

        results = {}

        for ticker in tickers:

            df = self.download_ticker(ticker)

            if df is not None:
                results[ticker] = df

        return results


    def load_multiple(self, tickers):

        results = {}

        for ticker in tickers:

            df = self.load_ticker(ticker)

            if df is not None:
                results[ticker] = df

        return results
