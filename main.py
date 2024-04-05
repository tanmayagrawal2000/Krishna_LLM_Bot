import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

from Prompt import Prompt
from Model import Model


load_dotenv()
open_ai_key = os.getenv("OPEN_AI_KEY")
chat = ChatOpenAI(
    openai_api_key = open_ai_key,
    model = Model.GPT4_PREVIEW.value
)

messages = []
messages.append(SystemMessage(content=Prompt.MAIN_PROMPT.value))

def answer_question(user_question):
    global gpt_tokens, prompt_tokens, total_tokens
    messages.append(HumanMessage(content=user_question))
    response = chat.invoke(messages)
    gpt_tokens += response.response_metadata['token_usage']['completion_tokens']
    prompt_tokens += response.response_metadata['token_usage']['prompt_tokens']
    total_tokens += response.response_metadata['token_usage']['total_tokens']
    messages.append(AIMessage(content=response.content))
    # print(f"gpt_token: {response.response_metadata['token_usage']['completion_tokens']}")
    # print(f"prompt: {response.response_metadata['token_usage']['prompt_tokens']}")
    # print(f"Total tokens: {response.response_metadata['token_usage']['total_tokens']}")
    return response.content


print("Welcome to the Krishna Chatbot!")

gpt_tokens = 0
prompt_tokens = 0
total_tokens = 0

while True:
    user_question = input("\nYou: ")
    if user_question.lower() == "quit":
        print(f"Final completions tokens : {gpt_tokens}")
        print(f"Final prompt tokens : {prompt_tokens}")
        print(f"Overall tokens : {total_tokens}")
        break
    response = answer_question(user_question)
    print(f"Krishna: {response}")


