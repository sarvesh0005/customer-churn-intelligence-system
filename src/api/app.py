"""
app.py

FastAPI application for Customer Churn Intelligence System.
"""

import pandas as pd
from fastapi import FastAPI, HTTPException

from src.api.schemas import CustomerRequest
from src.config.settings import (
    APP_NAME,
    APP_VERSION,
)
from src.services.prediction_service import PredictionService
from src.utils.exceptions import (
    InvalidInputDataError,
    PredictionError,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title=APP_NAME,
    description="Production-ready Machine Learning API for customer churn prediction.",
    version=APP_VERSION,
)

# ==========================================================
# Initialize Prediction Service
# ==========================================================

prediction_service = PredictionService()


# ==========================================================
# Home Endpoint
# ==========================================================

@app.get("/")
def home():

    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "status": "running",
    }


# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.post("/predict")
def predict(customer: CustomerRequest):

    try:

        customer_df = pd.DataFrame([customer.model_dump()])

        result = prediction_service.predict(customer_df)

        return result

    except InvalidInputDataError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except PredictionError as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    except Exception as e:

        logger.exception("Unexpected server error.")

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )