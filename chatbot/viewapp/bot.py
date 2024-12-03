import os
from dotenv import load_dotenv

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat
load_dotenv()

BOT_TOKEN = 'OTdlOWU4ZTAtNDY0Yy00M2MyLTkzN2QtY2YzMzEwYjFhZTBkOmM4NGJjNWZkLTM1MjYtNDRhYy1iODM5LWZlNDNmODA5ZjE4Ng=='

chat = GigaChat(credentials=BOT_TOKEN, verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Ты бот помощник."
    )
]


def chats(messag):
    # Ввод пользователя
    messages.append(HumanMessage(content=messag))
    res = chat(messages)
    messages.append(res)
    print(res.content)
    return res.content
