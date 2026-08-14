import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

def show_machine_learning(df):

    st.header("\U0001F916 Machine Learning")

    st.write("### Linear Regression Model")
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
    y = df["Calories_Burned"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    st.success("✅ Model Trained Successfully")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("R² Score", round(r2, 4))
        st.metric("MAE", round(mae, 2))

    with col2:
        st.metric("MSE", round(mse, 2))
        st.metric("RMSE", round(rmse, 2))

    st.subheader("Feature Importance (Coefficients)")

    feature_df = X.columns.to_frame(index=False, name="Feature")
    feature_df["Coefficient"] = model.coef_

    st.dataframe(feature_df, width="stretch")