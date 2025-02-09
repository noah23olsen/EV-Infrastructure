import streamlit as st

st.set_page_config(layout="wide")

# Read the HTML file
with open("map.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML file in Streamlit
st.components.v1.html(html_content, width=1600, height=900, scrolling=False)
