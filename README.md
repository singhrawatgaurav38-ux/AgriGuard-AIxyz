# 🌾 AgriGuard AI: Climate-Smart Advisory System


AgriGuard AI is an end-to-end agricultural intelligence platform engineered to provide smallholder farmers, extension officers, and agricultural researchers in India with data-driven, climate-adaptive farming recommendations. The system integrates ensemble LLMs, heuristic soil analysis engines, real-time meteorological APIs, and multi-language support.
---

## 🛠️🚀 Key Features

Hybrid AI Ensemble: Synthesizes insights from fine-tuned T5-PEFT (Agriculture Expert), Climate-LoRA (Drought & Risk Specialist), Ollama (Gemma 3 local inference), and Groq Factual Synthesis.

Heuristic Scoring & Soil Analysis: Evaluates NPK nutrient levels, soil pH, and environmental parameters to generate crop suitability and risk scores.

Weather & Climate Intelligence: Integrates OpenMeteo and NASA POWER APIs for 7-day weather forecasts, temperature trend analysis, and historical precipitation patterns.

Multilingual & Voice Support: Generates advisories in 6 languages (Hindi, Tamil, Telugu, Marathi, Punjabi, English) with under-1-minute audio summarization.

Audit Trail & Export Module: Logs historical query data with interactive filtering and one-click JSON/CSV dataset exporting.
---

## 🔮Repository Structure

AgriGuard-AI/
├── src/
│   ├── pipeline/
│   │   ├── e2e_workflow.py       # Master pipeline validator & integration test
│   │   └── scoring_engine.py     # Heuristic scoring & soil NPK analysis
│   ├── ui/
│   │   ├── history.py            # Audit trail & CSV/JSON export module
│   │   └── conclusion.py         # System summary & roadmap UI view
│   └── utils/
│       └── weather_api.py        # OpenMeteo & NASA POWER integration
├── tests/                        # Pytest suite for core pipeline modules
├── app.py                        # Streamlit main entry point
├── Dockerfile                    # Containerization configuration
├── docker-compose.yml            # Multi-service deployment setup
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation

## 💻 Tech Stack

- CategoryComponent / TechnologiesAI & Ensemble ModelsT5-PEFT (Agriculture Expert), Climate-LoRA (Drought Specialist), Ollama (Gemma 3 local LLM), Groq Factual SynthesisFrontend & UIStreamlit dashboard, Plotly (interactive charts, radar profiles, trend visualizations)Backend & Data ProcessingPython 3.10+, Pandas, Heuristic Soil NPK & pH Scoring EngineData & RAG PipelineDomain-specific RAG retrieval engine, 10-year historical agricultural databaseExternal APIsOpenMeteo API (7-day weather forecast), NASA POWER API (historical climate data)Audio & MultilingualMultilingual Translation Engine (Hindi, Tamil, Telugu, Marathi, Punjabi, English), Audio Summarization engine (<1 min)DevOps & TestingDocker, Docker Compose, Pytest

---

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   # Clone the repository
git clone https://github.com/singhrawatgaurav38-ux/AgriGuard-AIxyz

# Navigate into the project directory
cd AgriGuard-AIxyz

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

   ```
# Create module files
touch src/pipeline/__init__.py src/pipeline/e2e_workflow.py src/pipeline/scoring_engine.py
touch src/ui/__init__.py src/ui/history.py src/ui/conclusion.py
touch src/utils/__init__.py src/utils/weather_api.py
   ```
# Install project dependencies
pip install -r requirements.txt


   ```

4. **Initialize Database & Run Application**:
   ```bash
python src/db/database.py
streamlit run app.py
   ```
# Launch the application
streamlit run app.py
