from data.yahoo_loader import YahooFinanceLoader
from signals.momentum import MomentumSignal

# Load data
loader = YahooFinanceLoader()
df_aapl = loader.load_ticker("AAPL")

# Create momentum signal
momentum = MomentumSignal(lookback=50)
signal_df = momentum.generate_signal(df_aapl)

print(signal_df.tail(10))
