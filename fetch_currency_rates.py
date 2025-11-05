#!/usr/bin/env python3
"""
Currency Exchange Rate Fetcher
Fetches daily exchange rates for key developing economy currencies
Data source: Frankfurter API (European Central Bank)
"""

import requests
import json
import csv
from datetime import datetime
import os

# Key currencies for development economics
# Focus on major developing economies and trade currencies
CURRENCIES = [
    'USD',  # US Dollar - global reserve
    'EUR',  # Euro - major trade currency
    'GBP',  # British Pound
    'JPY',  # Japanese Yen
    'CNY',  # Chinese Yuan - largest developing economy
    'INR',  # Indian Rupee - major developing economy
    'BRL',  # Brazilian Real - Latin America
    'MXN',  # Mexican Peso - Latin America
    'ZAR',  # South African Rand - Africa
    'NGN',  # Nigerian Naira - Africa
    'EGP',  # Egyptian Pound - Africa
    'KES',  # Kenyan Shilling - Africa
    'IDR',  # Indonesian Rupiah - Southeast Asia
    'PHP',  # Philippine Peso - Southeast Asia
    'VND',  # Vietnamese Dong - Southeast Asia
    'THB',  # Thai Baht - Southeast Asia
    'TRY',  # Turkish Lira - Middle East
    'ARS',  # Argentine Peso - Latin America
    'COP',  # Colombian Peso - Latin America
    'PKR',  # Pakistani Rupee - South Asia
    'BGD',  # Bangladeshi Taka - South Asia (using BGN as proxy, BGD not in standard ISO)
    'CHF',  # Swiss Franc - safe haven
    'CAD',  # Canadian Dollar
    'AUD',  # Australian Dollar
    'NZD',  # New Zealand Dollar
]

def fetch_currency_rates():
    """Fetch latest currency exchange rates from Frankfurter API"""
    
    print("🌍 Fetching currency exchange rates...")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    try:
        # Fetch latest rates with USD as base
        url = "https://api.frankfurter.dev/v1/latest"
        params = {
            'base': 'USD',
            'symbols': ','.join(CURRENCIES)
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract data
        date = data['date']
        base = data['base']
        rates = data['rates']
        
        print(f"✅ Successfully fetched rates for {date}")
        print(f"📊 Base currency: {base}")
        print(f"💱 Rates retrieved: {len(rates)} currencies")
        
        return {
            'date': date,
            'timestamp': datetime.now().isoformat(),
            'base_currency': base,
            'rates': rates
        }
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching currency rates: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def save_data(data):
    """Save currency data to CSV and JSON formats"""
    
    if not data:
        print("⚠️ No data to save")
        return False
    
    # Create data directory if it doesn't exist
    os.makedirs('data/currency_rates', exist_ok=True)
    
    date = data['date']
    timestamp = data['timestamp']
    
    # Save as JSON
    json_filename = f"data/currency_rates/{date}.json"
    with open(json_filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"💾 Saved JSON: {json_filename}")
    
    # Save as CSV
    csv_filename = f"data/currency_rates/{date}.csv"
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Timestamp', 'Currency', 'Rate_to_USD'])
        
        for currency, rate in sorted(data['rates'].items()):
            writer.writerow([date, timestamp, currency, rate])
    
    print(f"💾 Saved CSV: {csv_filename}")
    
    # Update latest.csv (overwrite with most recent data)
    latest_csv = "data/currency_rates/latest.csv"
    with open(latest_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Timestamp', 'Currency', 'Rate_to_USD'])
        
        for currency, rate in sorted(data['rates'].items()):
            writer.writerow([date, timestamp, currency, rate])
    
    print(f"💾 Updated: {latest_csv}")
    
    # Append to historical file
    history_csv = "data/currency_rates/history.csv"
    file_exists = os.path.exists(history_csv)
    
    with open(history_csv, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow(['Date', 'Timestamp', 'Currency', 'Rate_to_USD'])
        
        # Append all rates
        for currency, rate in sorted(data['rates'].items()):
            writer.writerow([date, timestamp, currency, rate])
    
    print(f"📊 Appended to historical data: {history_csv}")
    
    return True

def generate_summary(data):
    """Generate a quick summary of interesting rate changes"""
    
    if not data:
        return
    
    print("\n" + "="*60)
    print("📈 CURRENCY RATE SUMMARY")
    print("="*60)
    print(f"Date: {data['date']}")
    print(f"Base: {data['base_currency']}")
    print(f"\nKey Developing Economy Rates (1 USD =):")
    print("-"*60)
    
    # Highlight key developing economy currencies
    key_currencies = {
        'INR': 'Indian Rupee',
        'CNY': 'Chinese Yuan',
        'BRL': 'Brazilian Real',
        'ZAR': 'South African Rand',
        'IDR': 'Indonesian Rupiah',
        'MXN': 'Mexican Peso',
        'TRY': 'Turkish Lira',
        'NGN': 'Nigerian Naira',
    }
    
    for code, name in key_currencies.items():
        if code in data['rates']:
            rate = data['rates'][code]
            print(f"{code} ({name}): {rate:.4f}")
    
    print("="*60 + "\n")

def main():
    """Main execution function"""
    
    print("="*60)
    print("💰 Daily Currency Exchange Rate Fetcher")
    print("="*60 + "\n")
    
    # Fetch data
    data = fetch_currency_rates()
    
    if data:
        # Save data
        if save_data(data):
            # Generate summary
            generate_summary(data)
            print("✅ Currency rate update completed successfully!")
            return 0
        else:
            print("❌ Failed to save data")
            return 1
    else:
        print("❌ Failed to fetch currency rates")
        return 1

if __name__ == "__main__":
    exit(main())
