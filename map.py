import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the datasets
ev_data = pd.read_csv("ev_charging_stations.csv",
                    encoding='utf-8',
                    on_bad_lines='skip')

park_data = pd.read_csv("nationalparks.csv",
                    encoding='utf-8')

# Convert coordinates to numeric, handling errors gracefully
ev_data['latitude'] = pd.to_numeric(ev_data['latitude'], errors='coerce')
ev_data['longitude'] = pd.to_numeric(ev_data['longitude'], errors='coerce')
ev_data['ev_dc_fast_num'] = pd.to_numeric(ev_data['ev_dc_fast_num'], errors='coerce')

# Clean data
ev_data = ev_data.dropna(subset=['latitude', 'longitude'])
park_data = park_data.dropna(subset=['Latitude', 'Longitude'])

# Create base map
base_map = folium.Map(location=[39.8283, -98.5795],
                    zoom_start=5,
                    tiles='cartodbpositron')

# Create feature groups for different layers
heatmap_group = folium.FeatureGroup(name="Heatmap")
stations_group = folium.FeatureGroup(name="EV Stations")
parks_group = folium.FeatureGroup(name="National Parks")

# Prepare and add heatmap layer
dc_fast_stations = ev_data[ev_data['ev_dc_fast_num'] > 0]
heat_data = dc_fast_stations[['latitude', 'longitude']].values.tolist()

HeatMap(
    data=heat_data,
    radius=15,
    blur=10,
    max_zoom=12,
    min_opacity=0.3
).add_to(heatmap_group)

# Add individual station markers
for _, row in dc_fast_stations.iterrows():
    try:
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=1.5,  # Smaller radius
            color='#000080',  # Dark blue
            fill=True,
            fill_color='#4169E1',  # Royal blue
            fill_opacity=0.4,  # More transparent
            popup=row.get('station_name', 'EV Station')
        ).add_to(stations_group)
    except (ValueError, TypeError) as e:
        continue

# Add park markers
for _, row in park_data.iterrows():
    try:
        folium.Marker(
            location=[float(row['Latitude']), float(row['Longitude'])],
            popup=row['National Park Name'],
            icon=folium.Icon(color='darkgreen', icon='leaf')
        ).add_to(parks_group)
    except (ValueError, TypeError) as e:
        continue

# Add all layers to map
heatmap_group.add_to(base_map)
stations_group.add_to(base_map)
parks_group.add_to(base_map)

# Add layer control
folium.LayerControl().add_to(base_map)

# Save map
output_file = "map.html"
base_map.save(output_file)

# Print diagnostic information
print(f"Number of heatmap points: {len(heat_data)}")
print(f"Number of parks: {len(park_data)}")
print(f"Map saved to {output_file}")