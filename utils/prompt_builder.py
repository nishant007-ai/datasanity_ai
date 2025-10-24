def build_prompt(csv_preview, user_command):
    return f"""
Here is a sample of my dataset:
{csv_preview}

Please write Python code using pandas to:
{user_command}

Make sure your final dataframe is named 'df'.
Return only code, no explanation.
"""

