import openai

# Set up your OpenAI API credentials
openai.api_key = 'YOUR_API'

# Function to interact with the chatbot
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
