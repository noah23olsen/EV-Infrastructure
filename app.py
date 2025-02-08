import kagglehub
import requests

# Download latest version
path = kagglehub.dataset_download("prasertk/electric-vehicle-charging-stations-in-usa")

print("Path to dataset files:", path)
