# Methodology

## Scope

This portfolio project compares historical prices and returns across major global stock indices and commodities. It demonstrates an analytical workflow rather than providing investment recommendations.

## Preparation

1. Read each source CSV using its `Date` and `Price` fields.
2. Convert dates and formatted price strings into consistent types.
3. Remove invalid rows and duplicate dates within each series.
4. Outer-join the individual series on date.
5. Forward-fill the most recently observed price when trading calendars differ.
6. Remove the remaining leading incomplete observations.

Forward filling is used only after sorting by date. Backward filling is avoided because it would introduce future values into earlier observations.

## Measures

Daily return for asset *i* on date *t*:

```text
return(i,t) = price(i,t) / price(i,t-1) - 1
```

Annualised average return:

```text
mean(daily returns) × 260
```

Annualised volatility:

```text
standard deviation(daily returns) × square root(260)
```

Correlation uses Pearson correlation between the calculated daily-return series.

## Important limitations

- Different exchanges observe different holidays and trading hours.
- Forward filling simplifies cross-market alignment and may create zero returns on non-trading days.
- Currency differences are not adjusted unless the source data already uses a common currency.
- Historical relationships can change and do not predict future results.
- Dataset coverage differs between instruments.
- The calculations do not include fees, taxation, inflation or investability constraints.

## Original workflow

The original analysis was developed in Google Colab and used Google BigQuery for intermediate storage. This repository provides a local CSV workflow so reviewers can inspect the logic without access to the original cloud project.
