from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions= 300
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about Virat Kolhi"

doc_embeddings = embedding.embed_documents(documents) ## 5 vectors each in 300 dimension space , document embeddings
query_embeddings = embedding.embed_query(query) ## 1 vector with 300 dimension , query embeddings 

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]  ## always pass it as a 2D list , [0] brings the first row from thr 2d list

index, score = sorted(list(enumerate(scores)), key = lambda x :x[1])[-1] ## sorting and indexing to get the document ith the highest score

print(query)
print(documents[index])
print("The Score is :", score)