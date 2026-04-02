Insurance Premium Predictor (FastAPI + ML)
PS- (This project is not live for now and just a dummy practice project)
This project is an end-to-end machine learning API that predicts a user's insurance premium category based on personal, lifestyle, and financial data.

The backend is built using FastAPI and integrates a trained machine learning model to provide real-time predictions. The project demonstrates how to deploy ML models in a backend system with proper API design.

Features
FastAPI backend for building REST APIs
Machine learning model integration
Feature engineering (BMI, lifestyle risk, age group, city tier)
Automatic API documentation (Swagger UI and ReDoc)
Streamlit-based frontend interface
Clean and modular structure
How It Works
The user provides inputs such as age, height, weight, income, occupation, and city
The backend computes derived features like BMI, lifestyle risk, and age group
The processed data is passed to the trained ML model
The model predicts the insurance premium category
The result is returned via API and displayed on the frontend
API Endpoint
POST /predict
Request Body:
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
Response:
{
  "predicted_category": "low"
}
