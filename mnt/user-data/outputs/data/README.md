# Development Economics Data

This directory contains the collected economic data for development analysis.

## Directory Structure

- **currency_rates/** - Daily currency exchange rate data
  - Individual daily JSON and CSV files
  - `latest.csv` - Most recent rates
  - `history.csv` - Complete historical record

- **commodity_prices/** - Monthly World Bank commodity price data
  - Individual monthly records
  - `template.csv` - Template for manual updates

- **food_prices/** - Monthly FAO Food Price Index data
  - Individual monthly records
  - `fao_index.csv` - Historical index values

- **summaries/** - Daily analysis summaries
  - JSON files with statistics and insights

## Data Updates

- Currency rates: Updated daily via GitHub Actions
- Commodity prices: Updated monthly (check first business day)
- Food price index: Updated monthly (check first Thursday)

## Using the Data

All data files are in standard CSV and JSON formats for easy analysis with:
- Python (pandas, matplotlib)
- R (tidyverse, ggplot2)
- Excel/Google Sheets
- Tableau/Power BI
- Any statistical software

## Data Quality

- Currency data sourced from European Central Bank via Frankfurter API
- Commodity data from World Bank Pink Sheet
- Food index from UN FAO
- All sources are authoritative and widely used in development research

---

**Note**: This dataset grows over time. The longer the project runs, the more valuable the historical dataset becomes for trend analysis and forecasting.
