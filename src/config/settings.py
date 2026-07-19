"""
settings.py

Centralized project configuration.

This module stores project-wide paths so that every module
uses the same configuration instead of hardcoded paths.
"""

from pathlib import Path

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# Directories
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = PROJECT_ROOT / "models"

CONFIG_DIR = PROJECT_ROOT / "configs"

LOG_DIR = PROJECT_ROOT / "logs"

DOCS_DIR = PROJECT_ROOT / "docs"

TESTS_DIR = PROJECT_ROOT / "tests"

# ==========================================================
# Log File
# ==========================================================

LOG_FILE = LOG_DIR / "app.log"

# ==========================================================
# Ensure Required Directories Exist
# ==========================================================

LOG_DIR.mkdir(exist_ok=True)