Insurance Premium Predictor (FastAPI + ML)

This project is an end-to-end machine learning API that predicts a user's insurance premium category based on personal, lifestyle, and financial data.

The backend is built using FastAPI and integrates a trained machine learning model to provide real-time predictions. The project demonstrates how to deploy ML models in a backend system with proper API design.

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
API Documentation
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Tech Stack
FastAPI
Pydantic
Scikit-learn
Pandas
Streamlit
Run Locally
Backend
uvicorn main:app --reload
Frontend
streamlit run app.py
Purpose

This project demonstrates:

Building REST APIs using FastAPI
Integrating machine learning models into backend systems
Performing feature engineering at runtime
Creating a simple interactive frontend
Future Improvements
Add prediction confidence scores
Integrate caching (e.g., Redis)
Deploy using Docker and cloud platforms
Improve model performance and preprocessing pipeline
Author

Created as a practice project to demonstrate machine learning and backend development skills.
