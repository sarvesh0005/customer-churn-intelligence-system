from src.inference.predictor import ChurnPredictor


def main():

    predictor = ChurnPredictor()

    print("=" * 60)
    print(predictor.get_model_info())
    print("=" * 60)


if __name__ == "__main__":
    main()