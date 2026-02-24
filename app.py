import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Dashboard", layout="wide")
st.title("📊 Simple CSV Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview")
    st.dataframe(df, use_container_width=True)

    st.subheader("Filters")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        col = st.selectbox("Choose a numeric column to filter", numeric_cols)
        min_val, max_val = float(df[col].min()), float(df[col].max())
        low, high = st.slider("Select range", min_val, max_val, (min_val, max_val))
        filtered = df[df[col].between(low, high)]
    else:
        st.info("No numeric columns found. Showing full dataset.")
        filtered = df

    st.subheader("Filtered Data")
    st.write(f"Rows: {len(filtered)}")
    st.dataframe(filtered, use_container_width=True)

    st.subheader("Charts")
    if numeric_cols:
        st.bar_chart(filtered[col])
        st.line_chart(filtered[col])
    else:
        st.info("Upload a CSV with at least one numeric column to see charts.")
else:
    st.caption("Upload a CSV file to begin.")