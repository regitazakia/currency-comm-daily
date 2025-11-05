# 🚀 Quick Start Guide

## Setup (5 minutes)

### 1. Create Your Repository
```bash
# Option A: Create a new repo on GitHub
# - Go to github.com/new
# - Name it: "dev-economics-monitor" or similar
# - Make it public (for free Actions minutes)
# - Don't initialize with README (we have one)

# Option B: Use GitHub CLI
gh repo create dev-economics-monitor --public
```

### 2. Upload Files
Upload all the files from this project to your new repository, maintaining the directory structure:
```
your-repo/
├── .github/workflows/daily-update.yml
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── QUICKSTART.md (this file)
├── data/
│   ├── README.md
│   └── currency_rates/EXAMPLE_2025-11-04.csv
└── scripts/
    ├── fetch_currency_rates.py
    ├── fetch_commodity_prices.py
    ├── fetch_food_prices.py
    └── generate_summary.py
```

### 3. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click the **"Actions"** tab
3. Click **"I understand my workflows, go ahead and enable them"**

### 4. Configure Permissions

1. Go to **Settings** → **Actions** → **General**
2. Scroll to **"Workflow permissions"**
3. Select **"Read and write permissions"**
4. Check **"Allow GitHub Actions to create and approve pull requests"**
5. Click **"Save"**

### 5. Test It!

1. Go to **Actions** tab
2. Click **"Daily Development Economics Update"** workflow
3. Click **"Run workflow"** dropdown
4. Click green **"Run workflow"** button
5. Watch it run! (takes ~30 seconds)

## What Happens Next?

✅ **Daily (6:00 AM UTC)**: Currency rates automatically update
✅ **Data accumulates**: Historical dataset grows over time
✅ **Green squares**: Your GitHub contribution graph stays active
✅ **Real value**: You're building a useful development economics dataset!

## Viewing Your Data

After the first run, you'll have:
- `data/currency_rates/YYYY-MM-DD.csv` - Daily currency rates
- `data/currency_rates/latest.csv` - Most recent rates
- `data/currency_rates/history.csv` - All historical data
- `data/summaries/summary_YYYY-MM-DD.json` - Daily statistics

## Using the Data

```python
import pandas as pd

# Load currency rates
df = pd.read_csv('data/currency_rates/history.csv')

# Analyze Indian Rupee trend
inr = df[df['Currency'] == 'INR']
print(inr)

# Compare multiple currencies
import matplotlib.pyplot as plt
for currency in ['INR', 'BRL', 'ZAR']:
    data = df[df['Currency'] == currency]
    plt.plot(data['Date'], data['Rate_to_USD'], label=currency)
plt.legend()
plt.show()
```

## Manual Updates (Optional)

For commodity and food price data (updated monthly):

1. Check the data sources (listed in README.md)
2. Update the template files in `data/commodity_prices/` and `data/food_prices/`
3. Commit and push the changes

## Customization

Want to track different currencies? Edit `scripts/fetch_currency_rates.py`:
```python
CURRENCIES = [
    'USD', 'EUR', 'GBP',  # Add or remove currencies
    'YOUR_CURRENCY_HERE',  # Add any ISO currency code
]
```

Want different update times? Edit `.github/workflows/daily-update.yml`:
```yaml
schedule:
  - cron: '0 12 * * *'  # Change to 12:00 UTC (noon)
```

## Troubleshooting

**"No changes to commit" in Actions**
- Normal! This means the data hasn't changed since last run
- Currency markets are closed on weekends

**"Workflow permissions" error**
- Make sure you enabled "Read and write permissions" in Settings

**Want to see what the workflow does?**
- Check the Actions tab → Click on a workflow run → View logs

## Next Steps

1. ⭐ Star the original project if you found this helpful!
2. 📊 Share your data analysis findings
3. 🤝 Contribute improvements back to the project
4. 📚 Use the data in research papers or reports
5. 🌍 Help make development data more accessible

## Need Help?

- Check the [main README](README.md) for detailed documentation
- View the [data README](data/README.md) for data structure info
- Review workflow runs in the Actions tab for debugging

---

**You're now tracking global development economics daily! 🎉**
