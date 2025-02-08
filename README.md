# EV Charging & National Parks Visualization

## Setup

1. Clone the repository:
    
    ```jsx
    git clone https://github.com/noah23olsen/EV-Infrastructure 
    ```
    
    ```jsx
    cd EV-Infrastructure
    ```
    
2. Create a virtual environment:
    
    ```jsx
    python -m venv venv
    ```
    

3. Activate the virtual environment
    
    ```jsx
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate  # Windows
    ```
3. Install dependencies:
    
    ```jsx
    pip install -r requirements.txt
    ```
    
4. Generate & open the map
    
    ```jsx
    python map.py && open map.html
    ```
    

## Description

- Generates a heatmap for EV charging stations.
- Interactive layers allow toggling stations, parks, and the heatmap.

## Notes

- Uses Folium for mapping.
- Data comes from EV charging station and National Parks datasets.
- Designed for visualizing charging infrastructure in relation to National Parks.