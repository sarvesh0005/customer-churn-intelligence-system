import pandas as pd

from src.inference.predictor import ChurnPredictor


def main():

    predictor = ChurnPredictor()

    customer = pd.DataFrame(
        [
            {
                "gender": "Female",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "Dependents": "No",
                "tenure": 1,
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "Fiber optic",
                "OnlineSecurity": "No",
                "OnlineBackup": "No",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "Yes",
                "StreamingMovies": "Yes",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 89.10,
                "TotalCharges": 89.10,
            }
        ]
    )

    result = predictor.predict(customer)

    print("\nPrediction Result")
    print("-" * 50)
    print(result)


if __name__ == "__main__":
    main()