# ==============================================================================
# AgriGuard AI - 10-Year Historical CSV Context Retriever
# Epic 3: Hybrid Intelligence System & Climate-Smart Advisory Pipeline
# ==============================================================================

import os
import logging
import pandas as pd
from typing import Dict, Any, Optional
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Default dataset location
DEFAULT_CSV_PATH = Path("data/raw/Unified_Decadal_Master_2015_2024.csv")


class HistoricalContextRetriever:
    """
    Retrieves and aggregates 10-year historical climate, yield, and soil 
    performance data (2015-2024) to enrich LLM prompts and heuristic scoring.
    """

    def __init__(self, csv_path: Optional[Path] = None):
        self.csv_path = Path(csv_path) if csv_path else DEFAULT_CSV_PATH
        self.df = self._load_dataset()

    def _load_dataset(self) -> pd.DataFrame:
        """Loads decadal CSV file or initializes a mock DataFrame if missing."""
        if self.csv_path.exists():
            try:
                df = pd.read_csv(self.csv_path)
                logging.info(f"Loaded 10-Year historical master data from: {self.csv_path}")
                return df
            except Exception as e:
                logging.error(f"Error loading CSV file {self.csv_path}: {e}")

        logging.warning("Historical dataset not found on disk. Initializing fallback schema.")
        return self._generate_fallback_dataframe()

    def _generate_fallback_dataframe(self) -> pd.DataFrame:
        """Fallback mock data for testing environment without mounted Drive."""
        data = [
            {
                "Year": year,
                "State": "Uttarakhand",
                "District": "Nainital",
                "Crop": "Wheat",
                "Rainfall_IMD_mm": 1100.0 + (year - 2015) * 15,
                "Mean_Temp_Historical": 22.5 + (year - 2015) * 0.2,
                "Yield_Kg_Ha": 2800 + (year - 2015) * 50,
                "NDVI": 0.68 + (year - 2015) * 0.01,
                "Soil_pH": 6.4
            }
            for year in range(2015, 2025)
        ]
        return pd.DataFrame(data)

    def get_10yr_summary(
        self,
        state: str,
        district: str,
        crop: str
    ) -> Dict[str, Any]:
        """
        Extracts 10-year historical averages and extreme weather metrics 
        for a target location and crop.
        """
        state_clean = state.strip().title()
        district_clean = district.strip().title()
        crop_clean = crop.strip().title()

        # Filter dataset
        filtered_df = self.df[
            (self.df["State"].astype(str).str.title() == state_clean) &
            (self.df["District"].astype(str).str.title() == district_clean)
        ]

        # Crop-level filtering if available
        if "Crop" in filtered_df.columns and not filtered_df.empty:
            crop_filtered = filtered_df[filtered_df["Crop"].astype(str).str.title() == crop_clean]
            if not crop_filtered.empty:
                filtered_df = crop_filtered

        # Fallback to state-wide average if district records are missing
        if filtered_df.empty:
            logging.warning(f"No specific records for {district_clean}, {state_clean}. Reverting to state baseline.")
            filtered_df = self.df[self.df["State"].astype(str).str.title() == state_clean]

        if filtered_df.empty:
            # Fallback to entire dataset baseline
            filtered_df = self.df

        # Calculate 10-Year (2015-2024) Aggregated Metrics
        avg_rainfall = filtered_df["Rainfall_IMD_mm"].mean() if "Rainfall_IMD_mm" in filtered_df.columns else 950.0
        max_rainfall = filtered_df["Rainfall_IMD_mm"].max() if "Rainfall_IMD_mm" in filtered_df.columns else 1400.0
        min_rainfall = filtered_df["Rainfall_IMD_mm"].min() if "Rainfall_IMD_mm" in filtered_df.columns else 500.0

        avg_temp = filtered_df["Mean_Temp_Historical"].mean() if "Mean_Temp_Historical" in filtered_df.columns else 24.5
        max_temp = filtered_df["Mean_Temp_Historical"].max() if "Mean_Temp_Historical" in filtered_df.columns else 38.0

        avg_yield = filtered_df["Yield_Kg_Ha"].mean() if "Yield_Kg_Ha" in filtered_df.columns else 2500.0
        avg_ndvi = filtered_df["NDVI"].mean() if "NDVI" in filtered_df.columns else 0.65
        avg_ph = filtered_df["Soil_pH"].mean() if "Soil_pH" in filtered_df.columns else 6.5

        return {
            "query_context": {
                "state": state_clean,
                "district": district_clean,
                "crop": crop_clean,
                "period": "2015-2024 (10 Years)"
            },
            "historical_climate_averages": {
                "mean_annual_rainfall_mm": round(float(avg_rainfall), 2),
                "max_recorded_rainfall_mm": round(float(max_rainfall), 2),
                "min_recorded_rainfall_mm": round(float(min_rainfall), 2),
                "mean_temperature_c": round(float(avg_temp), 2),
                "max_recorded_temp_c": round(float(max_temp), 2)
            },
            "agronomic_baselines": {
                "historical_yield_kg_ha": round(float(avg_yield), 2),
                "historical_ndvi_index": round(float(avg_ndvi), 3),
                "baseline_soil_ph": round(float(avg_ph), 2)
            },
            "records_found": len(filtered_df)
        }


# Standalone execution test
if __name__ == "__main__":
    import json
    retriever = HistoricalContextRetriever()
    
    # Test query for Nainital, Uttarakhand, Wheat
    summary = retriever.get_10yr_summary(
        state="Uttarakhand",
        district="Nainital",
        crop="Wheat"
    )
    
    print(json.dumps(summary, indent=2))