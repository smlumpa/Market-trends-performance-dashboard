"""Prepare and analyse historical stock-index and commodity price data.

Expected input files use the Investing.com CSV layout, including Date and Price
columns. Full source datasets are intentionally kept outside the repository.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

TRADING_DAYS = 260


def parse_price(value: object) -> float:
    """Convert a formatted market price to a float."""
    if pd.isna(value):
        return np.nan
    text = str(value).strip().replace(",", "")
    if not text or text in {"-", "nan"}:
        return np.nan

    multiplier = 1.0
    suffix = text[-1].upper()
    if suffix in {"K", "M", "B"}:
        multiplier = {"K": 1_000.0, "M": 1_000_000.0, "B": 1_000_000_000.0}[suffix]
        text = text[:-1]
    return float(text) * multiplier


def series_name(path: Path) -> str:
    """Create a stable column name from an input filename."""
    name = re.sub(r"\s+Historical Data.*$", "", path.stem, flags=re.IGNORECASE)
    name = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return name


def read_price_file(path: Path) -> pd.DataFrame:
    """Read one market CSV and return date plus a named price series."""
    # Source exports may be comma- or tab-delimited despite sharing a .csv
    # extension. Reading with utf-8-sig also removes a possible byte-order mark.
    first_line = path.open("r", encoding="utf-8-sig", errors="replace").readline()
    delimiter = "\t" if "\t" in first_line else ","
    frame = pd.read_csv(path, sep=delimiter, encoding="utf-8-sig")
    required = {"Date", "Price"}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"{path.name} is missing columns: {sorted(missing)}")

    column = series_name(path)
    output = frame.loc[:, ["Date", "Price"]].copy()
    output["Date"] = pd.to_datetime(output["Date"], errors="coerce", dayfirst=False)
    output[column] = output["Price"].map(parse_price)
    output = output.drop(columns="Price").dropna(subset=["Date", column])
    output = output.drop_duplicates(subset="Date", keep="last")
    return output.sort_values("Date")


def combine_directory(directory: Path) -> pd.DataFrame:
    """Outer-join every CSV in a directory on Date."""
    paths = sorted(directory.glob("*.csv"))
    if not paths:
        raise FileNotFoundError(f"No CSV files found in {directory}")

    combined: pd.DataFrame | None = None
    for path in paths:
        current = read_price_file(path)
        combined = current if combined is None else combined.merge(current, on="Date", how="outer")

    assert combined is not None
    return combined.sort_values("Date").reset_index(drop=True)


def prepare_prices(stock_dir: Path, commodity_dir: Path) -> pd.DataFrame:
    """Combine stock and commodity prices and align non-matching calendars."""
    stocks = combine_directory(stock_dir)
    commodities = combine_directory(commodity_dir)
    prices = stocks.merge(commodities, on="Date", how="outer").sort_values("Date")

    # Carry the most recently observed price across non-trading days. A backward
    # fill is deliberately avoided because it would introduce future information.
    value_columns = prices.columns.difference(["Date"])
    prices[value_columns] = prices[value_columns].ffill()
    prices = prices.dropna().drop_duplicates(subset="Date", keep="last")
    return prices.reset_index(drop=True)


def calculate_outputs(prices: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Calculate returns, summary measures and a correlation matrix."""
    values = prices.set_index("Date")
    returns = values.pct_change(fill_method=None).dropna(how="all")

    summary = pd.DataFrame(
        {
            "annualised_return": returns.mean() * TRADING_DAYS,
            "annualised_volatility": returns.std() * np.sqrt(TRADING_DAYS),
            "observations": returns.count(),
        }
    ).sort_values("annualised_return", ascending=False)

    return returns, summary, returns.corr()


def save_charts(summary: pd.DataFrame, correlation: pd.DataFrame, output_dir: Path) -> None:
    """Save concise portfolio charts."""
    sns.set_theme(style="whitegrid")

    ranked = summary.head(15).sort_values("annualised_return")
    fig, axis = plt.subplots(figsize=(10, 7))
    axis.barh(ranked.index, ranked["annualised_return"] * 100, color="#2563EB")
    axis.set(title="Top annualised returns", xlabel="Annualised return (%)", ylabel="")
    fig.tight_layout()
    fig.savefig(output_dir / "top_annualised_returns.png", dpi=160)
    plt.close(fig)

    fig, axis = plt.subplots(figsize=(14, 11))
    sns.heatmap(correlation, cmap="vlag", center=0, ax=axis)
    axis.set_title("Return correlation matrix")
    fig.tight_layout()
    fig.savefig(output_dir / "correlation_matrix.png", dpi=160)
    plt.close(fig)


def run(stock_dir: Path, commodity_dir: Path, output_dir: Path) -> None:
    """Execute the complete local workflow."""
    output_dir.mkdir(parents=True, exist_ok=True)
    prices = prepare_prices(stock_dir, commodity_dir)
    returns, summary, correlation = calculate_outputs(prices)

    prices.to_csv(output_dir / "cleaned_market_prices.csv", index=False)
    returns.to_csv(output_dir / "daily_returns.csv")
    summary.to_csv(output_dir / "market_summary.csv")
    correlation.to_csv(output_dir / "return_correlations.csv")
    save_charts(summary, correlation, output_dir)

    print(f"Processed {len(prices):,} dates across {prices.shape[1] - 1} price series.")
    print(f"Outputs saved to {output_dir.resolve()}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stock-dir", type=Path, required=True)
    parser.add_argument("--commodity-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("data/processed"))
    return parser


if __name__ == "__main__":
    arguments = build_parser().parse_args()
    run(arguments.stock_dir, arguments.commodity_dir, arguments.output_dir)
