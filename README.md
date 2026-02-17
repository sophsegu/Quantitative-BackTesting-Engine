# Quantitative Backtesting Engine

[![Python Version](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Overview

The **Quantitative Backtesting Engine** is a Python framework designed for financial researchers, algorithmic traders, and quantitative analysts to:

- Download historical market data.
- Generate trading signals using custom strategies.
- Backtest single or multi-asset portfolios.
- Evaluate portfolio performance with standard financial metrics.

The engine supports **multi-ticker portfolios** with **custom weighting** and modular components for signals, portfolios, and metrics.  

---

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

---

## Project Structure
Quantitative-BackTesting-Engine/
├── data/
│ └── yahoo_loader.py # Yahoo Finance data loader
├── signals/
│ └── momentum.py # Example momentum signal generator
├── portfolio/
│ └── portfolio.py # Portfolio engine and backtesting
├── metrics/
│ └── metrics.py # Performance metrics
├── main.py # Example usage script
├── requirements.txt # Python dependencies
└── README.md # Project overview


---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Quantitative-BackTesting-Engine.git
cd Quantitative-BackTesting-Engine

2. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


