from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Farmers Entity[cite: 1]
class Farmer(Base):
    __tablename__ = 'farmers'

    farmer_id = Column(Integer, primary_key=True) # Primary key[cite: 1]
    farmer_name = Column(String, nullable=False) # Name of the farmer or user[cite: 1]
    mobile_number = Column(String(15)) # Contact number[cite: 1]
    state = Column(String(100)) # State location[cite: 1]
    district = Column(String(100)) # District location[cite: 1]
    preferred_language = Column(String(50)) # Selected advisory language[cite: 1]
    farm_size = Column(Float) # Total agricultural land area[cite: 1]
    created_at = Column(DateTime) # Account registration timestamp[cite: 1]

    # One-to-Many Relationship setup[cite: 1]
    advisory_records = relationship("AdvisoryRecord", back_populates="farmer")

# Advisory_Records Entity[cite: 1]
class AdvisoryRecord(Base):
    __tablename__ = 'advisory_records'

    advisory_id = Column(Integer, primary_key=True) # Primary key[cite: 1]
    farmer_id = Column(Integer, ForeignKey('farmers.farmer_id')) # Foreign key[cite: 1]
    
    crop_name = Column(String(100)) # Selected crop[cite: 1]
    nitrogen_level = Column(Float) # Soil nitrogen value[cite: 1]
    phosphorus_level = Column(Float) # Soil phosphorus value[cite: 1]
    potassium_level = Column(Float) # Soil potassium value[cite: 1]
    soil_ph = Column(Float) # Soil pH measurement[cite: 1]
    temperature = Column(Float) # Environmental temperature[cite: 1]
    rainfall = Column(Float) # Rainfall value[cite: 1]
    humidity = Column(Float) # Real-time humidity[cite: 1]
    
    suitability_score = Column(Float) # AI-generated crop suitability percentage[cite: 1]
    climate_risk_score = Column(Float) # Climate risk assessment score[cite: 1]
    risk_category = Column(String(50)) # Drought, Flood, Heat Stress, or Low Risk[cite: 1]
    recommended_actions = Column(Text) # Suggested farming interventions[cite: 1]
    weather_forecast = Column(Text) # Integrated weather forecast[cite: 1]
    ai_advisory = Column(Text) # Final AI-generated climate-smart recommendation[cite: 1]
    
    language_used = Column(String(50)) # Language used for advisory generation[cite: 1]
    model_used = Column(String(50)) # T5-PEFT, Climate-LoRA, Ollama, or Ensemble Mode[cite: 1]
    advisory_timestamp = Column(DateTime) # Date and time of advisory generation[cite: 1]
    export_status = Column(Boolean) # Indicates export status[cite: 1]

    # Establishing back-reference to Farmer
    farmer = relationship("Farmer", back_populates="advisory_records")