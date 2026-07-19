"""
Simple test for ArtifactLoader.
"""

from src.loaders.artifact_loader import ArtifactLoader


def main():

    loader = ArtifactLoader()

    print("=" * 60)

    print(type(loader.model))
    print(type(loader.preprocessor))
    print(type(loader.metrics))
    print(type(loader.feature_metadata))

    print("=" * 60)

    print(loader.metrics.keys())
    print(loader.feature_metadata.keys())


if __name__ == "__main__":
    main()