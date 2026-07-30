# Customer Churn Intelligence System

This project predicts whether a telecom customer is likely to leave the service and provides a business recommendation based on the predicted risk.

This project is built as an end-to-end machine learning application instead of just a trained model. It includes data preprocessing, model training, a FastAPI backend, Docker support, and deployment on Render, making the model accessible through a REST API.
## Live Demo

- **API:** https://customer-churn-intelligence-system.onrender.com
- **Swagger UI:** https://customer-churn-intelligence-system.onrender.com/docs

## Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses because losing existing customers is often more expensive than acquiring new ones. Predicting which customers are likely to leave allows companies to take proactive retention actions.

The goal of this project was not only to train a machine learning model but also to build a complete inference system that can be deployed and used in a production-like environment. The application accepts customer information through a REST API, processes the input using the same preprocessing pipeline used during training, predicts the probability of churn, and returns both the prediction and a business recommendation based on the customer's risk level.

The project follows a modular structure with separate components for preprocessing, prediction, API services, configuration management, and deployment.

## Key Features

- Predicts customer churn using an XGBoost classification model.
- Uses a saved preprocessing pipeline to ensure consistent predictions.
- Provides business recommendations based on predicted churn risk.
- Exposes predictions through a FastAPI REST API.
- Validates requests using Pydantic models.
- Containerized with Docker for consistent deployment.
- Deployed on Render with interactive Swagger API documentation.
- Organized using a modular and production-oriented project structure.

## System Architecture


<p align="center">
  <img src="docs/images/archi.png" alt="System Architecture" width="900">
</p>

## Project Structure

```text
customer-churn-intelligence-system/
│
├── configs/                 # Configuration files
├── docs/
│   └── images/              # README images
├── logs/                    # Application logs
├── models/                  # Trained model artifacts
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── feature_columns.json
│   └── metrics.json
├── notebooks/               # Model development and experiments
├── src/
│   ├── api/
│   ├── config/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | XGBoost, Scikit-learn |
| Data Processing | Pandas, NumPy |
| API Framework | FastAPI |
| Validation | Pydantic |
| Deployment | Docker, Render |
| Documentation | Swagger UI |
| Version Control | Git, GitHub |

## Machine Learning Pipeline

The prediction workflow follows the same preprocessing steps used during model training to ensure consistent results during inference.

```text
Customer Data
      │
      ▼
Input Validation (Pydantic)
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Transformation
      │
      ▼
XGBoost Model
      │
      ▼
Churn Probability
      │
      ▼
Risk Assessment
      │
      ▼
Business Recommendation
      │
      ▼
JSON Response
```

### Prediction Workflow

1. The client sends customer information to the `/predict` endpoint.
2. FastAPI validates the request using Pydantic models.
3. The saved preprocessing pipeline transforms the input features.
4. The processed data is passed to the trained XGBoost model.
5. The predicted probability is converted into a churn risk level.
6. A business recommendation is generated based on the predicted risk.
7. The API returns the prediction, confidence score, risk level, and recommended action.

## Screenshots

### API Documentation

The application provides interactive API documentation using Swagger UI, making it easy to test endpoints and understand request and response formats.

<p align="center">
  <img src="docs/images/swegger.png" alt="Swagger UI" width="900">
</p>

---

### Prediction Response

Example prediction returned by the API after processing customer information.

<p align="center">
  <img src="docs/images/prediction.png" alt="Prediction Response" width="900">
</p>

---

### Project Repository

Repository structure showing the modular organization of the project.

<p align="center">
  <img src="docs/images/github.png" alt="GitHub Repository" width="900">
</p>

---

### Cloud Deployment

Application successfully deployed on Render.

<p align="center">
  <img src="docs/images/rander.png" alt="Render Deployment" width="900">
</p>
