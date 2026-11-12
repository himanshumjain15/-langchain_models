from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override = True)

model = ChatOpenAI(
    model = "gpt-5.5",
    temperature = 0.7, ## higher temperature means more creative responses 
    max_completion_tokens= 50
)

result = model.invoke("Suggest me 5 Indian male names/")

print(result.content)