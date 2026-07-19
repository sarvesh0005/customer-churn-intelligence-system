"""
predictor.py

Core prediction engine for the Customer Churn Intelligence System.
"""

import pandas as pd

from src.loaders.artifact_loader import ArtifactLoader
from src.recommendations.recommendation_engine import RecommendationEngine
from src.utils.logger import get_logger
from src.validators.input_validator import InputValidator

logger = get_logger(__name__)


class ChurnPredictor:
    """
    Main inference engine.
    """

    def __init__(self) -> None:

        logger.info("Initializing ChurnPredictor...")

        self.loader = ArtifactLoader()

        self.model = self.loader.model
        self.metrics = self.loader.metrics
        self.feature_metadata = self.loader.feature_metadata

        self.validator = InputValidator(
            self.feature_metadata["raw_input_columns"]
        )

        self.recommendation_engine = RecommendationEngine()

        logger.info("ChurnPredictor initialized successfully.")

    # ======================================================
    # Public Methods
    # ======================================================

    def predict(self, customer_data: pd.DataFrame) -> dict:
        """
        Predict customer churn.
        """

        self.validator.validate(customer_data)

        prediction = int(self.model.predict(customer_data)[0])

        probability = float(
            self.model.predict_proba(customer_data)[0][1]
        )

        recommendation = self.recommendation_engine.generate(probability)

        return {
            "prediction": "Yes" if prediction else "No",
            "probability": round(probability, 4),
            "confidence": round(probability * 100, 2),
            **recommendation,
        }

    def predict_proba(self, customer_data: pd.DataFrame) -> float:

        self.validator.validate(customer_data)

        probability = self.model.predict_proba(customer_data)[0][1]

        return float(probability)

    def get_model_info(self) -> dict:

        return {
            "selected_model": self.metrics.get("selected_model"),
            "cv_roc_auc": self.metrics.get("cv_roc_auc"),
            "model_type": type(self.model).__name__,
        }