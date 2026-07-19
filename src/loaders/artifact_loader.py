"""
artifact_loader.py

Loads and manages all machine learning artifacts required for inference.

Responsibilities
----------------
- Load model artifacts
- Load preprocessing pipeline
- Load feature metadata
- Load evaluation metrics

This class acts as the single source of truth for accessing
trained artifacts during inference.
"""

from pathlib import Path
from typing import Any

import json
import joblib

from src.config.settings import MODELS_DIR, CONFIG_DIR
from src.utils.exceptions import ArtifactNotFoundError
from src.utils.logger import get_logger

logger = get_logger(__name__)


class ArtifactLoader:
    """
    Loads all machine learning artifacts into memory.
    """

    def __init__(self) -> None:

        self._artifact_paths = {
            "model": MODELS_DIR / "model.pkl",
            "preprocessor": MODELS_DIR / "preprocessor.pkl",
            "metrics": MODELS_DIR / "metrics.json",
            "feature_metadata": CONFIG_DIR / "feature_columns.json",
        }

        self._artifacts: dict[str, Any] = {}

        self._load_artifacts()

    # ---------------------------------------------------------
    # Private Methods
    # ---------------------------------------------------------

    def _load_artifacts(self) -> None:
        """
        Load every required artifact.
        """

        logger.info("Loading machine learning artifacts...")

        self._artifacts["model"] = self._load_joblib(
            self._artifact_paths["model"]
        )

        self._artifacts["preprocessor"] = self._load_joblib(
            self._artifact_paths["preprocessor"]
        )

        self._artifacts["metrics"] = self._load_json(
            self._artifact_paths["metrics"]
        )

        self._artifacts["feature_metadata"] = self._load_json(
            self._artifact_paths["feature_metadata"]
        )

        logger.info("All artifacts loaded successfully.")

    def _load_joblib(self, path: Path) -> Any:
        """
        Load a Joblib artifact.
        """

        if not path.exists():
            logger.error("Artifact not found: %s", path)
            raise ArtifactNotFoundError(f"Missing artifact: {path}")

        logger.info("Loaded %s", path.name)

        return joblib.load(path)

    def _load_json(self, path: Path) -> dict:
        """
        Load a JSON artifact.
        """

        if not path.exists():
            logger.error("Artifact not found: %s", path)
            raise ArtifactNotFoundError(f"Missing artifact: {path}")

        logger.info("Loaded %s", path.name)

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    # ---------------------------------------------------------
    # Public Properties
    # ---------------------------------------------------------

    @property
    def model(self) -> Any:
        return self._artifacts["model"]

    @property
    def preprocessor(self) -> Any:
        return self._artifacts["preprocessor"]

    @property
    def metrics(self) -> dict:
        return self._artifacts["metrics"]

    @property
    def feature_metadata(self) -> dict:
        return self._artifacts["feature_metadata"]