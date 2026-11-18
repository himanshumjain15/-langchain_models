from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-5.5")

while True:
    user_input = input("You:")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI:",result.content)

    ## This does not have any idea or cocept of memory it does not remember the previous context because we have not added that in our code we need to create chat history