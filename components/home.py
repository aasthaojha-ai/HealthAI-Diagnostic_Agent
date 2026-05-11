"""
components/home.py
Welcome / Home page for the patient dashboard.
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime


def _health_gauge(score: int) -> go.Figure:
    color = "#4ade80" if score >= 70 else "#facc15" if score >= 45 else "#fb7185"
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={"font": {"size": 42, "color": color, "family": "Inter"}, "suffix": ""},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#475569", "tickfont": {"color": "#475569"}},
            "bar": {"color": color, "thickness": 0.25},
            "bgcolor": "rgba(0,0,0,0)",
            "bordercolor": "rgba(0,0,0,0)",
            "steps": [
                {"range": [0, 45],  "color": "rgba(244,63,94,0.12)"},
                {"range": [45, 70], "color": "rgba(234,179,8,0.1)"},
                {"range": [70, 100],"color": "rgba(34,197,94,0.1)"},
            ],
            "threshold": {"line": {"color": color, "width": 3}, "value": score},
        },
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=30, b=10),
        height=220,
        font={"family": "Inter"},
    )
    return fig


def render_home():
    """Render the Home / Welcome page."""
    analyzed = bool(st.session_state.get("consensus_diagnosis"))

    # Hero banner
    st.markdown("""
    <div class="hero-container">
        <div class="hero-emoji">🩺</div>
        <div class="hero-title">Your Personal Health Intelligence</div>
        <div class="hero-desc">
            Upload your medical report and let our AI panel of specialists analyse it —
            giving you clear, plain-English insights into your health.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not analyzed:
        # CTA cards
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            <div class="glass-card" style="text-align:center;">
                <div style="font-size:2rem;">📤</div>
                <div style="font-weight:700;color:#f1f5f9;margin:.4rem 0 .2rem;">Upload Report</div>
                <div style="color:#94a3b8;font-size:.85rem;">
                    Upload your medical report in TXT format to get started.
                </div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="glass-card" style="text-align:center;">
                <div style="font-size:2rem;">🤖</div>
                <div style="font-weight:700;color:#f1f5f9;margin:.4rem 0 .2rem;">AI Analysis</div>
                <div style="color:#94a3b8;font-size:.85rem;">
                    4 specialist AIs review your report simultaneously in seconds.
                </div>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class="glass-card" style="text-align:center;">
                <div style="font-size:2rem;">💡</div>
                <div style="font-weight:700;color:#f1f5f9;margin:.4rem 0 .2rem;">Get Insights</div>
                <div style="color:#94a3b8;font-size:.85rem;">
                    Receive plain-English health insights, risk alerts &amp; lifestyle tips.
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.info("👆 Use **📤 Upload Report** in the sidebar to analyse your medical report.")

    else:
        # Post-analysis overview
        score = st.session_state.get("health_score", 72)
        label, color, _ = _score_label(score)
        n_alerts = len(st.session_state.get("risk_alerts", []))
        n_specialists = len(st.session_state.get("agent_results", {}))

        # 1. Health Snapshot Grid
        st.markdown(f"""
        <div class="stat-container">
            <div class="stat-card">
                <div class="stat-label">Overall Health</div>
                <div class="stat-value" style="color:{color};">{score}%</div>
                <div style="font-size:0.7rem;color:#64748b;margin-top:0.2rem;">Condition: {label}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Active Risks</div>
                <div class="stat-value" style="color:{'#fb7185' if n_alerts > 0 else '#4ade80'};">{n_alerts}</div>
                <div style="font-size:0.7rem;color:#64748b;margin-top:0.2rem;">Red Flags Detected</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Specialist Insights</div>
                <div class="stat-value" style="color:#a78bfa;">{n_specialists}</div>
                <div style="font-size:0.7rem;color:#64748b;margin-top:0.2rem;">Agents Consulted</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Report Date</div>
                <div class="stat-value" style="font-size:1.1rem;padding-top:0.4rem;">{datetime.now().strftime('%d %b %y')}</div>
                <div style="font-size:0.7rem;color:#64748b;margin-top:0.4rem;">Latest Analysis</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col_gauge, col_stats = st.columns([1, 1.8])

        with col_gauge:
            st.markdown('<div class="glass-card" style="text-align:center;padding:1rem;">', unsafe_allow_html=True)
            st.plotly_chart(_health_gauge(score), use_container_width=True, config={"displayModeBar": False})
            st.markdown('<div class="score-label-sub">Health Vitality Score</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col_stats:
            st.markdown(f"""
            <div class="glass-card">
                <h4 style="margin-top:0;">📋 Quick Summary</h4>
                <div style="font-size:.92rem;color:#cbd5e1;line-height:1.6;margin-bottom:1rem;">
                  Your medical report has been successfully processed by our AI panel. 
                  We've identified <strong>{n_alerts}</strong> key risk areas and generated 
                  a tailored lifestyle plan to help you improve your vitality.
                </div>
                <div style="display:flex;gap:0.75rem;">
                   <div style="background:rgba(102,126,234,0.1);padding:0.5rem 1rem;border-radius:10px;border:1px solid rgba(102,126,234,0.2);flex:1;text-align:center;">
                      <div style="font-size:0.75rem;color:#94a3b8;">Recommendations</div>
                      <div style="font-weight:700;color:#e2e8f0;">Ready</div>
                   </div>
                   <div style="background:rgba(102,126,234,0.1);padding:0.5rem 1rem;border-radius:10px;border:1px solid rgba(102,126,234,0.2);flex:1;text-align:center;">
                      <div style="font-size:0.75rem;color:#94a3b8;">Full Report</div>
                      <div style="font-weight:700;color:#e2e8f0;">Available</div>
                   </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Quick Actions
        st.markdown("#### ⚡ Quick Actions")
        qa1, qa2, qa3 = st.columns(3)
        with qa1:
            if st.button("👁️ View Risk Alerts", use_container_width=True):
                st.session_state.nav_radio = "⚠️  Risk Alerts"
                st.rerun()
        with qa2:
            if st.button("🥗 See Lifestyle Plan", use_container_width=True):
                st.session_state.nav_radio = "🥗  Lifestyle Plan"
                st.rerun()
        with qa3:
            if st.button("📥 Download Report", use_container_width=True):
                st.session_state.nav_radio = "📄  Download Report"
                st.rerun()


def _score_label(score: int) -> tuple:
    if score >= 70:
        return "Good", "#4ade80", "positive"
    elif score >= 45:
        return "Fair", "#facc15", "concerning"
    else:
        return "Critical", "#fb7185", "urgent"
