import streamlit as st
import pandas as pd
from utils.data_cleaner import clean_data
from utils.report_gen import generate_report

st.set_page_config(page_title="DataSanity AI", layout="wide")
st.title("📊 DataSanity AI – Clean, Explain, Automate")

uploaded_file = st.file_uploader("📤 Upload your CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    st.subheader("📁 Raw Data Preview")
    st.dataframe(df.head())

    user_command = st.text_area("🧠 Enter your data cleaning instruction (e.g., 'Drop nulls, rename columns, detect outliers')")

    if st.button("🚀 Clean & Generate Report"):
        cleaned_df, code_used = clean_data(df, user_command)
    