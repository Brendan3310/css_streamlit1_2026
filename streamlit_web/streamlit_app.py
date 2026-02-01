import streamlit as st
import sys
import os

# Set page config (MUST be first Streamlit command)
st.set_page_config(
    page_title="My Portfolio App",
    page_icon="🚀",
    layout="wide"
)

# Add the views directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "views"))

# Import the view modules as functions
try:
    from about_me import main as about_me_main
    from sales_dashboard import main as sales_dashboard_main
    from chatbot import main as chatbot_main
    from css_streamlit1_2026 import main as css_app_main
except ImportError as e:
    st.error(f"Failed to import modules: {e}")
    st.stop()

# --- PAGE SETUP ---
about_page = st.Page(
    about_me_main,
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    sales_dashboard_main,
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    chatbot_main,
    title="Chat Bot",
    icon=":material/smart_toy:",
)
project_3_page = st.Page(
    css_app_main,
    title="CSS App",
    icon=":material/code:",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_3_page],
    }
)

# --- SHARED ON ALL PAGES ---
# Fix the logo path
logo_path = os.path.join(os.path.dirname(__file__), "assets", "codingisfun_logo.png")
if os.path.exists(logo_path):
    st.logo(logo_path)
else:
    # Try alternative path
    alt_logo_path = "assets/codingisfun_logo.png"
    if os.path.exists(alt_logo_path):
        st.logo(alt_logo_path)

# --- RUN NAVIGATION ---
pg.run()
