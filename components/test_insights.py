"""
components/test_insights.py
Test Insights page — per-specialist findings in an accessible tabbed layout.
"""

import streamlit as st


SPECIALIST_META = {
    "Cardiologist": {
        "icon": "❤️",
        "friendly": "Heart & Cardiovascular",
        "desc": "Findings about your heart, blood vessels, and circulatory system.",
        "color": "#fb7185",
    },
    "Psychologist": {
        "icon": "🧠",
        "friendly": "Mental Health",
        "desc": "Insights about your emotional wellbeing and mental health.",
        "color": "#a78bfa",
    },
    "Pulmonologist": {
        "icon": "💨",
        "friendly": "Lungs & Breathing",
        "desc": "Findings related to your respiratory system and lung health.",
        "color": "#38bdf8",
    },
    "Neurologist": {
        "icon": "⚡",
        "friendly": "Brain & Nervous System",
        "desc": "Insights about your brain, spinal cord, and nervous system.",
        "color": "#fbbf24",
    },
}


def render_test_insights():
    """Render the Test Insights page."""
    st.markdown('<div class="page-title">🧪 Test Insights</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Detailed findings from each of your AI specialist consultants.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    results = st.session_state.get("agent_results")
    if not results:
        st.info("📤 No analysis yet. Go to **Upload Report** first.")
        return

    tab_labels = [
        f"{SPECIALIST_META[s]['icon']} {SPECIALIST_META[s]['friendly']}"
        for s in results
        if s in SPECIALIST_META
    ]
    tabs = st.tabs(tab_labels)

    for tab, (spec, report) in zip(tabs, results.items()):
        meta = SPECIALIST_META.get(spec, {"icon": "🔬", "friendly": spec, "desc": "", "color": "#667eea"})
        with tab:
            st.markdown(
                f'<div style="color:{meta["color"]};font-size:.85rem;margin-bottom:1rem;">'
                f'{meta["icon"]} {meta["desc"]}</div>',
                unsafe_allow_html=True,
            )
            # Use a container for the report content with glass-card styling
            with st.container(border=True):
                st.markdown(report)

    # Consensus at bottom
    st.markdown("---")
    st.markdown("#### 🎯 Final Consensus from Your Full Panel")
    consensus = st.session_state.get("consensus_diagnosis", "")
    with st.container(border=True):
        st.markdown(consensus)
