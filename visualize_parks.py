import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the CSV file
csv_file = 'nationalparks.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Create a base map centered around the average latitude and longitude
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
mymap = folium.Map(location=map_center, zoom_start=4)

# Initialize MarkerCluster
marker_cluster = MarkerCluster().add_to(mymap)

# Add markers for each national park to the MarkerCluster
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['National Park Name'],  # Display the park name in the popup
        icon=folium.Icon(color='green', icon='tree-conifer')  # Customize the icon
    ).add_to(marker_cluster)

# Save the map to an HTML file
output_file = 'national_parks_clustered_map.html'
mymap.save(output_file)

print(f"National Parks Map with Marker Clusters was saved to {output_file}. Open it in a web browser to view.")
