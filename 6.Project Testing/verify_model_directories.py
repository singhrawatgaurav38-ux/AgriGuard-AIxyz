import os
import sys
import shutil
import logging
from pathlib import Path

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Required directory layout for AgriGuard AI
REQUIRED_DIRECTORIES = {
    "Raw Datasets": "data/raw",
    "Processed Features": "data/processed",
    "10-Year Historical Data": "data/historical_10yr",
    "T5-PEFT Model Weights": "models/t5_peft",
    "Climate-LoRA Adapters": "models/climate_lora",
    "Ensemble Configuration": "models/ensemble",
    "Artifacts & Schemas": "artifacts",
    "Advisory Exports": "exports",
    "System Logs": "logs"
}

# Critical artifacts to check
MODEL_ARTIFACTS = {
    "T5-PEFT Adapter Config": "models/t5_peft/adapter_config.json",
    "Climate-LoRA Model Weights": "models/climate_lora/adapter_model.bin",
    "Historical Climate CSV": "data/historical_10yr/climate_data.csv"
}

def verify_disk_space(path=".", min_free_gb=5.0) -> bool:
    """Check available disk space for model storage."""
    total, used, free = shutil.disk_usage(path)
    free_gb = free / (1024 ** 3)
    logging.info(f"Disk Space Check: {free_gb:.2f} GB free available.")
    
    if free_gb < min_free_gb:
        logging.warning(f"Low disk space warning! Recommended minimum: {min_free_gb} GB.")
        return False
    return True

def verify_and_create_directories():
    """Ensure all required directories exist and are writable."""
    print("=" * 60)
    print(" AgriGuard AI - Model & Data Directory Verification")
    print("=" * 60)

    all_ok = True
    for name, dir_path in REQUIRED_DIRECTORIES.items():
        path = Path(dir_path)
        try:
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                print(f"  [CREATED]  {name:<25} -> {dir_path}/")
            else:
                print(f"  [EXISTS]   {name:<25} -> {dir_path}/")
            
            # Check write permissions
            test_file = path / ".write_test"
            test_file.touch()
            test_file.unlink()
        except Exception as e:
            print(f"  [ERROR]    {name:<25} -> Permission/Creation issue: {e}")
            all_ok = False

    return all_ok

def check_artifact_status():
    """Check presence of optional or trained model artifacts."""
    print("\n" + "-" * 60)
    print(" Model Weights & Dataset Artifact Verification")
    print("-" * 60)

    for artifact_name, rel_path in MODEL_ARTIFACTS.items():
        path = Path(rel_path)
        if path.exists():
            size_mb = path.stat().st_size / (1024 * 1024)
            print(f"  ✓ FOUND:   {artifact_name:<30} ({size_mb:.2f} MB)")
        else:
            print(f"  ⏳ PENDING: {artifact_name:<30} (Will be populated in Epic 2)")

if __name__ == "__main__":
    space_ok = verify_disk_space(min_free_gb=5.0)
    dirs_ok = verify_and_create_directories()
    check_artifact_status()

    print("\n" + "=" * 60)
    if space_ok and dirs_ok:
        print("🚀 Directory verification complete! System ready for Story 6.")
    else:
        print("⚠️ Verification completed with warnings. Please review the logs above.")
    print("=" * 60)