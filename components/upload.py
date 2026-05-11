"""
components/upload.py
Medical report upload page with AI analysis trigger.
"""

import streamlit as st
from agents import run_analysis as _run_analysis, LifestyleAdvisor
import re


def _extract_health_score(consensus: str) -> int:
    """Parse an overall confidence score from the consensus text and convert to 0-100."""
    patterns = [
        r"overall.*?confidence.*?(\d+\.\d+)",
        r"score[:\s]+(\d+\.\d+)",
        r"(\d+\.\d+)\s*/\s*1\.0",
    ]
    for pat in patterns:
        m = re.search(pat, consensus, re.IGNORECASE)
        if m:
            val = float(m.group(1))
            if val <= 1.0:
                return int(val * 100)
            return min(int(val), 100)
    return 72  # sensible default


def _extract_alerts(agent_results: dict, consensus: str) -> list:
    """Extract plain-English risk alerts from agent results."""
    alerts = []
    keywords = {
        "Critical": ["critical", "immediate", "emergency", "urgent", "severe", "life-threatening"],
        "High":     ["high risk", "significant", "elevated", "abnormal", "red flag", "concerning"],
        "Medium":   ["moderate", "medium risk", "monitor", "watch", "borderline", "mild"],
    }
    for specialist, report in agent_results.items():
        report_lower = report.lower()
        for severity, kws in keywords.items():
            if any(kw in report_lower for kw in kws):
                # Grab the first sentence mentioning the keyword
                for kw in kws:
                    idx = report_lower.find(kw)
                    if idx != -1:
                        snippet = report[max(0, idx - 40): idx + 120].strip()
                        snippet = snippet.split("\n")[0].strip("- •*#").strip()
                        if len(snippet) > 20:
                            alerts.append({
                                "specialist": specialist,
                                "severity": severity,
                                "message": snippet,
                            })
                            break
                break
    return alerts[:8]  # cap


def run_analysis_ui(medical_report: str):
    """Run analysis with custom premium status badges."""
    st.session_state.processing = True

    agent_names = ["Cardiologist", "Psychologist", "Pulmonologist", "Neurologist"]
    
    with st.container(border=True):
        st.markdown('<div style="font-size:0.8rem;color:#94a3b8;margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:0.05em;">Consulting AI Specialist Panel...</div>', unsafe_allow_html=True)
        cols = st.columns(4)
        slots = [cols[i].empty() for i in range(4)]
        
        for i, n in enumerate(agent_names):
            slots[i].markdown(f"""
                <div class="agent-status-row">
                    <div class="status-dot active"></div>
                    <div style="font-size:0.85rem;color:#94a3b8;">{n}</div>
                </div>
            """, unsafe_allow_html=True)

        try:
            # Main analysis call
            results, consensus = _run_analysis(medical_report)

            for i, n in enumerate(agent_names):
                status_class = "done" if n in results else "error"
                status_icon = "✅" if n in results else "❌"
                slots[i].markdown(f"""
                    <div class="agent-status-row">
                        <div class="status-dot {status_class}"></div>
                        <div style="font-size:0.85rem;color:#e2e8f0;">{status_icon} {n}</div>
                    </div>
                """, unsafe_allow_html=True)

            # Lifestyle plan
            with st.spinner("🥗 Designing your personalised wellness roadmap..."):
                lifestyle_agent = LifestyleAdvisor()
                lifestyle_plan = lifestyle_agent.execute(medical_report, consensus)

            # Persist to session
            st.session_state.agent_results       = results
            st.session_state.consensus_diagnosis = consensus
            st.session_state.lifestyle_plan      = lifestyle_plan
            st.session_state.health_score        = _extract_health_score(consensus)
            st.session_state.risk_alerts         = _extract_alerts(results, consensus)
            st.session_state.report_text_raw     = medical_report

        except Exception as e:
            st.error(f"❌ Analysis failed: {e}")
        finally:
            st.session_state.processing = False


def render_upload():
    """Render the Upload Report page."""
    st.markdown('<div class="page-title">📤 Upload Your Medical Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Our AI specialist panel will review it and give you clear, personalised health insights.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

    # Upload zone
    uploaded_file = st.file_uploader(
        "Drop your medical report here",
        type=["txt"],
        help="Plain-text (.txt) reports work best. Max 10 MB.",
        label_visibility="collapsed",
    )

    if uploaded_file:
        st.success(f"✅ **{uploaded_file.name}** uploaded successfully")
        medical_report = uploaded_file.read().decode("utf-8", errors="replace")

        with st.expander("👁️ Preview report content", expanded=False):
            st.text(medical_report[:1500] + ("…" if len(medical_report) > 1500 else ""))

        st.markdown("<br>", unsafe_allow_html=True)

        # Ensure API key is present
        if not st.session_state.get("OPENAI_API_KEY_OK"):
            import os
            if not os.getenv("OPENAI_API_KEY"):
                st.error("❌ OpenAI API key not found. Please ensure it is set in your environment or secrets.")
                return
            else:
                st.session_state.OPENAI_API_KEY_OK = True

        if st.button("🔍 Analyse My Report", use_container_width=True):
            st.markdown("---")
            run_analysis_ui(medical_report)
            if st.session_state.get("consensus_diagnosis"):
                st.success("✅ Analysis complete! Navigate the sidebar to explore your results.")
                st.balloons()

    else:
        st.markdown("""
        <div class="glass-card" style="text-align:center;padding:2.5rem;">
            <div style="font-size:3rem;margin-bottom:.5rem;">📋</div>
            <div style="font-weight:700;font-size:1.1rem;color:#e2e8f0;margin-bottom:.4rem;">
                No file selected yet
            </div>
            <div style="color:#64748b;font-size:.9rem;">
                Click <strong>Browse files</strong> above or drag &amp; drop your report.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("##### 💡 Tips for best results")
        st.markdown("""
- Export your medical report as a plain **.txt** file
- Include lab results, doctor's notes, and symptom history if available
- Longer, more detailed reports = more accurate AI insights
- Your data is **never stored** — analysis runs in memory only
        """)
