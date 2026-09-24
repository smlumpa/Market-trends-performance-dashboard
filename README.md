# Market Trends & Performance Dashboard

**Power BI · Google BigQuery · Python · Power Query · Market Analytics**

An end-to-end portfolio project examining historical stock-market indices and commodity prices. It combines BigQuery-based analytical tables, Python analysis and an interactive Power BI dashboard.

![Dashboard preview](images/dashboard_screenshot.png)

## Live dashboard

[Open the interactive Power BI dashboard](https://app.powerbi.com/view?r=eyJrIjoiMzc0OGFiNmUtNmQ0OS00YWYxLTg4MzUtYWViNjFmYzkwMWQzIiwidCI6ImVlZDg0YTBlLWM3YTQtNDM1ZC05ZWQ1LTU4ODQwODgyYmMyOSJ9&pageName=d3fbaee262c4ba3b1b43)

## Business questions

- How did major global stock indices perform over the period analysed?
- Which markets and commodities produced the strongest average returns?
- Which assets showed the greatest volatility?
- How did performance vary by asset category and over time?
- How did major geo-economic events coincide with market movements?
- How can an interactive dashboard support cross-market comparison?

## Verified Power BI model scope

The model was verified from `Market Analysis Dashboard(1).vpax`, exported on 24 September 2026.

| Model component | Verified value |
|---|---:|
| Stock-market series | 19 |
| Commodity series | 19 |
| Combined series | 38 |
| Return dates | 4,380 |
| Joined price rows | 4,381 |
| Long-form stock-return rows | 83,220 |
| Long-form commodity-return rows | 83,220 |
| Combined long-form return rows | 166,440 |
| Geo-economic events | 29 |

The model also contains separate average-return and standard-deviation tables for the 19 stock-market series and 19 commodity series.

## Tools and techniques

- Google BigQuery for analytical storage and prepared return tables
- Python with pandas, NumPy, Matplotlib and Seaborn
- Power BI and Power Query
- Data cleaning, reshaping and joining
- Return and volatility analysis
- Long-form data preparation for interactive comparisons
- Geo-economic event annotation
- Interactive dashboard design

## Data pipeline

```text
Authorised source CSV files
        ↓
Python / analytical preparation
        ↓
Google BigQuery — Final schema
        ↓
Power Query transformations
        ↓
Power BI dashboard
```

The verified Power BI model connects directly to BigQuery tables in the `Final` schema. Two supporting Excel files provide geo-economic events and stock classifications.

## BigQuery tables used by Power BI

- `avg_return_commodities`
- `avg_return_stock_market`
- `commodities_return`
- `row_commodities_return`
- `row_commodities_stock_market_return`
- `row_stock_market_returns`
- `std_dev_commodities`
- `std_dev_stock_market`
- `stock_commodities_joined`
- `stock_commodities_return_joined`
- `stock_market_returns`

## Repository contents

```text
Market-trends-performance-dashboard/
├── dashboard/
│   └── Market_Analysis_Dashboard.pbix
├── data/
│   └── README.md
├── docs/
│   └── methodology.md
├── images/
├── python/
│   └── market_analysis.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Analytical workflow

1. Load authorised historical market and commodity files.
2. Standardise dates and price fields.
3. Combine the individual price series.
4. Calculate and reshape market and commodity returns.
5. Store prepared analytical tables in BigQuery.
6. Connect Power BI to the BigQuery `Final` schema.
7. Apply presentation transformations in Power Query.
8. Compare returns, volatility, categories and events in the dashboard.

See [the methodology](docs/methodology.md) for definitions, assumptions and limitations.

## Run the local Python analysis

The complete source downloads are not redistributed in this repository. Place legitimately obtained CSV files in two local directories and run:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python python/market_analysis.py \
  --stock-dir "/path/to/Stock Market Prices" \
  --commodity-dir "/path/to/Commodity Spot Prices" \
  --output-dir "data/processed"
```

The local script creates cleaned prices, daily returns, summary metrics, a correlation matrix and chart images. Its output counts depend on the authorised source files supplied by the user; they should not be substituted for the VPAX-verified Power BI model counts above.

## Data source and use

The original historical price files were downloaded from Investing.com for an educational portfolio project. They are not included here. Users should obtain data directly from a source they are authorised to use and follow that provider's applicable terms.

This analysis is for educational and portfolio purposes only. It is not investment advice, and historical performance does not predict future results.

## Author

**Sophia Lumpa**  
Business Intelligence & Operations Analyst  
[Portfolio website](https://www.virtavis.com/)
