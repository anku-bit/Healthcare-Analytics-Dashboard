import streamlit as st

def show_report(df):

    st.header("\U0001F4C4 Healthcare Analytics Report")

    st.subheader("Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Patients", len(df))
        st.metric("Total Columns", df.shape[1])

    with col2:
        st.metric("Average Age", round(df["Age"].mean(), 2))
        st.metric("Average BMI", round(df["BMI"].mean(), 2))

    st.divider()

    st.subheader("Health Statistics")

    st.write(f"**Average Heart Rate:** {round(df['Heart_Rate'].mean(),2)} bpm")
    st.write(f"**Average Steps:** {int(df['Steps'].mean())}")
    st.write(f"**Average Exercise Minutes:** {round(df['Exercise_Minutes'].mean(),2)} min")
    st.write(f"**Average Sleep Hours:** {round(df['Sleep_Hours'].mean(),2)} hrs")
    st.write(f"**Average Calories Burned:** {round(df['Calories_Burned'].mean(),2)} kcal")

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df.head(10), width="stretch")

    st.divider()

    st.subheader("Dataset Description")

    st.dataframe(df.describe(), width="stretch")

    st.success("✅ Report Generated Successfully")