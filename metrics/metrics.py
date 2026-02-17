import numpy as np

def calculate_metrics(portfolio_df):

    daily_returns = portfolio_df["Portfolio_Return"]

    cumulative_return = portfolio_df["Cumulative_Return"].iloc[-1] - 1

    annualized_return = (1 + cumulative_return) ** (252 / len(daily_returns)) - 1

    volatility = daily_returns.std() * np.sqrt(252)

    sharpe = annualized_return / volatility

    rolling_max = portfolio_df["Portfolio_Value"].cummax()
    drawdown = portfolio_df["Portfolio_Value"] / rolling_max - 1
    max_drawdown = drawdown.min()

    return {
        "Cumulative Return": cumulative_return,
        "Annual Return": annualized_return,
        "Volatility": volatility,
        "Sharpe": sharpe,
        "Max Drawdown": max_drawdown
    }
