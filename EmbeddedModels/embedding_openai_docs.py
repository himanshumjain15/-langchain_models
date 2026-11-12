from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding  = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions= 32
)
# Generating embeddings for multiple documents
documents = [
    "Delhi is the Capital of India",
    "Paris is the CApital of France",
    "Mumbai id the Captal of Maharashtra"
]
result = embedding.embed_documents(documents)

print(str(result))