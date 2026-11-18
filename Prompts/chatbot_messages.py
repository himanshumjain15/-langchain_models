from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model = "gpt-5.5")
chat_history = [
    SystemMessage(content = "Yor are an helpful AI Assistant")
]

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content = user_input)) ## add the users messgages directly in the chat history so that it has context
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content)) ## Add the result of the previous conversation into the chat history as well
    print("AI:",result.content)

print(chat_history)