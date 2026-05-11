"""
components/styles.py
All custom CSS for the patient dashboard.
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ── Base ─────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #0a0e1a;
    color: #e2e8f0;
}

[data-testid="stMain"] {
    background-color: #0a0e1a;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f1629 0%, #0a0e1a 100%);
    border-right: 1px solid rgba(102,126,234,0.15);
}

.block-container {
    padding: 1.5rem 2rem 3rem 2rem !important;
    max-width: 1200px;
}

/* ── Typography ───────────────────────────────────────── */
h1, h2, h3, h4 { color: #f1f5f9; font-weight: 700; }

.page-title {
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.25rem;
}

.page-subtitle {
    color: #94a3b8;
    font-size: 1rem;
    font-weight: 400;
    margin-bottom: 1.5rem;
}

/* ── Metric Cards ─────────────────────────────────────── */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(102,126,234,0.2);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s;
}
[data-testid="stMetric"]:hover {
    border-color: rgba(102,126,234,0.5);
}
[data-testid="stMetricValue"] {
    font-size: 2rem !important;
    font-weight: 700 !important;
    color: #f1f5f9 !important;
}
[data-testid="stMetricLabel"] {
    font-size: 0.8rem !important;
    color: #94a3b8 !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
[data-testid="stMetricDelta"] {
    font-size: 0.85rem !important;
}

/* ── Glass Cards ──────────────────────────────────────── */
.glass-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(102,126,234,0.2);
    border-radius: 20px;
    padding: 1.5rem;
    backdrop-filter: blur(12px);
    margin-bottom: 1rem;
    transition: all 0.25s ease;
}
.glass-card:hover {
    border-color: rgba(102,126,234,0.45);
    box-shadow: 0 0 24px rgba(102,126,234,0.12);
}

/* ── Alert Badges ─────────────────────────────────────── */
.badge-critical {
    background: rgba(244,63,94,0.15);
    border: 1px solid rgba(244,63,94,0.4);
    color: #fb7185;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-weight: 600;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
}
.badge-high {
    background: rgba(249,115,22,0.15);
    border: 1px solid rgba(249,115,22,0.4);
    color: #fb923c;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-weight: 600;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
}
.badge-medium {
    background: rgba(234,179,8,0.12);
    border: 1px solid rgba(234,179,8,0.35);
    color: #facc15;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-weight: 600;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
}
.badge-low {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.35);
    color: #4ade80;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-weight: 600;
    font-size: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
}

/* ── Lifestyle Tiles ──────────────────────────────────── */
.lifestyle-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.25rem;
    margin-bottom: 2rem;
}
.lifestyle-tile {
    background: linear-gradient(135deg, rgba(102,126,234,0.08) 0%, rgba(167,139,250,0.05) 100%);
    border: 1px solid rgba(102,126,234,0.2);
    border-radius: 20px;
    padding: 1.5rem;
    transition: transform 0.2s, border-color 0.2s;
}
.lifestyle-tile:hover {
    transform: translateY(-2px);
    border-color: rgba(102,126,234,0.4);
}
.lifestyle-tile h4 {
    font-size: 1.1rem;
    font-weight: 700;
    color: #a78bfa;
    margin: 0 0 1rem 0;
}
.lifestyle-tile ul {
    margin: 0;
    padding-left: 1.1rem;
}
.lifestyle-tile li {
    color: #cbd5e1;
    font-size: 0.92rem;
    line-height: 1.6;
    margin-bottom: 0.6rem;
}

/* ── Divider ──────────────────────────────────────────── */
.custom-divider {
    border: none;
    border-top: 1px solid rgba(102,126,234,0.15);
    margin: 1.5rem 0;
}

/* ── Sidebar ──────────────────────────────────────────── */
.sidebar-logo {
    font-size: 1.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    padding: 0.25rem 0;
}
.sidebar-tagline {
    color: #64748b;
    font-size: 0.78rem;
    margin-bottom: 1.5rem;
}

/* ── Upload Zone ──────────────────────────────────────── */
[data-testid="stFileUploader"] {
    background: rgba(102,126,234,0.06);
    border: 2px dashed rgba(102,126,234,0.35);
    border-radius: 16px;
    padding: 1rem;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(102,126,234,0.7);
}

/* ── Buttons ──────────────────────────────────────────── */
[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6rem 1.5rem;
    transition: opacity 0.2s, transform 0.15s;
    font-family: 'Inter', sans-serif;
}
[data-testid="stButton"] > button:hover {
    opacity: 0.88;
    transform: translateY(-1px);
}

/* ── Tabs ─────────────────────────────────────────────── */
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent;
    color: #94a3b8;
    border-radius: 8px 8px 0 0;
    font-weight: 500;
}
[data-testid="stTabs"] [aria-selected="true"] {
    color: #a78bfa !important;
    border-bottom: 2px solid #a78bfa;
}

/* ── Containers ───────────────────────────────────────── */
[data-testid="stExpander"] {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(102,126,234,0.18);
    border-radius: 12px;
}

/* ── Footer ───────────────────────────────────────────── */
.footer {
    text-align: center;
    color: #475569;
    font-size: 0.78rem;
    padding: 2rem 0 1rem;
    border-top: 1px solid rgba(102,126,234,0.1);
    margin-top: 3rem;
}

/* ── Welcome Hero ─────────────────────────────────────── */
.hero-container {
    background: linear-gradient(135deg, rgba(102,126,234,0.12) 0%, rgba(167,139,250,0.08) 50%, rgba(20,184,166,0.06) 100%);
    border: 1px solid rgba(102,126,234,0.2);
    border-radius: 24px;
    padding: 2.5rem;
    margin-bottom: 2rem;
    text-align: center;
}
.hero-emoji { font-size: 3rem; margin-bottom: 0.5rem; }
.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #a78bfa 60%, #14b8a6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}
.hero-desc { color: #94a3b8; font-size: 1.05rem; max-width: 520px; margin: 0 auto; }

/* ── Stat Cards (Dashboard Style) ─────────────────────── */
.stat-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
    margin-bottom: 2rem;
}
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(102,126,234,0.15);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
    transition: transform 0.2s, border-color 0.2s;
}
.stat-card:hover {
    transform: translateY(-3px);
    border-color: rgba(102,126,234,0.4);
    background: rgba(255,255,255,0.05);
}
.stat-label {
    font-size: 0.72rem;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
}
.stat-value {
    font-size: 1.5rem;
    font-weight: 800;
    color: #f1f5f9;
}

/* ── Progress Indicators ──────────────────────────────── */
.analysis-progress-container {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(102,126,234,0.1);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1rem;
}
.agent-status-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
}
.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
}
.status-dot.pending { background: #64748b; animation: pulse 1.5s infinite; }
.status-dot.active { background: #667eea; animation: pulse 1s infinite; }
.status-dot.done { background: #4ade80; }
.status-dot.error { background: #fb7185; }

/* ── Animations ───────────────────────────────────────── */
@keyframes pulse {
    0% { opacity: 0.4; transform: scale(0.9); }
    50% { opacity: 1; transform: scale(1.1); }
    100% { opacity: 0.4; transform: scale(0.9); }
}

@keyframes slideInUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-in {
    animation: slideInUp 0.4s ease-out forwards;
}

/* ── Score Ring ───────────────────────────────────────── */
.score-label-sub {
    text-align: center;
    font-size: 0.85rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: -0.5rem;
}
</style>
"""


def inject_css():
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
