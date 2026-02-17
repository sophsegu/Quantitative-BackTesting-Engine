from data.yahoo_loader import YahooFinanceLoader
from signals.momentum import MomentumSignal
from portfolio.portfolio import Portfolio

# 1. Load data
loader = YahooFinanceLoader()
tickers = ["AAPL", "MSFT", "SPY"]
data = {t: loader.load_ticker(t) for t in tickers}

# 2. Generate signals
momentum = MomentumSignal(lookback=50)
signals = {t: momentum.generate_signal(df) for t, df in data.items()}

# 3. Backtest
portfolio = Portfolio(initial_capital=100000)
backtest_results = portfolio.backtest_multiple(signals)

# 4. Inspect
for ticker, df in backtest_results.items():
    print(f"\n{ticker} Backtest:")
    print(df.tail(10))
