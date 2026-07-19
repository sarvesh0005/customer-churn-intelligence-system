"""
exceptions.py

Custom exceptions used throughout the project.
"""


class ArtifactNotFoundError(FileNotFoundError):
    """
    Raised when a required artifact file is missing.
    """

    pass


class InvalidInputDataError(ValueError):
    """
    Raised when prediction input data is invalid.
    """

    pass


class PredictionError(Exception):
    """
    Raised when prediction fails.
    """

    pass


class ConfigurationError(Exception):
    """
    Raised when project configuration is invalid.
    """

    pass