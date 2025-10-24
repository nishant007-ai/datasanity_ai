def generate_report(df):
    report = "📊 DATA REPORT\n"
    report += f"Rows: {df.shape[0]} | Columns: {df.shape[1]}\n\n"

    report += "Missing Values (%):\n"
    report += str(df.isnull().mean() * 100)
    report += "\n\nColumn Types:\n"
    report += str(df.dtypes)
    return report
