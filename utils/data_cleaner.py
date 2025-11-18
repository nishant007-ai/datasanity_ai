import pandas as pd
import ollama  # ✅ new import
from utils.prompt_builder import build_prompt

def clean_data(df, command):
    prompt = build_prompt(df.head().to_csv(), command)

    # ✅ Call Ollama instead of OpenAI
    response = ollama.chat(
        model="llama3",  # or "mistral", "codellama", etc.
   