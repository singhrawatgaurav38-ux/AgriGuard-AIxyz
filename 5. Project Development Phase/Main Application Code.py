import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import os
from gtts import gTTS
from io import BytesIO
from groq import Groq
from dotenv import load_dotenv

# Epic 1: Load Environment Variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if GROQ_API_KEY:
    groq_client = Groq(api_key=GROQ_API_KEY)

# --- Epic 3: Core Engines (Heuristics & Risk Detection) ---
def detect_climate_risk(temp, rainfall):
    """Epic 3, Story 2: Climate Risk Detection"""
    risk = "Low Risk"
    if temp > 35 and rainfall < 50:
        risk = "Drought & Heat Stress Risk ⚠️"
    elif rainfall > 200:
        risk = "Flood Risk 🌊"
    return risk

def get_weather_data(lat, lon):
    """Epic 3, Story 3: OpenMeteo API Integration"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url)
        return response.json().get("current_weather", {})
    except Exception as e:
        return {"error": str(e)}

# --- Epic 5, Story 1: 6-Tab Streamlit Layout ---
st.set_page_config(page_title="AgriGuard AI", page_icon="🌱", layout="wide")
st.title("🌱 AgriGuard AI: Climate-Smart Advisory System")
st.markdown("Powered by Ensemble AI, OpenMeteo & Groq")

# Creating the 6 Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "1️⃣ Data Input", 
    "2️⃣ Weather & Risk", 
    "3️⃣ Ensemble Advisory", 
    "4️⃣ Analytics Dashboard", 
    "5️⃣ Multilingual & Voice", 
    "6️⃣ Export History"
])

# ==========================================
# TAB 1: Dynamic Input & Heuristics
# ==========================================
with tab1:
    st.header("Farmer & Soil Data")
    col1, col2 = st.columns(2)
    with col1:
        # Epic 5, Story 2: Dynamic Selectors
        state = st.selectbox("Select State", ["Uttarakhand", "Punjab", "Maharashtra"])
        district = st.selectbox("Select District", ["Nainital", "Dehradun", "Almora"] if state=="Uttarakhand" else ["Other"])
        crop = st.selectbox("Target Crop", ["Wheat", "Rice", "Sugarcane", "Maize"])
    
    with col2:
        st.subheader("Soil Parameters (NPK & pH)")
        n_val = st.number_input("Nitrogen (N)", 0, 200, 50)
        p_val = st.number_input("Phosphorus (P)", 0, 200, 30)
        k_val = st.number_input("Potassium (K)", 0, 200, 40)
        ph_val = st.slider("Soil pH", 0.0, 14.0, 6.5)

# ==========================================
# TAB 2: Weather API & Risk Detection
# ==========================================
with tab2:
    st.header("Real-Time Weather & Climate Risk")
    if st.button("Fetch Real-Time Weather"):
        with st.spinner("Fetching from OpenMeteo..."):
            # Coordinates for demo (e.g., Haldwani/Nainital area)
            weather = get_weather_data(29.21, 79.51) 
            if "error" not in weather:
                current_temp = weather.get("temperature", 25)
                current_rain = 40 # Simulated current rainfall
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Temperature", f"{current_temp} °C")
                col2.metric("Wind Speed", f"{weather.get('windspeed', 0)} km/h")
                
                risk_status = detect_climate_risk(current_temp, current_rain)
                col3.metric("Climate Risk Status", risk_status)
            else:
                st.error("Failed to fetch weather data.")

# ==========================================
# TAB 3: Ensemble AI Advisory (Groq Llama 3)
# ==========================================
with tab3:
    st.header("AI-Generated Advisory")
    if st.button("Generate Climate-Smart Advisory"):
        if GROQ_API_KEY:
            with st.spinner("Synthesizing data with Groq Llama 3.3-70B..."):
                prompt = f"""
                Act as an agricultural expert. Give a short advisory for {crop} farming in {district}, {state}.
                Soil Data: N={n_val}, P={p_val}, K={k_val}, pH={ph_val}.
                Provide 3 actionable steps.
                """
                try:
                    response = groq_client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama3-70b-8192" # Epic 4, Story 2 model spec
                    )
                    advisory_text = response.choices[0].message.content
                    st.success("Advisory Generated!")
                    st.write(advisory_text)
                    # Save to session state for Translation/Voice
                    st.session_state['advisory'] = advisory_text 
                except Exception as e:
                    st.error(f"Groq API Error: {e}")
        else:
            st.warning("Please configure your GROQ_API_KEY in the .env file.")

# ==========================================
# TAB 4: Analytics Dashboard (Plotly)
# ==========================================
with tab4:
    st.header("10-Year Climate Trend Visualization")
    # Epic 5, Story 3: Plotly integration with dummy historical data
    years = np.arange(2014, 2024)
    rainfall = np.random.randint(800, 1200, size=10)
    df_trend = pd.DataFrame({"Year": years, "Rainfall (mm)": rainfall})
    
    fig = px.line(df_trend, x="Year", y="Rainfall (mm)", title=f"Historical Rainfall Trends for {district}", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# TAB 5: Multilingual & Voice (gTTS)
# ==========================================
with tab5:
    st.header("Translation & Voice (Text-to-Speech)")
    lang = st.selectbox("Select Language", ["English (en)", "Hindi (hi)"])
    
    if st.button("Generate Audio") and 'advisory' in st.session_state:
        lang_code = lang.split("(")[1].replace(")", "")
        with st.spinner("Generating Voice Output..."):
            tts = gTTS(text=st.session_state['advisory'], lang=lang_code, slow=False)
            audio_bytes = BytesIO()
            tts.write_to_fp(audio_bytes)
            st.audio(audio_bytes, format="audio/mp3")

# ==========================================
# TAB 6: Export Management
# ==========================================
with tab6:
    st.header("Recommendation History & Export")
    st.info("Export your AI-generated advisories here.")
    if 'advisory' in st.session_state:
        # Epic 5, Story 4: JSON/CSV Export Support
        df_export = pd.DataFrame({"Crop": [crop], "District": [district], "Advisory": [st.session_state['advisory']]})
        
        col1, col2 = st.columns(2)
        with col1:
            csv = df_export.to_csv(index=False).encode('utf-8')
            st.download_button("Download as CSV", csv, "advisory.csv", "text/csv")
        with col2:
            json_data = df_export.to_json(orient="records")
            st.download_button("Download as JSON", json_data, "advisory.json", "application/json")