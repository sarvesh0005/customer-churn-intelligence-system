"""
recommendation_engine.py

Business recommendation engine for customer churn predictions.
"""

from src.utils.logger import get_logger

logger = get_logger(__name__)


class RecommendationEngine:
    """
    Generate business recommendations based on churn probability.
    """

    def generate(self, probability: float) -> dict:
        """
        Generate recommendation for a customer.

        Parameters
        ----------
        probability : float

        Returns
        -------
        dict
        """

        if probability >= 0.80:

            return {
                "risk_level": "High",
                "priority": "Immediate",
                "recommended_action": (
                    "Assign retention specialist, "
                    "offer premium discount, and contact customer within 24 hours."
                ),
            }

        elif probability >= 0.50:

            return {
                "risk_level": "Medium",
                "priority": "High",
                "recommended_action": (
                    "Offer promotional plan, "
                    "send personalized retention email, and monitor activity."
                ),
            }

        else:

            return {
                "risk_level": "Low",
                "priority": "Normal",
                "recommended_action": (
                    "No immediate intervention required. "
                    "Continue regular engagement."
                ),
            }