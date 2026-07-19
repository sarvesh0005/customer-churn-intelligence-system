"""
input_validator.py

Validates customer input before sending it to the ML model.
"""

from typing import List

import pandas as pd

from src.utils.exceptions import InvalidInputDataError
from src.utils.logger import get_logger

logger = get_logger(__name__)


class InputValidator:
    """
    Validate customer input data.
    """

    def __init__(self, expected_columns: List[str]) -> None:
        self.expected_columns = expected_columns

    def validate(self, customer_data: pd.DataFrame) -> None:
        """
        Validate the customer input.
        """

        self._validate_dataframe(customer_data)
        self._validate_empty(customer_data)
        self._validate_columns(customer_data)

        logger.info("Input validation successful.")

    # ======================================================
    # Private Methods
    # ======================================================

    def _validate_dataframe(self, customer_data: pd.DataFrame) -> None:

        if not isinstance(customer_data, pd.DataFrame):
            raise InvalidInputDataError(
                "Input must be a pandas DataFrame."
            )

    def _validate_empty(self, customer_data: pd.DataFrame) -> None:

        if customer_data.empty:
            raise InvalidInputDataError(
                "Input DataFrame is empty."
            )

    def _validate_columns(self, customer_data: pd.DataFrame) -> None:

        received_columns = list(customer_data.columns)

        missing_columns = list(
            set(self.expected_columns) - set(received_columns)
        )

        extra_columns = list(
            set(received_columns) - set(self.expected_columns)
        )

        if missing_columns:

            raise InvalidInputDataError(
                f"Missing columns: {missing_columns}"
            )

        if extra_columns:

            raise InvalidInputDataError(
                f"Unexpected columns: {extra_columns}"
            )