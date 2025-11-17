import streamlit as st
import pandas as pd
from utils.data_cleaner import clean_data
from utils.report_gen import generate_report

st.set_page_config(page_title="DataSanity AI", layout="wide")
st.title("📊 DataSanity AI – Clean, Explain, Automate")

uploaded_file = st.file_uploader("📤 Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        data = pd.read_excel(uploaded_file)
    
    st.subheader("📊 Data Preview")
    st.dataframe(data.head())

    if st.button("🧹 Clean Data"):
        cleaned_data = clean_data(data)
        st.subheader("✅ Cleaned Data")
        st.dataframe(cleaned_data)

        if st.button("📄 Generate Report"):
            report = generate_report(cleaned_data)
            st.subheader("📑 Generated Report")
            st.text(report)
else:
    st.info("Please upload a CSV or Excel file to get started.")        