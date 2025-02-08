import folium
import pandas as pd

# Load your dataset
data = pd.read_csv("ev_charging_stations.csv")

# Optional: Ensure no NaN values remain in latitude and longitude
data = data.dropna(subset=['latitude', 'longitude'])

# Create a base map centered over the US
us_map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

# Add points for the remaining data
for _, row in data.iterrows():
    try:
        # if the ev_dc_fast_num column is greater than 0 and not empty, continue, otherwise, stop

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
