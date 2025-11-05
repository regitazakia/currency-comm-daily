#!/usr/bin/env python3
"""
Commodity Price Fetcher
Checks for and downloads World Bank commodity price data (Pink Sheet)
Focuses on commodities critical to development economics
"""

import requests
import json
import csv
from datetime import datetime
import os

def fetch_commodity_prices():
    """
    Fetch commodity prices from World Bank Pink Sheet data
    Note: This data is updated monthly, typically on the first business day
    """
    
    print("🛢️ Checking World Bank commodity prices...")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    # World Bank Pink Sheet URL (they provide Excel/CSV downloads)
    # This is a simplified approach - in practice, you'd parse their Excel files
    # For now, we'll create a structure to manually update or scrape
    
    print("\n⚠️ Note: World Bank commodity data updates monthly")
    print("📊 Data should be manually updated from:")
    print("   https://www.worldbank.org/en/research/commodity-markets")
    print("   or https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Pink-Sheet-[Month]-[Year].pdf")
    
    # Create placeholder structure
    commodity_data = {
        'timestamp': datetime.now().isoformat(),
        'date': datetime.now().strftime('%Y-%m'),
        'source': 'World Bank Commodity Price Data (Pink Sheet)',
        'note': 'Monthly data - requires manual update or API when available',
        'commodities': {
            'energy': {
                'crude_oil_brent': {'unit': '$/bbl', 'price': None},
                'crude_oil_wti': {'unit': '$/bbl', 'price': None},
                'crude_oil_dubai': {'unit': '$/bbl', 'price': None},
                'natural_gas_us': {'unit': '$/mmbtu', 'price': None},
                'natural_gas_europe': {'unit': '$/mmbtu', 'price': None},
                'coal_australia': {'unit': '$/mt', 'price': None},
            },
            'agriculture': {
                'wheat_us': {'unit': '$/mt', 'price': None},
                'rice_thailand': {'unit': '$/mt', 'price': None},
                'maize': {'unit': '$/mt', 'price': None},
                'soybeans': {'unit': '$/mt', 'price': None},
                'sugar': {'unit': '¢/kg', 'price': None},
                'coffee_arabica': {'unit': '$/kg', 'price': None},
                'coffee_robusta': {'unit': '$/kg', 'price': None},
                'tea_mombasa': {'unit': '$/kg', 'price': None},
                'cocoa': {'unit': '$/kg', 'price': None},
            },
            'fertilizers': {
                'dap': {'unit': '$/mt', 'price': None},
                'tsp': {'unit': '$/mt', 'price': None},
                'urea': {'unit': '$/mt', 'price': None},
            },
            'metals': {
                'aluminum': {'unit': '$/mt', 'price': None},
                'copper': {'unit': '$/mt', 'price': None},
                'iron_ore': {'unit': '$/dmt', 'price': None},
                'gold': {'unit': '$/toz', 'price': None},
            }
        }
    }
    
    return commodity_data

def save_commodity_data(data):
    """Save commodity price data"""
    
    os.makedirs('data/commodity_prices', exist_ok=True)
    
    date = data['date']
    
    # Save as JSON
    json_filename = f"data/commodity_prices/{date}.json"
    with open(json_filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"💾 Saved commodity data: {json_filename}")
    
    # Create a template CSV for manual updates
    csv_filename = "data/commodity_prices/template.csv"
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Category', 'Commodity', 'Unit', 'Price', 'Source'])
        
        for category, commodities in data['commodities'].items():
            for commodity, details in commodities.items():
                writer.writerow([
                    date,
                    category,
                    commodity,
                    details['unit'],
                    details['price'] if details['price'] else 'UPDATE_ME',
                    'World Bank Pink Sheet'
                ])
    
    print(f"📋 Created template: {csv_filename}")
    print("\n📝 Instructions:")
    print("1. Visit: https://www.worldbank.org/en/research/commodity-markets")
    print("2. Download the latest Pink Sheet (PDF/Excel)")
    print("3. Update the template.csv with current prices")
    print("4. Run this script to process and archive the data")
    
    return True

def main():
    """Main execution function"""
    
    print("="*60)
    print("📊 World Bank Commodity Price Checker")
    print("="*60 + "\n")
    
    data = fetch_commodity_prices()
    save_commodity_data(data)
    
    print("\n✅ Commodity price template created!")
    print("⚠️ Note: Requires manual data entry from World Bank source")
    
    return 0

if __name__ == "__main__":
    exit(main())
