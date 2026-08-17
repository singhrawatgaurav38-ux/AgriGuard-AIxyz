# 🔄 AgriGuard AI - Data Flow Diagram (DFD) Specification

This document details the multi-level Data Flow Diagrams (DFDs) for the **AgriGuard AI Climate-Smart Advisory System**, illustrating how farmer inputs, weather API streams, soil metrics, ensemble AI reasoning, and audit logs flow through the architecture.

---

## 📌 1. DFD Level 0: Context Diagram

The Level 0 Context Diagram represents the high-level boundary of the AgriGuard AI system and its interactions with external entities.

```mermaid
graph TD
    Farmer[👨‍🌾 Farmer / Extension Worker] -->|State, District, NPK, pH, Crop| System((AgriGuard AI System))
    System -->|Multilingual Advisory, Audio, Yield Risk| Farmer

    WeatherAPI[🌤️ OpenMeteo / NASA POWER APIs] -->|7-Day Weather Forecast & Historical Data| System
    System -->|API Requests (Lat/Lon Coordinates)| WeatherAPI

    AIEnsemble[🤖 Ensemble AI Models (Groq / Ollama / T5-PEFT)] -->|Factual Synthesis & Contextual Logic| System
    System -->|Prompt Context & Soil-Climate Inputs| AIEnsemble

    Storage[(💾 Session Audit Log & Export)] <-->|Save Query History & Download CSV/JSON| System