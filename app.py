import streamlit as st
import os

# Set Streamlit page layout to wide mode
st.set_page_config(layout="wide")

# Set the HTML file path
html_file = "map.html"

st.write("### EV Charging Stations & National Parks Map")

# Provide a link to directly open the file
st.markdown(f"[Click here to open the interactive map](./{html_file})", unsafe_allow_html=True)

# Optionally, open the file automatically if running locally
if os.path.exists(html_file):
    os.system(f"open {html_file}")  # Mac
    # os.system(f"start {html_file}")  # Windows
