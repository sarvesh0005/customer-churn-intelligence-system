"""
settings.py

Centralized project configuration.

Loads environment variables from a .env file and exposes
project-wide paths and application settings.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# Application Configuration
# ==========================================================

APP_NAME = os.getenv("APP_NAME", "Customer Churn Prediction API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ==========================================================
# Project Directories
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = PROJECT_ROOT / os.getenv("MODELS_DIR", "models")

CONFIG_DIR = PROJECT_ROOT / os.getenv("CONFIG_DIR", "configs")

LOG_DIR = PROJECT_ROOT / os.getenv("LOG_DIR", "logs")

DOCS_DIR = PROJECT_ROOT / "docs"

TESTS_DIR = PROJECT_ROOT / "tests"

# ==========================================================
# Log File
# ==========================================================

LOG_FILE = LOG_DIR / "app.log"

# ==========================================================
# Ensure Required Directories Exist
# ==========================================================

LOG_DIR.mkdir(parents=True, exist_ok=True)