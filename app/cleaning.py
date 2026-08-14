import streamlit as st

def show_cleaning(df):

    st.header("\U0001F9F9 Data Cleaning")

    col1,col2=st.columns(2)

    with col1:
        st.metric("Rows",df.shape[0])

    with col2:
        st.metric("Columns",df.shape[1])

    st.subheader("Missing Values")

    st.dataframe(df.isnull().sum())

    st.subheader("Duplicate Records")

    st.metric("Duplicates",df.duplicated().sum())

    st.subheader("Statistics")

    st.dataframe(df.describe())

    if st.button("Remove Duplicates"):
        df=df.drop_duplicates()
        st.success("Duplicates Removed Successfully")