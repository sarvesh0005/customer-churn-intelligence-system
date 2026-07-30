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
