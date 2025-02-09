import streamlit as st

# Set Streamlit to wide layout
st.set_page_config(layout="wide")

# Read the HTML file
with open("map.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Inject custom CSS to remove padding, header, and menu
st.markdown(
    """
    <style>
        /* Hide Streamlit header, footer, and menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Remove Streamlit default padding */
        .stApp {
            padding: 0;
            margin: 0;
            height: 100vh;
            width: 100vw;
        }

        /* Force full-screen iframe */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the full-screen map
st.components.v1.html(html_content, width=None, height=None, scrolling=False)
