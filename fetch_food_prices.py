#!/usr/bin/env python3
"""
FAO Food Price Index Fetcher
Monitors and logs the FAO Food Price Index
Updates monthly on the first Thursday of each month
"""

import requests
import json
import csv
from datetime import datetime
import os
import re
from bs4 import BeautifulSoup

def fetch_fao_food_price_index():
    """
    Attempt to fetch FAO Food Price Index
    The official data is on: https://www.fao.org/worldfoodsituation/foodpricesindex/en/
    """
    
    print("🌾 Checking FAO Food Price Index...")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    
    url = "https://www.fao.org/worldfoodsituation/foodpricesindex/en/"
    
    try:
        print(f"🔍 Fetching data from: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        # Parse the page to extract the latest index value
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # The FAO page structure may vary, this is a general approach
        print("📄 Page retrieved successfully")
        print("⚠️ Note: FAO data parsing requires page structure analysis")
        print("💡 Suggestion: Check page source and update parser accordingly")
        
        # Create data structure
        fao_data = {
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().strftime('%Y-%m'),
            'source': 'FAO Food Price Index',
            'url': url,
            'update_schedule': 'First Thursday of each month',
            'indices': {
                'overall_index': {'value': None, 'unit': 'points (2014-2016=100)'},
                'cereals': {'value': None, 'unit': 'points'},
                'vegetable_oils': {'value': None, 'unit': 'points'},
                'dairy': {'value': None, 'unit': 'points'},
                'meat': {'value': None, 'unit': 'points'},
                'sugar': {'value': None, 'unit': 'points'},
            },
            'note': 'Values need to be manually updated from FAO website'
        }
        
        return fao_data
        
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Could not fetch FAO page: {e}")
        print("💡 Creating template for manual update")
        
        fao_data = {
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().strftime('%Y-%m'),
            'source': 'FAO Food Price Index',
            'url': url,
            'update_schedule': 'First Thursday of each month',
            'indices': {
                'overall_index': {'value': None, 'unit': 'points (2014-2016=100)'},
                'cereals': {'value': None, 'unit': 'points'},
                'vegetable_oils': {'value': None, 'unit': 'points'},
                'dairy': {'value': None, 'unit': 'points'},
                'meat': {'value': None, 'unit': 'points'},
                'sugar': {'value': None, 'unit': 'points'},
            },
            'note': 'Values need to be manually updated from FAO website'
        }
        
        return fao_data

def save_fao_data(data):
    """Save FAO Food Price Index data"""
    
    os.makedirs('data/food_prices', exist_ok=True)
    
    date = data['date']
    
    # Save as JSON
    json_filename = f"data/food_prices/{date}.json"
    with open(json_filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"💾 Saved FAO data: {json_filename}")
    
    # Create CSV template
    csv_filename = "data/food_prices/fao_index.csv"
    file_exists = os.path.exists(csv_filename)
    
    with open(csv_filename, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write header if new file
        if not file_exists:
            writer.writerow([
                'Date',
                'Timestamp',
                'Overall_Index',
                'Cereals_Index',
                'Vegetable_Oils_Index',
                'Dairy_Index',
                'Meat_Index',
                'Sugar_Index',
                'Source'
            ])
        
        # Write data row
        writer.writerow([
            date,
            data['timestamp'],
            data['indices']['overall_index']['value'] or 'UPDATE_ME',
            data['indices']['cereals']['value'] or 'UPDATE_ME',
            data['indices']['vegetable_oils']['value'] or 'UPDATE_ME',
            data['indices']['dairy']['value'] or 'UPDATE_ME',
            data['indices']['meat']['value'] or 'UPDATE_ME',
            data['indices']['sugar']['value'] or 'UPDATE_ME',
            'FAO'
        ])
    
    print(f"📊 Updated FAO index file: {csv_filename}")
    
    print("\n📝 Manual Update Instructions:")
    print("1. Visit: https://www.fao.org/worldfoodsituation/foodpricesindex/en/")
    print("2. Find the latest monthly index values")
    print("3. Update fao_index.csv with current values")
    print("4. The index is updated on the first Thursday of each month")
    
    return True

def main():
    """Main execution function"""
    
    print("="*60)
    print("🌾 FAO Food Price Index Monitor")
    print("="*60 + "\n")
    
    data = fetch_fao_food_price_index()
    save_fao_data(data)
    
    print("\n✅ FAO Food Price Index template updated!")
    print("⚠️ Note: Requires manual data entry from FAO source")
    print("📅 Check on first Thursday of each month for new data")
    
    return 0

if __name__ == "__main__":
    # Install beautifulsoup4 if needed: pip install beautifulsoup4
    try:
        from bs4 import BeautifulSoup
        exit(main())
    except ImportError:
        print("⚠️ beautifulsoup4 not installed")
        print("Installing required package...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'beautifulsoup4', '--break-system-packages'])
        from bs4 import BeautifulSoup
        exit(main())
