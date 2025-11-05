#!/usr/bin/env python3
"""
Data Summary Generator
Creates daily summaries and statistics from collected development economics data
"""

import json
import csv
import os
from datetime import datetime, timedelta
import glob

def generate_currency_summary():
    """Generate summary of currency rate trends"""
    
    print("\n" + "="*60)
    print("💱 CURRENCY RATE SUMMARY")
    print("="*60)
    
    # Check if we have historical data
    history_file = "data/currency_rates/history.csv"
    
    if not os.path.exists(history_file):
        print("⚠️ No historical currency data available yet")
        return
    
    # Read historical data
    with open(history_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    if not data:
        print("⚠️ No currency data in history file")
        return
    
    print(f"📊 Total data points: {len(data)}")
    
    # Get unique dates
    dates = sorted(set(row['Date'] for row in data))
    print(f"📅 Date range: {dates[0]} to {dates[-1]}")
    print(f"📈 Days tracked: {len(dates)}")
    
    # Show latest rates for key currencies
    latest_date = dates[-1]
    latest_data = [row for row in data if row['Date'] == latest_date]
    
    print(f"\n📍 Latest rates as of {latest_date}:")
    print("-"*60)
    
    key_currencies = ['CNY', 'INR', 'BRL', 'ZAR', 'IDR', 'MXN', 'NGN', 'TRY']
    
    for currency in key_currencies:
        currency_data = [row for row in latest_data if row['Currency'] == currency]
        if currency_data:
            rate = float(currency_data[0]['Rate_to_USD'])
            print(f"  {currency}: {rate:.4f}")
    
    return True

def generate_overall_summary():
    """Generate overall project summary"""
    
    print("\n" + "="*60)
    print("📊 DAILY DEVELOPMENT ECONOMICS MONITOR - SUMMARY")
    print("="*60)
    
    print(f"\n🕐 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    # Count data points
    currency_files = len(glob.glob("data/currency_rates/*.json"))
    commodity_files = len(glob.glob("data/commodity_prices/*.json"))
    food_files = len(glob.glob("data/food_prices/*.json"))
    
    print(f"\n📁 Data Collection Status:")
    print(f"  💱 Currency rate snapshots: {currency_files}")
    print(f"  🛢️ Commodity price records: {commodity_files}")
    print(f"  🌾 Food price index records: {food_files}")
    
    # Check for latest data
    if os.path.exists("data/currency_rates/latest.csv"):
        print(f"\n✅ Latest currency data available")
    
    print("\n🌍 Impact Areas Being Monitored:")
    print("  • Exchange rate volatility in developing economies")
    print("  • Food security through commodity price tracking")
    print("  • Energy costs affecting economic development")
    print("  • Agricultural commodity trends for farmer livelihoods")
    
    print("\n📈 Building Historical Dataset...")
    print("  Over time, this project will create a comprehensive")
    print("  database of development-critical economic indicators")
    print("  useful for research, policy analysis, and forecasting.")
    
    # Save summary to file
    summary_data = {
        'generated': datetime.now().isoformat(),
        'data_counts': {
            'currency_snapshots': currency_files,
            'commodity_records': commodity_files,
            'food_price_records': food_files
        }
    }
    
    os.makedirs('data/summaries', exist_ok=True)
    summary_file = f"data/summaries/summary_{datetime.now().strftime('%Y-%m-%d')}.json"
    
    with open(summary_file, 'w') as f:
        json.dump(summary_data, f, indent=2)
    
    print(f"\n💾 Summary saved: {summary_file}")
    
    return True

def main():
    """Main execution function"""
    
    print("="*60)
    print("📊 Development Economics Data Summary Generator")
    print("="*60)
    
    generate_currency_summary()
    generate_overall_summary()
    
    print("\n" + "="*60)
    print("✅ Summary generation completed!")
    print("="*60 + "\n")
    
    return 0

if __name__ == "__main__":
    exit(main())
