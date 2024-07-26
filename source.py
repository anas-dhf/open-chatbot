YOUR_API_KEY = "replace this text with your api key from google"

from langchain_google_genai import ChatGoogleGenerativeAI

print("Welcome to Open-Chatbot using GenAI Technology! How can I assist you today?")

def generate_response(prompt):
  """Sends a prompt to the Gemini API and returns the generated response."""
  try:
    genai_model = ChatGoogleGenerativeAI(model="gemini-pro", api_key=YOUR_API_KEY)
    response = genai_model.invoke(prompt)
    return response.content.strip()
  except Exception as e:
    print(f"An error occurred: {e}")
    return "Sorry, I encountered an issue. Please try again later."

while True:
  #input
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break

  #output
  response = generate_response(prompt=user_input)
  print(f"OCB: {response}")

print("Thank you for chatting!")
