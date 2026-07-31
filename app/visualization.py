import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_visualization(df):

    st.header("📈 Data Visualization Dashboard")

    # ---------------- BMI vs Calories ---------------- #

    st.subheader("BMI vs Calories Burned")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(
        data=df,
        x="BMI",
        y="Calories_Burned",
        hue="Gender",
        ax=ax
    )
    st.pyplot(fig)

    # ---------------- Steps vs Calories ---------------- #

    st.subheader("Steps vs Calories Burned")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(
        data=df,
        x="Steps",
        y="Calories_Burned",
        ax=ax
    )
    st.pyplot(fig)

    # ---------------- Sleep Hours ---------------- #

    st.subheader("Sleep Hours Distribution")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df["Sleep_Hours"], kde=True, ax=ax)
    st.pyplot(fig)

    # ---------------- Exercise Minutes ---------------- #

    st.subheader("Exercise Minutes Distribution")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df["Exercise_Minutes"], kde=True, ax=ax)
    st.pyplot(fig)

    # ---------------- Heart Rate Box Plot ---------------- #

    st.subheader("Heart Rate Box Plot")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(
        y=df["Heart_Rate"],
        ax=ax
    )
    st.pyplot(fig)

    # ---------------- Calories by Gender ---------------- #

    st.subheader("Average Calories Burned by Gender")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(
        data=df,
        x="Gender",
        y="Calories_Burned",
        ax=ax
    )
    st.pyplot(fig)

    # ---------------- Average Steps ---------------- #

    st.subheader("Average Steps by Gender")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(
        data=df,
        x="Gender",
        y="Steps",
        ax=ax
    )
    st.pyplot(fig)

    # ---------------- Correlation Heatmap ---------------- #

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(10,7))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="viridis",
        ax=ax
    )

    st.pyplot(fig)