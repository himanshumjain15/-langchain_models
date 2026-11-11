from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model_anthropic = ChatAnthropic(
    model = "claude-sonnet-5-5"
    temperature= 0.6
    max_tokens_to_sample= 50
)

result = model_anthropic.invoke("Tell me the differnece between type 1 and type 2 dibetics")

print(result.content)