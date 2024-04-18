import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage)
import database_utils as dbUtils
from Prompt import Prompt
from Model import Model
from message_helper import MessageHelper as messagehelper


load_dotenv()

open_ai_key = os.getenv("OPEN_AI_KEY")
chat = ChatOpenAI(
    openai_api_key = open_ai_key,
    model = Model.GPT4.value
)


def answer_question(user_question, user_phoneno):
    user_id = None
    messages = []
    messages.append(SystemMessage(content=Prompt.MAIN_PROMPT.value))
    dbHistory = dbUtils.getMessageHistory(user_phoneno)

    if not dbHistory:
        #Creating new user
        user_id = dbUtils.add_new_user(user_phoneno)
    else:
        messages.extend(dbHistory)
        user_id = dbUtils.getUserId(user_phoneno)
    
    messages.append(HumanMessage(content=user_question))

    response = chat.invoke(messages)
    
    updateDB(user_question, user_id, response)

    return response.content

def updateDB(user_question, user_id, response):
    dbUtils.update_db_conversation(user_id=user_id, type=messagehelper.HUMAN.value,convo=user_question )
    dbUtils.update_db_conversation(user_id=user_id, type=messagehelper.AI.value,convo=response.content )

    
