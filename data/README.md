# Data

The complete source datasets are intentionally not redistributed in this public repository.

The original project used historical stock-index and commodity-price CSV downloads from Investing.com. Reviewers can use equivalent authorised files containing at least:

```text
Date,Price
```

Optional source fields such as `Open`, `High`, `Low`, `Vol.` and `Change %` are ignored by the cleaned portfolio script.

Recommended local structure:

```text
data/
├── raw/
│   ├── stocks/
│   └── commodities/
└── processed/
```

The `.gitignore` file excludes raw and generated data so provider files are not accidentally committed.
