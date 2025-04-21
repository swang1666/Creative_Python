# 1. Import the Gemini API Python client
import google.generativeai as genai

# 2. Configure your Gemini API key (replace YOUR_API_KEY with your actual key)
genai.configure(api_key="AIzaSyDrEYzyAfCwkVAhoI-UwhS7FVXp6jVQo1o")

# 3. Initialize the model you want to use (Gemini 1.5 Pro is most powerful at the time of writing)
model = genai.GenerativeModel("gemini-1.5-pro")

# 4. Send a prompt to the model (can be a question, instruction, story starter, etc.)
response = model.generate_content("Explain how AI works")

# 5. Print the response text from the model
print(response.text)
