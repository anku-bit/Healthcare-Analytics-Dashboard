import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_eda(df):

    st.header("📊 Exploratory Data Analysis")

    # Age Distribution
    st.subheader("Age Distribution")
    fig, ax = plt.subplots(figsize=(8,5))
    ax.hist(df["Age"], bins=10)
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Gender Distribution
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots(figsize=(5,5))
    df["Gender"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )
    ax.set_ylabel("")
    st.pyplot(fig)

    # BMI Distribution
    st.subheader("BMI Distribution")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df["BMI"], kde=True, ax=ax)
    st.pyplot(fig)

    # Heart Rate Distribution
    st.subheader("Heart Rate Distribution")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df["Heart_Rate"], kde=True, ax=ax)
    st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10,7))
    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax
    )
    st.pyplot(fig)