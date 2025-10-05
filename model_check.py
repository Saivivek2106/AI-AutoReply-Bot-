import google.generativeai as genai

# --- Paste your Gemini API key here ---
GEMINI_API_KEY = "AIzaSyBpLsfUzeUl1wwUAepfpda7aNt9B2lY8us"

try:
    genai.configure(api_key=GEMINI_API_KEY)

    print("Successfully configured API key. Fetching available models...")
    print("-" * 30)

    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"Model Name: {model.name}")
            print(f"   Supported Methods: {model.supported_generation_methods}\n")

except Exception as e:
    print(f"An error occurred: {e}")
    print("\nPlease ensure your API key is correct and that you have enabled the 'Generative Language API' in your Google Cloud project.")