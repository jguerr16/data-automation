# csv_processor.py
import pandas as pd
import requests
from config import GOOGLE_MAPS_API_KEY

# Convert coordinates to city using Google Maps API
def get_city_from_coordinates(lat, lng):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            for component in results[0]['address_components']:
                if 'locality' in component['types']:
                    return component['long_name']
    return None

# Process the CSV and add city information
def process_csv(file_path):
    df = pd.read_csv(file_path)
    
    # Assume columns are named 'lat' and 'lng'
    df['city'] = df.apply(lambda row: get_city_from_coordinates(row['lat'], row['lng']), axis=1)
    
    # Save processed CSV with city info
    processed_file = file_path.replace('.csv', '_processed.csv')
    df.to_csv(processed_file, index=False)
    return processed_file
