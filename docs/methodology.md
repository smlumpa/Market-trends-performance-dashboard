# Methodology

## Scope

This portfolio project compares historical prices and returns across major global stock indices and commodities. It demonstrates an analytical and business-intelligence workflow rather than providing investment recommendations.

## Verified architecture

The Power BI model was inspected using `Market Analysis Dashboard(1).vpax`, exported on 24 September 2026.

- Eleven analytical tables are imported from Google BigQuery.
- The BigQuery connection uses the `kavsh-project` project and `Final` schema.
- Two supporting Excel tables provide geo-economic events and stock classifications.
- The model contains 19 stock-market series and 19 commodity series.
- The combined return table contains 4,380 dates and 38 return series.
- Long-form tables support category and series comparisons in Power BI.

## Preparation

The accompanying local Python workflow:

1. Reads each authorised source CSV using its `Date` and `Price` fields.
2. Converts dates and formatted prices into consistent types.
3. Removes invalid rows and duplicate dates.
4. Outer-joins individual series by date.
5. Forward-fills the most recently observed price when trading calendars differ.
6. Avoids backward filling so future values are not introduced into earlier observations.
7. Calculates daily returns, summary statistics and correlations.
8. Produces cleaned analytical outputs and charts.

The production dashboard uses prepared BigQuery tables. The local Python script provides inspectable portfolio logic and may produce different row counts when run with a different set or version of source files.

## Measures

Daily return for asset *i* on date *t*:

```text
return(i,t) = price(i,t) / price(i,t-1) - 1
```

The local Python script calculates annualised arithmetic average return as:

```text
mean(daily returns) × 260
```

Annualised volatility is calculated as:

```text
standard deviation(daily returns) × square root(260)
```

Correlation uses Pearson correlation between calculated daily-return series.

## Power BI presentation layer

Power Query:

- Connects to the BigQuery `Final` schema.
- Assigns date and numeric types.
- Cleans market and commodity labels.
- Rounds selected return and standard-deviation values.
- Reshapes percentage fields for presentation.
- Imports geo-economic events and stock classifications from supporting Excel files.

The calculations displayed in the dashboard are primarily supplied by the prepared analytical tables; the inspected model does not contain a separate set of report-level DAX measures.

## Important limitations

- Different exchanges observe different holidays and trading hours.
- Forward filling simplifies cross-market alignment and may create zero returns on non-trading days.
- Currency differences are not adjusted unless the source data already uses a common currency.
- Historical relationships can change and do not predict future results.
- Dataset coverage differs between instruments.
- The calculations do not include fees, taxation, inflation or investability constraints.
- The dashboard is educational and is not investment advice.
