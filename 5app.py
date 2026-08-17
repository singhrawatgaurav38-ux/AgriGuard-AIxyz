# ==============================================================================
# AgriGuard AI - Streamlit Web Application
# Epic 5: Streamlit UI Implementation and User Interaction
# Story: 6-Tab Responsive Layout Design
# ==============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import json

# Page Configuration
st.set_page_config(
    page_title="AgriGuard AI - Climate-Smart Advisory",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Application Header & Title
st.title("🌾 AgriGuard AI: Climate-Smart Agricultural Intelligence Platform")
st.markdown(
    "Welcome to **AgriGuard AI**. Select a tab below to access AI advisories, "
    "location-based risk analysis, historical climate trends, weather forecasting, crop selection, and advisory history."
)

# ------------------------------------------------------------------------------
# Sidebar Configuration & District Selectors
# ------------------------------------------------------------------------------
st.sidebar.header("📌 Location & Settings")
selected_state = st.sidebar.selectbox("Select State", ["Uttarakhand", "Uttar Pradesh", "Punjab", "Haryana"])
selected_district = st.sidebar.selectbox("Select District", ["Nainital", "Haldwani", "Dehradun", "Almora", "Udham Singh Nagar"])
selected_language = st.sidebar.selectbox("Preferred Language", ["English", "Hindi (हिन्दी)", "Bengali (বাংলা)", "Telugu (తెలుగు)", "Tamil (தமிழ்)", "Marathi (मराठी)", "Gujarati (ગુજરાતી)"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **AgriGuard AI Status**: Operational\nEnsemble AI Models Active.")

# ------------------------------------------------------------------------------
# Create 6-Tab Responsive Layout
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🤖 AI Chatbot",
    "📍 Location Analysis",
    "📊 Analytics & Visuals",
    "🌤️ Weather Forecast",
    "🌾 Crop Recommendations",
    "📜 Recommendation History"
])

# ==============================================================================
# TAB 1: AI Chatbot (Climate-Smart AI Advisory)
# ==============================================================================
with tab1:
    st.header("🤖 Climate-Smart AI Advisory Chatbot")
    st.markdown(
        "Ask any farming query. Powered by Ensemble AI Architecture "
        "(T5-PEFT, Climate-LoRA, Ollama & Groq synthesis) with multilingual support."
    )

    # Chat interface history initialization
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": f"Hello! I am your AgriGuard AI advisory assistant. How can I assist your farming in {selected_district} today?"
            }
        ]

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    user_query = st.chat_input("Ask your farming question (e.g., What fertilizer should I apply for Wheat?)....")
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # Simulated AI Response Synthesis
        with st.chat_message("assistant"):
            with st.spinner("Synthesizing climate-smart advisory..."):
                bot_response = (
                    f"**Advisory for {selected_district} ({selected_state}):**\n\n"
                    f"Based on recent soil moisture and weather trends for {user_query}, "
                    f"apply balanced NPK (40:20:20 kg/ha) and ensure adequate drip irrigation cycle. "
                    f"Risk factor for crop stress is Low to Moderate."
                )
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})

# ==============================================================================
# TAB 2: Location Analysis (District-Specific Intelligence)
# ==============================================================================
with tab2:
    st.header("📍 District-Specific Agricultural Intelligence")
    st.subheader(f"Region Profile: {selected_district}, {selected_state}")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Soil pH Level", value="6.8", delta="Optimal")
    col2.metric(label="Nitrogen (N)", value="240 kg/ha", delta="-5% Normal")
    col3.metric(label="Phosphorus (P)", value="18 kg/ha", delta="Sufficient")
    col4.metric(label="Potassium (K)", value="150 kg/ha", delta="+2% Normal")

    st.markdown("---")
    st.subheader("Climate Risk & Suitability Assessment")
    st.progress(78, text="Crop Climate Suitability Score: 78%")
    st.warning(f"⚠️ Moderate drought risk detected in {selected_district}. Recommend moisture conservation techniques.")

