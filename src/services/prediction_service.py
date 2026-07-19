"""
prediction_service.py

Service layer responsible for orchestrating the complete
customer churn prediction workflow.
"""

import pandas as pd

from src.inference.predictor import ChurnPredictor
from src.utils.exceptions import (
    InvalidInputDataError,
    PredictionError,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)


class PredictionService:
    """
    Service responsible for executing the complete
    prediction workflow.
    """

    def __init__(self):

        logger.info("Initializing Prediction Service...")

        self.predictor = ChurnPredictor()

        logger.info("Prediction Service initialized successfully.")

    def predict(self, customer_data: pd.DataFrame) -> dict:
        """
        Execute end-to-end prediction workflow.
        """

        try:

            logger.info("Starting prediction workflow.")

            result = self.predictor.predict(customer_data)

            logger.info("Prediction workflow completed successfully.")

            return {
                "status": "success",
                "data": result
            }

        except InvalidInputDataError as e:

            logger.error(f"Input validation failed: {e}")

            raise

        except Exception as e:

            logger.exception("Prediction workflow failed.")

            raise PredictionError(
                f"Prediction failed: {str(e)}"
            )