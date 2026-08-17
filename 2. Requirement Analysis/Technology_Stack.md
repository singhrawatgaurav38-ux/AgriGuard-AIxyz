# 🛠️ Technology Stack & Project Planning Specification

This document details the hardware/software requirements, technology stack selection criteria, architecture rationale, and development milestones for **AgriGuard AI**.

---

## 1. Technology Stack Overview

| Category / Layer | Technology Selected | Version / Spec | Rationale & Functional Purpose |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | Streamlit | `>=1.30.0` | Enables rapid deployment of an interactive, responsive agricultural dashboard with built-in state management and layout controls. |
| **Programming Language** | Python | `3.10+` | Core language chosen for its robust ecosystem in data processing, ML pipeline orchestration, and API integration. |
| **Fine-Tuned Domain Model** | T5-PEFT (LoRA) | HuggingFace Transformers | Parameter-Efficient Fine-Tuning for specialized agricultural advice, crop suitability scoring, and NPK soil evaluation. |
| **Local LLM Engine** | Ollama (Gemma 3) | Local Edge Service | Offline-capable local LLM inference engine ensuring fallback operational readiness in internet-constrained rural areas. |
| **Cloud Synthesis Engine** | Groq Cloud API | Llama-3 / Custom Models | Ultra-low latency cloud inference engine used to merge and synthesize outputs from multiple ensemble AI models. |
| **Weather APIs** | OpenMeteo & NASA POWER | REST JSON Endpoints | Real-time 7-day meteorological forecasts and historical 10-year climate dataset retrieval without strict rate limits or mandatory API keys. |
| **Data Analytics & Charts** | Plotly Express | `>=5.18.0` | Generates interactive dual-axis charts (Rainfall vs. Yield), temperature anomaly graphs, and NDVI health trajectory plots. |
| **Data Engineering** | Pandas & NumPy | `>=2.0.0` | In-memory data processing, historical dataset querying, heuristic scoring calculations, and CSV/JSON export rendering. |
| **Containerization** | Docker & Docker Compose | Engine `24.0+` | Microservices containerization ensuring consistent deployment across local development, edge devices, and cloud servers. |

---

## 2. Architectural Rationale

* **Hybrid AI Synthesis:** Combines deterministic heuristic scoring (for NPK and pH limits) with generative AI (for qualitative farming advice) to eliminate hallucinations and maintain scientific accuracy.
* **Edge-Cloud Fallback:** Integrates local Ollama models alongside cloud-based Groq synthesis, allowing partial system functionality even when internet connectivity is spotty.
* **Multilingual & Voice-First Design:** Features built-in translation layers supporting Hindi, Tamil, Telugu, Marathi, Punjabi, and English with under-1-minute audio summaries.

---

## 3. Development Milestones

1. **Milestone 1: Environment Setup & Infrastructure** — Repository structuring, dependency pinning, and API configuration.
2. **Milestone 2: Data & Weather Pipeline** — OpenMeteo API integration and 10-year historical climate dataset aggregation.
3. **Milestone 3: Hybrid AI Ensemble Development** — Model orchestration combining T5-PEFT, Climate-LoRA, Ollama, and Groq synthesis.
4. **Milestone 4: UI Development & Audit Engine** — Streamlit dynamic input selectors, Plotly chart integration, and CSV/JSON export module.
5. **Milestone 5: Testing & Production Deployment** — E2E workflow validation, pytest suite creation, Docker containerization, and final repository documentation.