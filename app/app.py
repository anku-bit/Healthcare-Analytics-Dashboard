import streamlit as st
import pandas as pd
from home import show_home
from upload import show_upload
from cleaning import show_cleaning
from eda import show_eda
from visualization import show_visualization
from machine_learning import show_machine_learning
from prediction import show_prediction
from report import show_report

st.set_page_config(
    page_title="Healthcare Analytics Dashboard",
    page_icon="\U0001F3E5",
    layout="wide"
)

st.title("\U0001F3E5 Healthcare Analytics Dashboard")
st.write("Welcome to Healthcare Analytics Dashboard")
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "Upload Dataset",
        "Data Cleaning",
        "EDA",
        "Visualization",
        "Machine Learning",
        "Prediction",
        "Report"
    ]
)

try:
    df = pd.read_csv("dataset/healthcare_dataset.csv")
except:
    df = None
if df is None:
    st.error("\u274C Dataset Not Found!")
    st.stop()

if option == "Home":
    show_home(df)

elif option == "Upload Dataset":
    show_upload(df)

elif option == "Data Cleaning":
    show_cleaning(df)

elif option == "EDA":
    show_eda(df)

elif option == "Visualization":
    show_visualization(df)

elif option == "Machine Learning":
    show_machine_learning(df)

elif option == "Prediction":
    show_prediction(df)


elif option == "Report":
    show_report(df)