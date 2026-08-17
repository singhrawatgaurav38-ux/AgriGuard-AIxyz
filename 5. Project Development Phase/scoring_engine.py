# ==============================================================================
# AgriGuard AI - Heuristic Scoring Engine
# Epic 3: Hybrid Intelligence System & Climate-Smart Advisory Pipeline
# ==============================================================================

def calculate_heuristic_score(
    nitrogen: float,
    phosphorus: float,
    potassium: float,
    ph: float,
    rainfall: float,
    temperature: float,
    crop: str
) -> dict:
    """
    Evaluates crop suitability (0-100 score) based on NPK balance, pH deviation,
    rainfall adequacy, and temperature thresholds.
    
    Returns score breakdown, penalties list, and suitability status.
    """
    penalties = []
    crop_lower = crop.lower().strip()

    # --------------------------------------------------------------------------
    # 1. NPK Balance Score (Max 30 Points)
    # --------------------------------------------------------------------------
    npk_score = 30.0
    
    # Crop-specific threshold allocation
    high_n_crops = ['rice', 'wheat', 'maize', 'sugarcane']
    min_n, max_n = (80, 200) if crop_lower in high_n_crops else (40, 140)
    min_p, max_p = 20, 80
    min_k, max_k = 40, 180

    # Nitrogen evaluation
    if nitrogen < min_n:
        npk_score -= 10
        penalties.append(f"Low Nitrogen level ({nitrogen} kg/ha). Ideal for {crop}: {min_n}-{max_n} kg/ha (-10 pts)")
    elif nitrogen > max_n:
        npk_score -= 5
        penalties.append(f"Excessive Nitrogen level ({nitrogen} kg/ha). Ideal max: {max_n} kg/ha (-5 pts)")

    # Phosphorus evaluation
    if phosphorus < min_p:
        npk_score -= 10
        penalties.append(f"Low Phosphorus level ({phosphorus} kg/ha). Ideal min: {min_p} kg/ha (-10 pts)")
    elif phosphorus > max_p:
        npk_score -= 5
        penalties.append(f"Excessive Phosphorus level ({phosphorus} kg/ha). Ideal max: {max_p} kg/ha (-5 pts)")

    # Potassium evaluation
    if potassium < min_k:
        npk_score -= 10
        penalties.append(f"Low Potassium level ({potassium} kg/ha). Ideal min: {min_k} kg/ha (-10 pts)")
    elif potassium > max_k:
        npk_score -= 5
        penalties.append(f"Excessive Potassium level ({potassium} kg/ha). Ideal max: {max_k} kg/ha (-5 pts)")

    npk_score = max(0.0, npk_score)

    # --------------------------------------------------------------------------
    # 2. Dynamic pH Deviation Score (Max 20 Points)
    # --------------------------------------------------------------------------
    ph_score = 20.0
    
    # Dynamic ideal pH lookup
    if crop_lower in ['rice']:
        ideal_ph = 6.0
    elif crop_lower in ['potato', 'tea']:
        ideal_ph = 5.5
    else:
        ideal_ph = 6.5  # default

    ph_deviation = abs(ph - ideal_ph)

    if ph_deviation > 1.5:
        ph_score -= 15
        penalties.append(f"pH far from ideal for {crop} (Current: {ph}, Ideal: {ideal_ph}) (-15 pts)")
    elif ph_deviation > 1.0:
        ph_score -= 8
        penalties.append(f"Moderate pH deviation for {crop} (Current: {ph}, Ideal: {ideal_ph}) (-8 pts)")
    elif ph_deviation > 0.5:
        ph_score -= 3
        penalties.append(f"Slight pH deviation for {crop} (Current: {ph}, Ideal: {ideal_ph}) (-3 pts)")

    ph_score = max(0.0, ph_score)

    # --------------------------------------------------------------------------
    # 3. Rainfall Score (Max 25 Points)
    # --------------------------------------------------------------------------
    rainfall_score = 25.0
    
    if crop_lower in ['rice', 'sugarcane']:
        if rainfall < 600:
            rainfall_score -= 15
            penalties.append(f"Insufficient rainfall for high-water crop '{crop}' ({rainfall}mm < 600mm) (-15 pts)")
        elif rainfall > 2000:
            rainfall_score -= 5
            penalties.append(f"Excess rainfall may cause waterlogging for '{crop}' ({rainfall}mm > 2000mm) (-5 pts)")
    elif crop_lower in ['wheat', 'maize']:
        if rainfall < 400:
            rainfall_score -= 15
            penalties.append(f"Insufficient rainfall for '{crop}' ({rainfall}mm < 400mm) (-15 pts)")
        elif rainfall > 1500:
            rainfall_score -= 5
            penalties.append(f"Excess rainfall for '{crop}' ({rainfall}mm > 1500mm) (-5 pts)")
    else:
        if rainfall < 300:
            rainfall_score -= 15
            penalties.append(f"Critically low rainfall ({rainfall}mm) (-15 pts)")
        elif rainfall > 1800:
            rainfall_score -= 5
            penalties.append(f"Excess rainfall risk ({rainfall}mm) (-5 pts)")

    rainfall_score = max(0.0, rainfall_score)

    # --------------------------------------------------------------------------
    # 4. Temperature Score (Max 25 Points)
    # --------------------------------------------------------------------------
    temp_score = 25.0
    
    warm_season_crops = ['rice', 'cotton', 'sugarcane', 'maize']
    cool_season_crops = ['wheat', 'barley', 'mustard', 'potato']

    if crop_lower in warm_season_crops:
        if temperature < 20:
            temp_score -= 15
            penalties.append(f"Too cold for warm-season crop '{crop}' ({temperature}°C < 20°C) (-15 pts)")
        elif temperature > 38:
            temp_score -= 10
            penalties.append(f"Too hot, heat stress risk for '{crop}' ({temperature}°C > 38°C) (-10 pts)")
    elif crop_lower in cool_season_crops:
        if temperature < 15:
            temp_score -= 15
            penalties.append(f"Too cold for cool-season crop '{crop}' ({temperature}°C < 15°C) (-15 pts)")
        elif temperature > 30:
            temp_score -= 10
            penalties.append(f"Too hot for cool-season crop '{crop}' ({temperature}°C > 30°C) (-10 pts)")
    else:
        if temperature < 15:
            temp_score -= 15
            penalties.append(f"Sub-optimal low temperature ({temperature}°C) (-15 pts)")
        elif temperature > 35:
            temp_score -= 10
            penalties.append(f"High temperature stress ({temperature}°C) (-10 pts)")

    temp_score = max(0.0, temp_score)

    # --------------------------------------------------------------------------
    # 5. Final Calculation & Classification
    # --------------------------------------------------------------------------
    final_score = npk_score + ph_score + rainfall_score + temp_score

    if final_score >= 85:
        suitability = "Highly Suitable"
    elif final_score >= 65:
        suitability = "Moderately Suitable"
    elif final_score >= 45:
        suitability = "Marginally Suitable"
    else:
        suitability = "Unsuitable"

    return {
        "crop": crop,
        "final_score": round(final_score, 2),
        "suitability_level": suitability,
        "component_scores": {
            "npk_score": round(npk_score, 2),
            "ph_score": round(ph_score, 2),
            "rainfall_score": round(rainfall_score, 2),
            "temp_score": round(temp_score, 2)
        },
        "penalties": penalties
    }


# Standalone execution test
if __name__ == "__main__":
    test_result = calculate_heuristic_score(
        nitrogen=120,
        phosphorus=15,
        potassium=50,
        ph=5.2,
        rainfall=500,
        temperature=18,
        crop="Rice"
    )
    import json
    print(json.dumps(test_result, indent=2))