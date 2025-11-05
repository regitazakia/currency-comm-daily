# 📊 Daily Development Economics Monitor

A meaningful GitHub project that tracks key economic indicators affecting international development: currency exchange rates, commodity prices, and food price indices. This project automatically pulls data daily and builds a historical dataset useful for development research and policy analysis.

## 🎯 Purpose

This project serves development researchers, economists, and policymakers by:
- Tracking currency rates for developing economies
- Monitoring commodity prices that affect poverty and food security
- Building a historical database of development-critical economic indicators
- Providing daily updates on data that impacts billions of people globally

## 📈 Data Sources

### 1. **Currency Exchange Rates** (Updated Daily)
- **Source**: Frankfurter API (European Central Bank data)
- **Coverage**: 30+ currencies including major developing economy currencies
- **Update Frequency**: Daily (weekdays)
- **Key Currencies Tracked**:
  - USD (US Dollar) - Global reserve currency
  - EUR (Euro) - Major trade currency
  - CNY (Chinese Yuan) - Largest developing economy
  - INR (Indian Rupee) - Large developing economy
  - BRL (Brazilian Real) - Latin America
  - ZAR (South African Rand) - Africa
  - And more...

### 2. **Commodity Prices** (Updated Monthly)
- **Source**: World Bank Commodity Price Data (Pink Sheet)
- **Coverage**: Energy, agriculture, metals
- **Update Frequency**: Monthly (first business day)
- **Key Commodities**:
  - Crude Oil (Brent, WTI) - Energy costs
  - Natural Gas - Energy access
  - Wheat, Rice, Maize - Food security
  - Coffee, Tea, Sugar - Cash crops
  - Fertilizers - Agricultural inputs

### 3. **Food Price Index** (Updated Monthly)
- **Source**: FAO Food Price Index
- **Coverage**: Global food commodity basket
- **Update Frequency**: Monthly (first Thursday)
- **Components**:
  - Cereals - Staple foods
  - Dairy - Protein source
  - Meat - Protein source
  - Oils/Fats - Cooking essentials
  - Sugar - Basic commodity

## 🚀 How It Works

1. **Daily Automation**: GitHub Actions runs every day at 06:00 UTC
2. **Data Collection**: 
   - Currency rates are fetched daily
   - Commodity and food price data are checked for monthly updates
3. **Data Storage**: Results saved in CSV and JSON formats
4. **Historical Building**: Over time, builds a comprehensive dataset
5. **Visualization**: Generates summary statistics and trends

## 📁 Project Structure

```
├── data/
│   ├── currency_rates/      # Daily currency exchange rates
│   ├── commodity_prices/    # Monthly commodity prices
│   ├── food_prices/         # Monthly FAO Food Price Index
│   └── summaries/           # Analysis summaries
├── scripts/
│   ├── fetch_currency_rates.py
│   ├── fetch_commodity_prices.py
│   ├── fetch_food_prices.py
│   └── generate_summary.py
├── .github/workflows/
│   └── daily-update.yml
└── README.md
```

## 🛠️ Setup Instructions

### 1. Fork or Clone This Repository

```bash
git clone https://github.com/yourusername/dev-economics-monitor.git
cd dev-economics-monitor
```

### 2. Enable GitHub Actions

- Go to the **Actions** tab in your repository
- Click "I understand my workflows, go ahead and enable them"

### 3. Configure Workflow Permissions

- Go to **Settings → Actions → General**
- Under "Workflow permissions", select **"Read and write permissions"**
- Check **"Allow GitHub Actions to create and approve pull requests"**
- Click **Save**

### 4. Manual First Run (Optional)

- Go to **Actions** tab
- Select "Daily Development Economics Update"
- Click **"Run workflow"** to test immediately

## 📊 Using The Data

### Currency Rates
```python
import pandas as pd

# Load latest currency rates
df = pd.read_csv('data/currency_rates/latest.csv')
print(df)
```

### Commodity Prices
```python
# Load commodity price history
df = pd.read_csv('data/commodity_prices/history.csv')
oil_prices = df[df['commodity'] == 'crude_oil_brent']
```

### Food Price Index
```python
# Load FAO Food Price Index
df = pd.read_csv('data/food_prices/fao_index.csv')
```

## 🌍 Development Impact

This data helps understand:

- **Exchange Rate Volatility**: Currency instability affecting developing economies
- **Food Security**: Rising food prices impact poverty and hunger
- **Energy Costs**: Oil/gas prices affect economic growth and inflation
- **Agricultural Economics**: Commodity prices impact farmer livelihoods
- **Trade Balance**: Import/export dynamics for developing nations

## 📅 Update Schedule

- **Daily** (6:00 AM UTC): Currency exchange rates
- **Monthly** (1st business day): Commodity prices check
- **Monthly** (1st Thursday): Food price index check
- **Continuous**: Historical data accumulation

## 🤝 Contributing

This is a research project! Contributions welcome:
- Additional data sources
- Better visualizations
- Analysis scripts
- Regional focus expansions

## 📖 References

- [World Bank Commodity Markets](https://www.worldbank.org/en/research/commodity-markets)
- [FAO Food Price Index](https://www.fao.org/worldfoodsituation/foodpricesindex/en/)
- [Frankfurter Currency API](https://frankfurter.dev/)
- [European Central Bank](https://www.ecb.europa.eu/)

## 📝 License

MIT License - Free for research and educational purposes

## 🎓 Citation

If you use this data in research, please cite:
```
Development Economics Monitor. (2025). Daily tracking of currency rates, 
commodity prices, and food security indicators. GitHub repository.
```

---

**Making Development Data Accessible, One Day at a Time** 🌍
