from enum import Enum, auto
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

class MessageHelper(Enum):

    AI = "A"

    HUMAN = "U"

    def transformConversation(message):
        type, convo = message
        if type == MessageHelper.AI.value:
            return AIMessage(content=convo)
        
        elif type == MessageHelper.HUMAN.value:
            return HumanMessage(content=convo)