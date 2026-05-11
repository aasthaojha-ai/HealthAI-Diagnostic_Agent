"""
components/health_summary.py
Personal health summary page — plain-English overview of the consensus diagnosis.
"""

import streamlit as st
import plotly.graph_objects as go


def _risk_donut(score: int) -> go.Figure:
    remaining = 100 - score
    color = "#4ade80" if score >= 70 else "#facc15" if score >= 45 else "#fb7185"
    fig = go.Figure(data=[go.Pie(
        values=[score, remaining],
        hole=0.72,
        marker=dict(colors=[color, "rgba(255,255,255,0.04)"]),
        textinfo="none",
        showlegend=False,
    )])
    fig.add_annotation(
        text=f"<b>{score}</b>",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=34, color=color, family="Inter"),
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=10),
        height=180,
    )
    return fig


def _score_label(score: int) -> tuple:
    if score >= 70:
        return "Good", "#4ade80", "Your health indicators are generally positive."
    elif score >= 45:
        return "Fair", "#facc15", "Some areas need attention — see Risk Alerts."
    else:
        return "Needs Attention", "#fb7185", "Several issues detected — please consult a doctor soon."


def render_health_summary():
    """Render the My Health Summary page."""
    st.markdown('<div class="page-title">💊 My Health Summary</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">A plain-English overview of what your AI panel found.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    consensus = st.session_state.get("consensus_diagnosis")
    if not consensus:
        st.info("📤 No analysis yet. Go to **Upload Report** to analyse your medical report.")
        return

    score = st.session_state.get("health_score", 72)
    label, color, desc = _score_label(score)

    # Top row: score + summary card
    col_score, col_summary = st.columns([1, 2.5])

    with col_score:
        st.markdown('<div class="glass-card" style="text-align:center;">', unsafe_allow_html=True)
        st.plotly_chart(_risk_donut(score), use_container_width=True, config={"displayModeBar": False})
        st.markdown(
            f'<div style="font-weight:700;font-size:1.1rem;color:{color};">{label}</div>'
            f'<div style="color:#94a3b8;font-size:.82rem;margin-top:.2rem;">{desc}</div>',
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col_summary:
        st.markdown("#### 🔍 What Your AI Panel Found")
        st.markdown(
            '<div style="color:#94a3b8;font-size:.85rem;margin-bottom:.75rem;">'
            'This is the combined view from all 4 specialists in plain English.</div>',
            unsafe_allow_html=True,
        )
        with st.container(border=True):
            st.markdown(consensus)

    # Specialist mini-cards
    st.markdown("---")
    st.markdown("#### 👨‍⚕️ Specialist Highlights")

    results = st.session_state.get("agent_results", {})
    spec_icons = {
        "Cardiologist":  ("❤️", "Heart & Cardiovascular"),
        "Psychologist":  ("🧠", "Mental Health"),
        "Pulmonologist": ("💨", "Lungs & Breathing"),
        "Neurologist":   ("⚡", "Brain & Nervous System"),
    }

    cols = st.columns(2)
    for idx, (spec, report) in enumerate(results.items()):
        icon, friendly_name = spec_icons.get(spec, ("🔬", spec))
        # Show first 3 non-empty lines as a teaser
        lines = [l.strip("- •*#").strip() for l in report.split("\n") if l.strip() and not l.startswith("#")]
        teaser = " ".join(lines[:3])[:280] + "…"
        with cols[idx % 2]:
            st.markdown(
                f"""<div class="glass-card">
                    <div style="font-size:1.5rem;margin-bottom:.3rem;">{icon}</div>
                    <div style="font-weight:700;color:#e2e8f0;margin-bottom:.3rem;">{friendly_name}</div>
                    <div style="color:#94a3b8;font-size:.85rem;line-height:1.55;">{teaser}</div>
                </div>""",
                unsafe_allow_html=True,
            )
