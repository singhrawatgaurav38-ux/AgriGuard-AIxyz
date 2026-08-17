# ==============================================================================
# AgriGuard AI - Multi-Factor Climate Risk Scoring Engine
# Epic 3: Hybrid Intelligence System & Climate-Smart Advisory Pipeline
# ==============================================================================

def evaluate_climate_risk(
    rainfall: float,
    temperature: float,
    nitrogen: float,
    phosphorus: float,
    potassium: float,
    ph: float,
    crop: str = "General Crop"
) -> dict:
    """
    Evaluates multi-factor climate threats and soil anomalies on a 0-100 risk scale.
    
    Risk Matrix:
    - Drought Detection (Rainfall < 200mm): +25 pts
    - Flood Detection (Rainfall > 2000mm): +15 pts
    - Temperature Stress (<10°C or >40°C): +20 pts
    - Nutrient Imbalance (N/P/K out of bounds): +15/+10/+10 pts
    - Soil Acidity/Alkalinity (pH < 5.0 or > 8.0): +20 pts
    """
    raw_risk_score = 0.0
    detected_threats = []
    breakdown = {}

    # --------------------------------------------------------------------------
    # 1. Drought Detection (< 200mm)
    # --------------------------------------------------------------------------
    if rainfall < 200.0:
        raw_risk_score += 25.0
        detected_threats.append(f"Severe Drought Hazard: Rainfall is {rainfall:.1f}mm (< 200mm)")
        breakdown["drought_risk"] = 25.0
    else:
        breakdown["drought_risk"] = 0.0

    # --------------------------------------------------------------------------
    # 2. Flood & Waterlogging Detection (> 2000mm)
    # --------------------------------------------------------------------------
    if rainfall > 2000.0:
        raw_risk_score += 15.0
        detected_threats.append(f"Flood & Waterlogging Hazard: Rainfall is {rainfall:.1f}mm (> 2000mm)")
        breakdown["flood_risk"] = 15.0
    else:
        breakdown["flood_risk"] = 0.0

    # --------------------------------------------------------------------------
    # 3. Extreme Temperature Stress (< 10°C or > 40°C)
    # --------------------------------------------------------------------------
    if temperature < 10.0 or temperature > 40.0:
        raw_risk_score += 20.0
        condition = "Cold Stress (<10°C)" if temperature < 10.0 else "Extreme Heat Stress (>40°C)"
        detected_threats.append(f"{condition}: Current temperature is {temperature:.1f}°C")
        breakdown["temperature_risk"] = 20.0
    else:
        breakdown["temperature_risk"] = 0.0

    # --------------------------------------------------------------------------
    # 4. Nutrient Imbalance Scoring (N: 40-200, P: 20-80, K: 40-180)
    # --------------------------------------------------------------------------
    npk_risk = 0.0

    # Nitrogen check (+15 pts)
    if nitrogen < 40.0 or nitrogen > 200.0:
        npk_risk += 15.0
        detected_threats.append(f"Nitrogen Imbalance: {nitrogen} kg/ha (Optimal: 40-200 kg/ha)")

    # Phosphorus check (+10 pts)
    if phosphorus < 20.0 or phosphorus > 80.0:
        npk_risk += 10.0
        detected_threats.append(f"Phosphorus Imbalance: {phosphorus} kg/ha (Optimal: 20-80 kg/ha)")

    # Potassium check (+10 pts)
    if potassium < 40.0 or potassium > 180.0:
        npk_risk += 10.0
        detected_threats.append(f"Potassium Imbalance: {potassium} kg/ha (Optimal: 40-180 kg/ha)")

    raw_risk_score += npk_risk
    breakdown["nutrient_imbalance_risk"] = npk_risk

    # --------------------------------------------------------------------------
    # 5. Soil Acidity & Alkalinity Stress (pH < 5.0 or > 8.0)
    # --------------------------------------------------------------------------
    if ph < 5.0 or ph > 8.0:
        raw_risk_score += 20.0
        status = "Acidic Stress" if ph < 5.0 else "Alkaline Stress"
        detected_threats.append(f"Soil {status}: pH level is {ph:.1f} (Optimal: 5.5-7.5)")
        breakdown["ph_stress_risk"] = 20.0
    else:
        breakdown["ph_stress_risk"] = 0.0

    # Cap risk score at maximum 100.0
    final_risk_score = min(100.0, raw_risk_score)

    # Risk Category Classification
    if final_risk_score >= 75.0:
        risk_level = "Severe Risk"
    elif final_risk_score >= 50.0:
        risk_level = "High Risk"
    elif final_risk_score >= 25.0:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"

    return {
        "crop": crop,
        "overall_risk_score": final_risk_score,
        "risk_level": risk_level,
        "detected_threats": detected_threats,
        "risk_breakdown": breakdown
    }


# Standalone Test Execution
if __name__ == "__main__":
    import json
    test_assessment = evaluate_climate_risk(
        rainfall=150.0,      # Drought trigger (+25)
        temperature=42.5,   # Heat stress trigger (+20)
        nitrogen=30.0,      # Low N (+15)
        phosphorus=15.0,    # Low P (+10)
        potassium=100.0,    # Optimal (0)
        ph=4.5,             # Acidic trigger (+20)
        crop="Wheat"
    )
    print(json.dumps(test_assessment, indent=2))