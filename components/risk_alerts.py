"""
components/risk_alerts.py
Patient-friendly risk alerts page.
"""

import streamlit as st


SEVERITY_CONFIG = {
    "Critical": {
        "css_class": "badge-critical",
        "icon": "🚨",
        "action": "Seek emergency medical attention immediately.",
        "border": "rgba(244,63,94,0.4)",
    },
    "High": {
        "css_class": "badge-high",
        "icon": "🔴",
        "action": "Schedule an urgent appointment with your doctor within 48 hours.",
        "border": "rgba(249,115,22,0.4)",
    },
    "Medium": {
        "css_class": "badge-medium",
        "icon": "🟡",
        "action": "Discuss this with your doctor at your next routine visit.",
        "border": "rgba(234,179,8,0.35)",
    },
    "Low": {
        "css_class": "badge-low",
        "icon": "🟢",
        "action": "Keep monitoring — no immediate action required.",
        "border": "rgba(34,197,94,0.35)",
    },
}

SPECIALIST_ICONS = {
    "Cardiologist":  "❤️",
    "Psychologist":  "🧠",
    "Pulmonologist": "💨",
    "Neurologist":   "⚡",
}


def render_risk_alerts():
    """Render the Risk Alerts page."""
    st.markdown('<div class="page-title">⚠️ My Risk Alerts</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Flagged findings from your AI specialist panel, explained in plain English.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    if not st.session_state.get("consensus_diagnosis"):
        st.info("📤 No analysis yet. Go to **Upload Report** first.")
        return

    alerts = st.session_state.get("risk_alerts", [])

    if not alerts:
        st.markdown("""
        <div class="glass-card" style="text-align:center;padding:2rem;">
            <div style="font-size:3rem;">✅</div>
            <div style="font-weight:700;font-size:1.2rem;color:#4ade80;margin:.4rem 0;">No Significant Alerts</div>
            <div style="color:#94a3b8;">Your AI panel did not flag any major risk indicators. Keep up the good work!</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Summary bar
    counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    for a in alerts:
        counts[a["severity"]] = counts.get(a["severity"], 0) + 1

    c1, c2, c3, c4 = st.columns(4)
    for col, (sev, cnt) in zip([c1, c2, c3, c4], counts.items()):
        cfg = SEVERITY_CONFIG[sev]
        col.markdown(
            f'<div class="{cfg["css_class"]}" style="justify-content:center;text-align:center;">'
            f'{cfg["icon"]} {cnt} {sev}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Sort: Critical → High → Medium → Low
    order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    sorted_alerts = sorted(alerts, key=lambda x: order.get(x["severity"], 9))

    for alert in sorted_alerts:
        cfg = SEVERITY_CONFIG.get(alert["severity"], SEVERITY_CONFIG["Medium"])
        spec_icon = SPECIALIST_ICONS.get(alert["specialist"], "🔬")

        st.markdown(
            f"""
            <div style="background:rgba(255,255,255,0.03);border:1px solid {cfg['border']};
            border-left:4px solid {cfg['border']};border-radius:16px;padding:1.25rem 1.5rem;
            margin-bottom:1rem;">
              <div style="display:flex;align-items:center;gap:.5rem;margin-bottom:.5rem;">
                <span style="font-size:1.2rem;">{cfg['icon']}</span>
                <span style="font-weight:700;font-size:1rem;color:#f1f5f9;">{alert['severity']} Risk</span>
                <span style="margin-left:auto;font-size:.8rem;color:#64748b;">
                  {spec_icon} {alert['specialist']}
                </span>
              </div>
              <div style="color:#cbd5e1;font-size:.92rem;line-height:1.6;margin-bottom:.6rem;">
                {alert['message']}
              </div>
              <div style="font-size:.82rem;color:#94a3b8;">
                <strong style="color:#e2e8f0;">What to do:</strong> {cfg['action']}
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.caption("⚠️ These alerts are AI-generated and are not a substitute for professional medical advice. Always consult a qualified healthcare provider.")