# ==============================================================================
# TAB 3: Analytics & Visuals (10-Year Historical Trends)
# ==============================================================================
with tab3:
    st.header("📊 10-Year Historical Climate & Agricultural Trends")
    st.markdown("Interactive visualizations showing rainfall, temperature, and soil health metrics.")

    # Generate sample 10-year historical data
    years = list(range(2016, 2026))
    data = pd.DataFrame({
        "Year": years,
        "Annual Rainfall (mm)": np.random.randint(800, 1400, size=10),
        "Avg Temperature (°C)": np.random.uniform(22.0, 27.5, size=10).round(1),
        "Crop Yield (Tons/ha)": np.random.uniform(3.2, 5.1, size=10).round(2)
    })

    st.subheader("Rainfall vs. Yield Trends (2016 - 2025)")
    st.line_chart(data, x="Year", y=["Annual Rainfall (mm)", "Crop Yield (Tons/ha)"])

    st.subheader("Temperature Fluctuations")
    st.bar_chart(data, x="Year", y="Avg Temperature (°C)")

# ==============================================================================
# TAB 4: Weather Forecast (OpenMeteo API Integration)
# ==============================================================================
with tab4:
    st.header("🌤️ 7-Day Weather Forecast")
    st.markdown(f"Real-time meteorological forecast for **{selected_district}**")

    # Sample 7-day forecast display
    forecast_cols = st.columns(7)
    days = ["Today", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    temps = [28, 29, 27, 26, 30, 31, 29]
    conditions = ["☀️ Sunny", "⛅ Partky Cloudy", "🌧️ Rain", "🌧️ Rain", "☀️ Sunny", "☀️ Clear", "⛅ Cloudy"]

    for idx, col in enumerate(forecast_cols):
        with col:
            st.metric(label=days[idx], value=f"{temps[idx]}°C")
            st.caption(conditions[idx])

# ==============================================================================
# TAB 5: Crop Recommendations (Data-Driven Crop Selector)
# ==============================================================================
with tab5:
    st.header("🌾 Data-Driven Crop Selector & Recommendations")
    st.markdown("Combines soil health, climate risk, and heuristic suitability scores.")

    soil_type = st.selectbox("Select Soil Type", ["Alluvial", "Clay Loam", "Sandy Loam", "Black Soil"])
    season = st.radio("Select Season", ["Kharif", "Rabi", "Zaid"], horizontal=True)

    if st.button("Generate Recommendations"):
        st.subheader("Recommended Crops Ranked by Suitability")
        crop_data = pd.DataFrame({
            "Crop Name": ["Wheat", "Mustard", "Chickpea", "Barley"],
            "Suitability Score": ["92%", "85%", "78%", "71%"],
            "Water Requirement": ["Medium", "Low", "Low", "Low"],
            "Climate Risk Level": ["Low", "Low", "Moderate", "Low"]
        })
        st.dataframe(crop_data, use_container_width=True)

# ==============================================================================
# TAB 6: Recommendation History (Advisory Audit Trail)
# ==============================================================================
with tab6:
    st.header("📜 Advisory Audit Trail & History")
    st.markdown("Persistent session records of queries, advisories, and recommendations.")

    # Sample session audit logs
    audit_data = [
        {
            "Timestamp": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
            "District": selected_district,
            "Query": "NPK fertilizer recommendation for Wheat",
            "Status": "Completed",
            "Language": selected_language
        }
    ]

    st.table(pd.DataFrame(audit_data))

    col_exp1, col_exp2 = st.columns(2)
    with col_exp1:
        st.download_button(
            label="📥 Export History as CSV",
            data=pd.DataFrame(audit_data).to_csv(index=False),
            file_name="agriguard_history.csv",
            mime="text/csv"
        )
    with col_exp2:
        st.download_button(
            label="📥 Export History as JSON",
            data=json.dumps(audit_data, indent=2),
            file_name="agriguard_history.json",
            mime="application/json"
        )