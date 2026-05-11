"""
components/lifestyle.py
Lifestyle Plan page — diet, exercise, and wellness recommendations.
"""

import streamlit as st
import re


CATEGORY_META = {
    "Diet":      {"icon": "🥗", "color": "#4ade80", "border": "rgba(34,197,94,0.25)"},
    "Exercise":  {"icon": "🏃", "color": "#38bdf8", "border": "rgba(56,189,248,0.25)"},
    "Lifestyle": {"icon": "🌿", "color": "#a78bfa", "border": "rgba(167,139,250,0.25)"},
    "Mental":    {"icon": "🧘", "color": "#fbbf24", "border": "rgba(251,191,36,0.25)"},
    "Sleep":     {"icon": "😴", "color": "#818cf8", "border": "rgba(129,140,248,0.25)"},
    "General":   {"icon": "💡", "color": "#94a3b8", "border": "rgba(148,163,184,0.2)"},
}


def _parse_sections(text: str) -> list[dict]:
    """Split the lifestyle plan into labelled sections."""
    sections = []
    current_cat = "General"
    current_lines = []

    category_map = {
        "diet": "Diet", "nutrition": "Diet", "food": "Diet", "eat": "Diet",
        "exercise": "Exercise", "physical": "Exercise", "workout": "Exercise", "activity": "Exercise",
        "lifestyle": "Lifestyle", "habit": "Lifestyle", "routine": "Lifestyle",
        "mental": "Mental", "stress": "Mental", "mindful": "Mental", "wellbeing": "Mental",
        "sleep": "Sleep", "rest": "Sleep",
    }

    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or (stripped.endswith(":") and len(stripped) < 60):
            if current_lines:
                sections.append({"category": current_cat, "lines": current_lines})
                current_lines = []
            heading = stripped.lstrip("#").strip().rstrip(":").lower()
            current_cat = next(
                (v for k, v in category_map.items() if k in heading),
                "General",
            )
        else:
            current_lines.append(stripped.lstrip("- •*").strip())

    if current_lines:
        sections.append({"category": current_cat, "lines": current_lines})

    return sections


def render_lifestyle():
    """Render the Lifestyle Plan page."""
    st.markdown('<div class="page-title">🥗 Your Lifestyle Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Personalised diet, exercise, and wellness recommendations based on your health report.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    plan = st.session_state.get("lifestyle_plan")
    if not plan:
        if not st.session_state.get("consensus_diagnosis"):
            st.info("📤 No analysis yet. Go to **Upload Report** first.")
        else:
            st.warning("🥗 Lifestyle plan not generated. Try re-uploading your report.")
        return

    sections = _parse_sections(plan)

    if not sections:
        st.markdown(plan)
        return

    # Category summary chips
    seen_cats = list(dict.fromkeys(s["category"] for s in sections))
    chip_html = "".join(
        f'<span style="background:rgba(102,126,234,0.12);border:1px solid rgba(102,126,234,0.25);'
        f'border-radius:20px;padding:.2rem .8rem;font-size:.8rem;color:#a78bfa;margin:.2rem;">'
        f'{CATEGORY_META.get(c, CATEGORY_META["General"])["icon"]} {c}</span>'
        for c in seen_cats
    )
    st.markdown(f'<div style="margin-bottom:1.5rem;display:flex;flex-wrap:wrap;gap:.3rem;">{chip_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="lifestyle-grid">', unsafe_allow_html=True)
    # Render each section as a tile
    for sec in sections:
        meta = CATEGORY_META.get(sec["category"], CATEGORY_META["General"])
        bullets = "".join(
            f'<li>{line}</li>'
            for line in sec["lines"] if line
        )
        st.markdown(
            f"""
            <div class="lifestyle-tile" style="border-color:{meta['border']};">
              <h4>{meta['icon']} {sec['category']}</h4>
              <ul>{bullets}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.caption("🌿 These recommendations are AI-generated based on your medical report. Always consult your doctor before making significant changes to your diet or exercise routine.")
