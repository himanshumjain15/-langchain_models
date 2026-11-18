from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-5.5")
chat_history = []

while True:
    user_input = input("You:")
    chat_history.append(user_input) ## add the users messgages directly in the chat history so that it has context
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content) ## Add the result of the previous conversation into the chat history as well
    print("AI:",result.content)

print(chat_history)

## Even this chatbot not perfect , we the chat histroy has just messages but not who sent whcih message and it can be a problem when the context gets bigger.