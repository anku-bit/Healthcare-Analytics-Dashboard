import streamlit as st

def show_home(df):

    st.header("\U0001F3E0 Home Dashboard")

    st.write("Welcome to Healthcare Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("\U0001F468 Total Patients", len(df))

    with col2:
        st.metric("\U00002696 Average BMI", round(df["BMI"].mean(),2))

    with col3:
        st.metric("\U00002764️ Average Heart Rate", round(df["Heart_Rate"].mean(),2))

    col4, col5 = st.columns(2)

    with col4:
        st.metric("\U0001F463 Average Steps", int(df["Steps"].mean()))

    with col5:
        st.metric("\U0001F525 Average Calories Burned", int(df["Calories_Burned"].mean()))

    st.success("Dataset Loaded Successfully \u2705")