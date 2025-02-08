import folium
import pandas as pd

# Load your dataset
data = pd.read_csv("ev_charging_stations.csv")

# Check if the dataset has latitude and longitude columns
print(data.head())  # Ensure you see the latitude and longitude columns

# Handle rows with missing latitude or longitude
# Get the first 100 rows with missing latitude or longitude
# nan_rows = data[data['latitude'].isna() | data['longitude'].isna()].head(100)
# print(f"First 100 rows with NaN values:\n{nan_rows}")

# # Drop these rows for now (avoiding plotting invalid data)
# data = data.drop(nan_rows.index)

# Optional: Ensure no NaN values remain in latitude and longitude
data = data.dropna(subset=['latitude', 'longitude'])

# Create a base map centered over the US
us_map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

# Add points for the remaining data
for _, row in data.iterrows():
    try:
        # Add a circle marker for each charging station
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            color="blue",  # Marker color
            fill=True,
            fill_color="blue",
            fill_opacity=0.6,
            popup=row.get("station_name", "Location")  # Popup to show station name
        ).add_to(us_map)
    except ValueError as e:
        # Handle any unexpected issues with invalid coordinates
        print(f"Error adding marker for row: {row} -> {e}")

# Save the map to an HTML file
us_map.save("us_map.html")
print("Map saved as us_map.html. Open it in your browser.")
