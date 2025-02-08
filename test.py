import requests
import pandas as pd

# Replace with your actual API key
API_KEY = "zCExzG5atbZqlgGeHWrpVr7Ja9DfKQ9vEBDpyZLw"
URL = f"https://developer.nrel.gov/api/alt-fuel-stations/v1.json?api_key={API_KEY}"

# Request data from NREL API
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    stations = data["fuel_stations"]  # Extract charging station data
    
    # Convert to DataFrame
    df = pd.DataFrame(stations)
    
    # Save to CSV (optional)
    df.to_csv("ev_charging_stations.csv", index=False)
    
    print("Data successfully fetched and saved!")
else:
    print("Failed to fetch data:", response.status_code)
