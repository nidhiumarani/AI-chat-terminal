import os
from dotenv import load_dotenv
from groq import Groq

# Load the dotenv file to read the .env file
load_dotenv()

# read the API key which is stored in .env file
api_key = os.getenv("GROQ_API_KEY")

# creating a groq client
client = Groq(api_key=api_key)

# get the user input
while True: 
    user_input = input('Please type your question (you can always type EXIT to get out of the conversation) \n')
    
    # check if user has typed exit if not only then call the LLM
    if(user_input.lower() == "exit"):
        break

    # call the LLM API (Structure is specific for calling LLM api's)
    response = client.chat.completions.create ( 
        model = "llama-3.1-8b-instant",
        messages = [
            {"role" : "system", "content": "You are a great coder and always talk in coding language no matter what the question is "},
            {"role": "user", "content": user_input}
        ]
    )

    # print the LLM respose
    llm_answer = response.choices[0].message.content
    print(llm_answer)