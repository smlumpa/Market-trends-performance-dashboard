# Market Trends & Performance Dashboard

An end-to-end portfolio project examining historical stock-market indices and commodity prices. The project combines Python data preparation and analysis with an interactive Power BI report.

![Dashboard preview](images/dashboard_screenshot.png)

## Live dashboard

[Open the interactive Power BI dashboard](https://app.powerbi.com/view?r=eyJrIjoiMzc0OGFiNmUtNmQ0OS00YWYxLTg4MzUtYWViNjFmYzkwMWQzIiwidCI6ImVlZDg0YTBlLWM3YTQtNDM1ZC05ZWQ1LTU4ODQwODgyYmMyOSJ9&pageName=d3fbaee262c4ba3b1b43)

## Business questions

- How did major global stock indices perform over the period analysed?
- Which markets and commodities produced the highest annualised returns?
- Which assets showed the greatest volatility?
- How strongly were stock-market and commodity returns correlated?
- How can an interactive dashboard make cross-market comparison easier?

## Tools and techniques

- Python: pandas, NumPy, Matplotlib and Seaborn
- Power BI and data modelling
- Data cleaning, reshaping and joining
- Daily and annualised return calculations
- Annualised volatility and correlation analysis
- Interactive dashboard design
- Google BigQuery in the original project workflow

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

1. Load historical market and commodity CSV files.
2. Standardise dates and price fields.
3. Combine each series into a date-indexed dataset.
4. Align different trading calendars without using future information.
5. Calculate daily returns, annualised returns and annualised volatility.
6. Produce a correlation matrix and portfolio-ready outputs.
7. Present the results through Power BI.

See [the methodology](docs/methodology.md) for definitions, assumptions and limitations.

## Findings from the supplied project data

After aligning the available source series, the reproducible workflow produced 3,239 dated observations across 40 stock-index and commodity series, covering 16 June 2014 to 4 October 2024.

- The Dow Jones and S&P 500 daily returns had a correlation of **0.956**.
- The Nasdaq Composite and S&P 500 daily returns had a correlation of **0.947**.
- The CAC 40 and DAX daily returns had a correlation of **0.932**.
- The BIST 100 had the highest arithmetic annualised mean return in the aligned dataset at **22.3%**.
- WTI crude oil had the highest annualised volatility at **102.8%**, reflecting exceptional price behaviour during the period.

These figures describe this dataset only. Returns are not currency-adjusted, the annualised mean is not a compound annual growth rate, and the results should not be interpreted as investment recommendations.

## Run the Python analysis

The complete source downloads are not redistributed in this repository. Place legitimately obtained CSV files in two local directories and run:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python python/market_analysis.py \
  --stock-dir "/path/to/Stock Market Prices" \
  --commodity-dir "/path/to/Commodity Spot Prices" \
  --output-dir "data/processed"
```

The script creates cleaned prices, daily returns, summary metrics, a correlation matrix and two chart images.

## Data source and use

The original historical price files were downloaded from Investing.com for an educational portfolio project. They are not included here. Users should obtain data directly from a source they are authorised to use and follow that provider's applicable terms.

This analysis is for educational and portfolio purposes only. It is not investment advice, and historical performance does not predict future results.

## Author

**Sophia Lumpa**  
Business Intelligence & Operations Analyst  
[Portfolio website](https://www.virtavis.com/)
