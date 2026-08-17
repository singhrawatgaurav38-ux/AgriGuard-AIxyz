-- Farmers Table Entity
CREATE TABLE Farmers (
    farmer_id INT PRIMARY KEY, -- Primary key and unique identifier
    farmer_name VARCHAR(255), -- Name of the farmer or user[cite: 1]
    mobile_number VARCHAR(15), -- Contact number for notifications[cite: 1]
    state VARCHAR(100), -- Farmer's state location[cite: 1]
    district VARCHAR(100), -- Farmer's district location[cite: 1]
    preferred_language VARCHAR(50), -- Selected advisory language[cite: 1]
    farm_size DECIMAL(10, 2), -- Total agricultural land area[cite: 1]
    created_at TIMESTAMP -- Account registration timestamp[cite: 1]
);

-- Advisory_Records Table Entity[cite: 1]
CREATE TABLE Advisory_Records (
    advisory_id INT PRIMARY KEY, -- Primary key of the advisory session[cite: 1]
    farmer_id INT, -- Foreign key referencing the farmer[cite: 1]
    crop_name VARCHAR(100), -- Selected crop for recommendation analysis[cite: 1]
    nitrogen_level DECIMAL(5, 2), -- Soil nitrogen value[cite: 1]
    phosphorus_level DECIMAL(5, 2), -- Soil phosphorus value[cite: 1]
    potassium_level DECIMAL(5, 2), -- Soil potassium value[cite: 1]
    soil_ph DECIMAL(4, 2), -- Soil pH measurement[cite: 1]
    temperature DECIMAL(5, 2), -- Current environmental temperature[cite: 1]
    rainfall DECIMAL(6, 2), -- Rainfall value used for analysis[cite: 1]
    humidity DECIMAL(5, 2), -- Real-time humidity information[cite: 1]
    suitability_score DECIMAL(5, 2), -- AI-generated crop suitability percentage[cite: 1]
    climate_risk_score DECIMAL(5, 2), -- Climate risk assessment score[cite: 1]
    risk_category VARCHAR(50), -- Drought, Flood, Heat Stress, or Low Risk classification[cite: 1]
    recommended_actions TEXT, -- Suggested farming interventions[cite: 1]
    weather_forecast TEXT, -- Integrated weather forecast information[cite: 1]
    ai_advisory TEXT, -- Final AI-generated climate-smart recommendation[cite: 1]
    language_used VARCHAR(50), -- Language used for advisory generation[cite: 1]
    model_used VARCHAR(50), -- T5-PEFT, Climate-LoRA, Ollama, or Ensemble Mode[cite: 1]
    advisory_timestamp TIMESTAMP, -- Date and time of advisory generation[cite: 1]
    export_status BOOLEAN, -- Indicates whether the advisory was exported as JSON/CSV[cite: 1]
    
    -- Establishes the 1 to Many relationship[cite: 1]
    FOREIGN KEY (farmer_id) REFERENCES Farmers(farmer_id)
);