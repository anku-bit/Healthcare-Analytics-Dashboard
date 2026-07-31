import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def show_prediction(df):

    st.header("🎯 Calories Burned Prediction")

    # Features
    X = df[
        [
            "Age",
            "Height_cm",
            "Weight_kg",
            "BMI",
            "Heart_Rate",
            "Steps",
            "Exercise_Minutes",
            "Sleep_Hours"
        ]
    ]

    # Target
    y = df["Calories_Burned"]

    # Train Model
    model = LinearRegression()
    model.fit(X, y)

    st.subheader("Enter Patient Details")

    age = st.number_input("Age", 1, 100, 25)
    height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
    weight = st.number_input("Weight (kg)", 20.0, 200.0, 70.0)
    bmi = st.number_input("BMI", 10.0, 50.0, 24.0)
    heart_rate = st.number_input("Heart Rate", 40, 200, 75)
    steps = st.number_input("Steps", 0, 50000, 8000)
    exercise = st.number_input("Exercise Minutes", 0, 300, 45)
    sleep = st.number_input("Sleep Hours", 0.0, 15.0, 7.5)

    if st.button("Predict Calories Burned"):

        input_data = pd.DataFrame(
            [[
                age,
                height,
                weight,
                bmi,
                heart_rate,
                steps,
                exercise,
                sleep
            ]],
            columns=[
                "Age",
                "Height_cm",
                "Weight_kg",
                "BMI",
                "Heart_Rate",
                "Steps",
                "Exercise_Minutes",
                "Sleep_Hours"
            ]
        )

        prediction = model.predict(input_data)[0]

        st.success(f"🔥 Estimated Calories Burned: {prediction:.2f} kcal")