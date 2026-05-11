"""
components/sidebar.py
Patient dashboard sidebar with navigation and health score badge.
"""

import streamlit as st


PAGES = [
    ("🏠", "Home"),
    ("📤", "Upload Report"),
    ("💊", "My Health Summary"),
    ("⚠️", "Risk Alerts"),
    ("🧪", "Test Insights"),
    ("🥗", "Lifestyle Plan"),
    ("📄", "Download Report"),
]


def render_sidebar() -> str:
    """Render sidebar and return the selected page name."""
    with st.sidebar:
        st.markdown('<div class="sidebar-logo">✦ HealthAI</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-tagline">Your Personal Health Intelligence</div>', unsafe_allow_html=True)

        # Health score badge (only if analysis done)
        if st.session_state.get("consensus_diagnosis"):
            score = st.session_state.get("health_score", 72)
            color = "#4ade80" if score >= 70 else "#facc15" if score >= 45 else "#fb7185"
            st.markdown(
                f"""
                <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(102,126,234,0.25);
                border-radius:14px;padding:0.9rem 1rem;margin-bottom:1rem;">
                  <div style="font-size:0.72rem;color:#64748b;text-transform:uppercase;letter-spacing:.06em;">
                    Health Score
                  </div>
                  <div style="font-size:2rem;font-weight:800;color:{color};line-height:1.1;">
                    {score}<span style="font-size:1rem;color:#64748b;">/100</span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown(
            '<div style="font-size:0.72rem;color:#475569;text-transform:uppercase;'
            'letter-spacing:.08em;margin-bottom:.5rem;">Navigation</div>',
            unsafe_allow_html=True,
        )

        labels = [f"{icon}  {name}" for icon, name in PAGES]
        selection = st.radio("nav", labels, label_visibility="collapsed", key="nav_radio")

        st.markdown("---")
        st.markdown(
            '<div style="font-size:0.72rem;color:#475569;margin-bottom:.4rem;">Analysis Status</div>',
            unsafe_allow_html=True,
        )
        if st.session_state.get("consensus_diagnosis"):
            st.success("✅ Report analysed")
        elif st.session_state.get("processing"):
            st.info("⏳ Analysing…")
        else:
            st.warning("📤 No report uploaded yet")

        st.markdown(
            '<div class="footer" style="margin-top:2rem;">© 2025 HealthAI · v2.0</div>',
            unsafe_allow_html=True,
        )

    # Return just the page name (strip icon)
    for icon, name in PAGES:
        if f"{icon}  {name}" == selection:
            return name
    return "Home"
