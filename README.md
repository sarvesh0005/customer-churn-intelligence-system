# Customer Churn Intelligence System

Production-ready Machine Learning system for predicting customer churn and generating actionable retention recommendations through a REST API.

---

## Overview

Customer churn is one of the most important business challenges for subscription-based companies. This project demonstrates how a machine learning model can be transformed into a deployable inference service using production-oriented software engineering practices.

The system performs:

- Customer churn prediction
- Business risk assessment
- Automated retention recommendations
- REST API inference using FastAPI
- Input validation before prediction
- Modular service-oriented architecture

---

## Features

- End-to-end ML inference pipeline
- Modular project architecture
- Input schema validation
- Business recommendation engine
- FastAPI REST API
- Interactive Swagger documentation
- Centralized logging
- Custom exception handling
- Reusable service layer

---

## Tech Stack

### Machine Learning

- Python
- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Software Engineering

- Modular Architecture
- Service Layer Pattern
- Logging
- Exception Handling
- Git

---

## Project Structure

```text
customer-churn-intelligence-system/
│
├── configs/
├── data/
├── docs/
├── logs/
├── models/
├── notebooks/
├── src/
│   ├── api/
│   ├── config/
│   ├── inference/
│   ├── loaders/
│   ├── recommendations/
│   ├── services/
│   ├── utils/
│   └── validators/
│
├── tests/
├── requirements.txt
└── README.md
```

---

## System Architecture

```text
                   Client
                      │
                      ▼
               FastAPI REST API
                      │
                      ▼
              Prediction Service
                      │
                      ▼
              Churn Predictor
             /                \
            ▼                  ▼
   Input Validator   Recommendation Engine
            │
            ▼
     Trained ML Pipeline
            │
            ▼
      Prediction Response
```

---

## Workflow

1. Receive customer information through REST API.
2. Validate request schema.
3. Load trained model artifacts.
4. Predict churn probability.
5. Estimate business risk.
6. Generate retention recommendation.
7. Return structured JSON response.

---

## API Endpoints

### Health Check

```
GET /health
```

---

### Predict Customer Churn

```
POST /predict
```

Example Request

```json
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
  "MonthlyCharges": 89.1,
  "TotalCharges": 89.1
}
```

Example Response

```json
{
  "status": "success",
  "data": {
    "prediction": "Yes",
    "probability": 0.9142,
    "confidence": 91.42,
    "risk_level": "High",
    "priority": "Immediate",
    "recommended_action": "Assign retention specialist, offer premium discount, and contact customer within 24 hours."
  }
}
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn src.api.app:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements

- Docker deployment
- Batch inference pipeline
- Streamlit dashboard
- MLflow experiment tracking
- Automated testing with Pytest
- CI/CD using GitHub Actions
- Cloud deployment

---

## Learning Outcomes

This project demonstrates practical experience with:

- Production ML inference
- API development using FastAPI
- Service-oriented architecture
- Machine learning deployment
- Input validation
- Business logic integration
- Modular Python application design
