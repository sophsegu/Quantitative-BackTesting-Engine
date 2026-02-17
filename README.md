# Quantitative Backtesting Engine

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/github/workflow/status/yourusername/Quantitative-Backtesting-Engine/Python%20package)

overview: |
  ## Overview
  The Quantitative Backtesting Engine is a Python framework designed for financial researchers, algorithmic traders, and quantitative analysts to:

  - Download historical market data.
  - Generate trading signals using custom strategies.
  - Backtest single or multi-asset portfolios.
  - Evaluate portfolio performance with standard financial metrics.

  The engine supports multi-ticker portfolios with **custom weighting** and modular components for signals, portfolios, and metrics.

features: |
  ## Features
  - Download historical stock and ETF data from Yahoo Finance.
  - Momentum-based signal generation (with configurable lookback).
  - Backtesting engine with positions, daily returns, and cumulative returns.
  - Weighted multi-ticker portfolios.
  - Portfolio performance metrics:
      - Cumulative Return
      - Annualized Return
      - Volatility
      - Sharpe Ratio
      - Maximum Drawdown
  - Extensible to custom signals and new metrics.
  - Output in Pandas DataFrames for easy visualization and analysis.

project_structure: |
  ## Project Structure
  Quantitative-BackTesting-Engine/
  ├── data/
  │   └── yahoo_loader.py        # Yahoo Finance data loader
  ├── signals/
  │   └── momentum.py            # Example momentum signal generator
  ├── portfolio/
  │   └── portfolio.py           # Portfolio engine and backtesting
  ├── metrics/
  │   └── metrics.py             # Performance metrics
  ├── main.py                    # Example usage script
  ├── requirements.txt           # Python dependencies
  └── README.md                  # Project overview

installation: |
  ## Installation
  1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/Quantitative-BackTesting-Engine.git
  cd Quantitative-BackTesting-Engine
  ```
  2. Create a virtual environment and install dependencies:
  ```bash
  python -m venv venv
  # Linux/macOS:
  source venv/bin/activate
  # Windows:
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

usage: |
   ## Usage
   ```bash
    from data.yahoo_loader import YahooFinanceLoader
    from signals.momentum import MomentumSignal
    from portfolio.portfolio import Portfolio
    from metrics.metrics import calculate_metrics

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
    print(f"\\n{ticker} Backtest:")
    print(df.tail(10))

    # 5. Build custom weighted portfolio
    weights = {
        "AAPL": 0.25,
        "MSFT": 0.25,
        "SPY": 0.50
    }
    portfolio_df = portfolio.build_weighted_portfolio(backtest_results, weights)

    # 6. Calculate metrics
    metrics = calculate_metrics(portfolio_df)
    print(metrics)
  ```

license: |
  ## License
  This project is licensed under the MIT License.

notes: |
  ## Notes
  - The engine is fully modular: you can add new signal generators, portfolios, or metrics easily.
  - All outputs are Pandas DataFrames for easy plotting, visualization, and further analysis.
  - Designed for Python 3.10+.
  - Supports multi-ticker portfolios with customizable weights.
  - Commission is applied in backtesting at 0.1% per trade (modifiable in the Portfolio class).
