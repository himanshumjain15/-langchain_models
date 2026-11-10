from langchain_openai import ChatOpenAI
from dotenv import load_dotenv ## load secert keys from the env invrioenmt to the current environemnt

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4.1-mini"
)

## .invoke is used to communicate with the gpt / any llm model 
result = llm.invoke("What is the capital of India ? ")

print(result.content)