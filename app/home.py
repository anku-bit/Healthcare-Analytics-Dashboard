import streamlit as st

def show_home(df):

    st.header("🏠 Home Dashboard")

    st.write("Welcome to Healthcare Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👨 Total Patients", len(df))

    with col2:
        st.metric("⚖ Average BMI", round(df["BMI"].mean(),2))

    with col3:
        st.metric("❤️ Average Heart Rate", round(df["Heart_Rate"].mean(),2))

    col4, col5 = st.columns(2)

    with col4:
        st.metric("👣 Average Steps", int(df["Steps"].mean()))

    with col5:
        st.metric("🔥 Average Calories Burned", int(df["Calories_Burned"].mean()))

    st.success("Dataset Loaded Successfully ✅")