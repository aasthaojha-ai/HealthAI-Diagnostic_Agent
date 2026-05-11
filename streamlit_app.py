"""
AI Health Diagnostic Agent - Streamlit Application (v2.0)
========================================================
Main entry point for the modularised dashboard.
"""

import streamlit as st
import os
from dotenv import load_dotenv

# 1. Custom Components
from components.styles import inject_css
from components.sidebar import render_sidebar
from components.home import render_home
from components.upload import render_upload
from components.health_summary import render_health_summary
from components.risk_alerts import render_risk_alerts
from components.test_insights import render_test_insights
from components.lifestyle import render_lifestyle
from components.report_download import render_report_download

# Load environment variables
load_dotenv()
if "OPENAI_API_KEY_OK" not in st.session_state:
    st.session_state.OPENAI_API_KEY_OK = bool(os.getenv("OPENAI_API_KEY"))

# 2. Page Configuration
st.set_page_config(
    page_title="HealthAI | Personal Health Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 3. Session State Initialisation
if "agent_results" not in st.session_state:
    st.session_state.agent_results = None
if "consensus_diagnosis" not in st.session_state:
    st.session_state.consensus_diagnosis = None
if "lifestyle_plan" not in st.session_state:
    st.session_state.lifestyle_plan = None
if "health_score" not in st.session_state:
    st.session_state.health_score = 72
if "risk_alerts" not in st.session_state:
    st.session_state.risk_alerts = []
if "processing" not in st.session_state:
    st.session_state.processing = False
if "report_text_raw" not in st.session_state:
    st.session_state.report_text_raw = ""

# 4. Inject Custom Styles
inject_css()

# 5. Render Sidebar & Get Selection
page_selection = render_sidebar()

# 6. Main Content Area Routing
if page_selection == "Home":
    render_home()

elif page_selection == "Upload Report":
    render_upload()

elif page_selection == "My Health Summary":
    render_health_summary()

elif page_selection == "Risk Alerts":
    render_risk_alerts()

elif page_selection == "Test Insights":
    render_test_insights()

elif page_selection == "Lifestyle Plan":
    render_lifestyle()

elif page_selection == "Download Report":
    render_report_download()