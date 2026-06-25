"""
dashboard/utils.py
====================
Reusable helper functions for the Smart Retail Sales Analysis dashboard.

Keeping chart-building and formatting logic here (separate from app.py)
makes the main dashboard file easier to read and makes these utilities
testable / reusable in notebooks as well.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def format_currency(value: float) -> str:
    """Format a number as a compact USD currency string, e.g. $1,234,567."""
    return f"${value:,.0f}"


def format_percent(value: float, decimals: int = 1) -> str:
    """Format a number as a percentage string, e.g. 12.3%."""
    return f"{value:.{decimals}f}%"


def make_trend_chart(series, color: str, ylabel: str, figsize=(10, 4.5)):
    """
    Build a filled line chart for a time-indexed Pandas Series
    (e.g. monthly Sales or Profit totals).
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(series.index.astype(str), series.values, marker="o", color=color, linewidth=2)
    ax.fill_between(range(len(series)), series.values, color=color, alpha=0.1)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=70, fontsize=8)
    plt.tight_layout()
    return fig


def make_bar_chart(categories, values, palette: str, xlabel: str, horizontal=True, figsize=(8, 5)):
    """Build a sorted bar chart (horizontal by default) for category-style comparisons."""
    fig, ax = plt.subplots(figsize=figsize)
    if horizontal:
        sns.barplot(x=values, y=categories, palette=palette, ax=ax)
        ax.set_xlabel(xlabel)
    else:
        sns.barplot(x=categories, y=values, palette=palette, ax=ax)
        ax.set_ylabel(xlabel)
    plt.tight_layout()
    return fig


def kpi_summary(df) -> dict:
    """Compute the standard KPI set used on the dashboard header cards."""
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    avg_order_value = df["Sales"].mean() if len(df) else 0
    profit_margin = (total_profit / total_sales * 100) if total_sales else 0
    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "avg_order_value": avg_order_value,
        "profit_margin": profit_margin,
    }
