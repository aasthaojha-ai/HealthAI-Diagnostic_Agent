# AI Health Diagnostic Agent

A state-of-the-art patient health intelligence dashboard powered by a multi-agent AI system. 

This application allows patients to upload their medical reports (e.g., lab results, clinical notes) and receive a comprehensive, plain-English health analysis. The analysis is performed by a simulated panel of expert AI specialists (Cardiologist, Neurologist, Pulmonologist, Psychologist) and aggregated into actionable insights.

## Features

- **Patient-Centric Dashboard**: A clean, premium UI built with Streamlit, featuring custom CSS, glassmorphism, and responsive grids.
- **Multi-Agent Analysis**: Uses LangChain and OpenAI to run parallel expert assessments.
- **Health Snapshot**: Get an instant overview of your overall health score, active risk alerts, and specialist recommendations.
- **Personalized Lifestyle Plan**: Tailored diet, exercise, and wellness advice based on your diagnostic results.
- **Risk Alerts System**: Severity-based alerts (Critical, High, Medium, Low) to help you prioritize your health concerns.
- **Export Options**: Download your complete report as a TXT or JSON file.

## Project Structure

```
.
├── agents.py                 # Core AI logic (Specialist agents, Aggregator, Lifestyle Advisor)
├── streamlit_app.py          # Main Streamlit application entry point (v2.0 modular router)
├── components/               # UI components module
│   ├── __init__.py
│   ├── health_summary.py     # "My Health Summary" view
│   ├── home.py               # Main dashboard "Health Snapshot"
│   ├── lifestyle.py          # "Your Lifestyle Plan" grid view
│   ├── report_download.py    # Export functionality
│   ├── risk_alerts.py        # Severity-based alerts
│   ├── sidebar.py            # App navigation
│   ├── styles.py             # Custom CSS injected into the app
│   ├── test_insights.py      # Detailed specialist findings
│   └── upload.py             # Report upload and analysis triggering UI
├── requirements.txt          # Python dependencies
└── .gitignore                # Git ignore rules
```

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aasthaojha-ai/HealthAI-Diagnostic_Agent
   cd HealthAI-Diagnostic_Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment Variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

## Disclaimer

This project is intended for informational and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
