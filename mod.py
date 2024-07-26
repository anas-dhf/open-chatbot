YOUR_API_KEY = "please insert API key here."

from langchain_google_genai import ChatGoogleGenerativeAI

print("Welcome to Open-Chatbot using GenAI Technology! How can I assist you today?")

#modified prompt
modified_prompt = f"""
Objective:  

User query: {{user_input}}

Style: 

Boundaries: 
"""

def generate_response(prompt):
  """Sends a prompt to the Gemini API and returns the generated response"""
  try:
    genai_model = ChatGoogleGenerativeAI(model="gemini-pro", api_key=YOUR_API_KEY)
    final_prompt = modified_prompt.format(user_input=prompt)  
    response = genai_model.invoke(final_prompt)
    return response.content.strip()
  except Exception as e:
    print(f"An error occurred: {e}")
    return "Sorry, I encountered an issue. Please try again later."

while True:
  # Get user input
  user_input = input("You: ")
  if user_input.lower() == "quit":
    break

  # Generate response using ChatGoogleGenerativeAI with modified prompt
  response = generate_response(prompt=user_input)
  print(f"MOD-OCB: {response}")

print("Thank you for chatting!")
