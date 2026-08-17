# ==============================================================================
# Epic 2 - Story 2: Exploratory Data Analysis (EDA) & Agricultural Corpus Statistics
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set global plotting style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ------------------------------------------------------------------------------
# 1. Load All Four Agricultural Datasets
# ------------------------------------------------------------------------------
print("=" * 60)
print("1. Loading Agricultural Corpus Datasets")
print("=" * 60)

DATA_DIR = "/content/unzipped_data"

# Load Datasets
feature_store = pd.read_csv(os.path.join(DATA_DIR, "merged_feature_store.csv"))
multilingual_adv = pd.read_csv(os.path.join(DATA_DIR, "Multilingual_Expert_Advisory.csv"))
smart_reports = pd.read_csv(os.path.join(DATA_DIR, "Smart_Advisory_Reports_All.csv"))
decadal_master = pd.read_csv(os.path.join(DATA_DIR, "Unified_Decadal_Master_2015_2024.csv"))

print("✅ DATASETS LOADED SUCCESSFULLY!\n")

# ------------------------------------------------------------------------------
# 2. Decadal Dataset Summary & Corpus Statistics (2015-2024)
# ------------------------------------------------------------------------------
print("=" * 60)
print("2. Decadal Corpus Overview")
print("=" * 60)

print(f"Decadal Master Rows/Cols: {decadal_master.shape}")
print(f"Temporal Metadata Range: {decadal_master['Year'].min()} - {decadal_master['Year'].max()}")
print(f"Total Unique Expert Advisories: {len(multilingual_adv)}")

# ------------------------------------------------------------------------------
# 3. Statistical Analysis (Rainfall, NDVI & MSP Fluctuations)
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("3. Computing Statistical Metrics")
print("=" * 60)

# A. Average Rainfall by State & District
if 'State' in decadal_master.columns and 'Rainfall_IMD_mm' in decadal_master.columns:
    state_rainfall = decadal_master.groupby(['State', 'District'])['Rainfall_IMD_mm'].mean().reset_index()
    print("--- State & District Rainfall Averages (Top 5) ---")
    print(state_rainfall.head())

# B. Annual Mean NDVI Vegetation Index
if 'NDVI' in decadal_master.columns and 'Year' in decadal_master.columns:
    ndvi_trends = decadal_master.groupby('Year')['NDVI'].mean()
    print("\n--- Annual NDVI Vegetation Trends ---")
    print(ndvi_trends)

# C. Minimum Support Price (MSP) Fluctuations
if 'Crop' in decadal_master.columns and 'MSP' in decadal_master.columns:
    msp_summary = decadal_master.groupby(['Year', 'Crop'])['MSP'].mean().unstack()
    print("\n--- MSP Fluctuations by Crop ---")
    print(msp_summary.tail())

# ------------------------------------------------------------------------------
# 4. Data Visualizations
# ------------------------------------------------------------------------------
print("\n" + "=" * 60)
print("4. Plotting Time-Series Trends & Correlation Matrices")
print("=" * 60)

# Plot 1: Decadal Climate Time-Series (Rainfall & Temperature 2015-2024)
if 'Year' in decadal_master.columns and 'Rainfall_IMD_mm' in decadal_master.columns:
    fig, ax1 = plt.subplots(figsize=(12, 5))
    
    annual_climate = decadal_master.groupby('Year').agg({
        'Rainfall_IMD_mm': 'mean',
        'Mean_Temp_Historical': 'mean'
    }).reset_index()

    ax2 = ax1.twinx()
    sns.lineplot(data=annual_climate, x='Year', y='Rainfall_IMD_mm', ax=ax1, color='b', marker='o', label='Rainfall (mm)')
    sns.lineplot(data=annual_climate, x='Year', y='Mean_Temp_Historical', ax=ax2, color='r', marker='s', label='Mean Temp (°C)')

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Rainfall (mm)', color='b')
    ax2.set_ylabel('Mean Temp (°C)', color='r')
    plt.title('Decadal Climate Trends (2015-2024)')
    plt.tight_layout()
    plt.show()

# Plot 2: NPK Soil Profile & Yield Correlation Heatmap
npk_cols = [col for col in ['Nitrogen', 'Phosphorus', 'Potassium', 'soil_ph', 'Yield', 'Rainfall_IMD_mm'] if col in decadal_master.columns]
if len(npk_cols) > 1:
    plt.figure(figsize=(8, 6))
    sns.heatmap(decadal_master[npk_cols].corr(), annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title('Correlation Matrix: NPK Soil Profile vs Yield & Climate')
    plt.tight_layout()
    plt.show()

# Plot 3: Regional Soil pH Distribution
if 'soil_ph' in decadal_master.columns:
    plt.figure(figsize=(9, 4))
    sns.histplot(data=decadal_master, x='soil_ph', kde=True, color='teal', bins=20)
    plt.title('Soil pH Distribution Across Regions')
    plt.xlabel('Soil pH Value')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

print("🚀 Story 2 EDA and Agricultural Statistics execution completed successfully!")