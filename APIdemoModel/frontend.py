import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

# Page config
st.set_page_config(page_title="Insurance Predictor", page_icon="💡", layout="centered")

st.title("💡 Insurance Premium Predictor")
st.markdown("Fill in your details to get your premium category prediction")

# --- Input Form ---
with st.form("user_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=119, value=25)
        weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
        smoker = st.selectbox("Smoker", [True, False])

    with col2:
        height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
        income_lpa = st.number_input("Income (LPA)", min_value=0.1, value=10.0)
        occupation = st.selectbox(
            "Occupation",
            ['retired', 'freelancer', 'student', 'government_job',
             'business_owner', 'unemployed', 'private_job']
        )

    city = st.text_input("City", value="Mumbai")

    submit = st.form_submit_button("🚀 Predict")

# --- Prediction ---
if submit:
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city.title(),  # 🔥 fix case issue
        "occupation": occupation
    }

    with st.spinner("⏳ Predicting..."):
        try:
            response = requests.post(API_URL, json=input_data)

            if response.status_code == 200:
                result = response.json()

                prediction = result.get("predicted_category", "N/A")

                st.success("✅ Prediction Successful!")

                st.markdown(f"""
                ### 🧾 Result
                **Predicted Category:** `{prediction}`
                """)

                # Optional: show input summary
                with st.expander("🔍 View Input Details"):
                    st.json(input_data)

            else:
                st.error(f"❌ API Error: {response.status_code}")
                st.json(response.json())

        except requests.exceptions.ConnectionError:
            st.error("🚫 Could not connect to FastAPI server. Is it running?")









