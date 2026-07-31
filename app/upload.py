import streamlit as st

def show_upload(df):

    st.header("📂 Upload Dataset")

    st.dataframe(df.head(10), width="stretch")

    col1,col2 = st.columns(2)

    with col1:
        st.metric("Rows",df.shape[0])

    with col2:
        st.metric("Columns",df.shape[1])

    st.subheader("Column Names")

    st.write(df.columns.tolist())

    st.subheader("Data Types")

    st.dataframe(df.dtypes.astype(str))
    