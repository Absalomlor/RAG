import chromadb
import pandas as pd
from chromadb.utils import embedding_functions
import pythainlp
import pythainlp.util
from pythainlp import word_tokenize
from dotenv import load_dotenv
import os

os.environ["PYTHAINLP_DATA_DIR"] = "/app/pythainlp-data"

load_dotenv()

data = pd.read_excel('Jobdb.xlsx')
data["Description"] = data["Description"].fillna(data["Job"])

job_ids = data.index.to_list()
job_names = data['Job'].tolist()
documents = data['Description'].str.replace('\n', '').tolist()

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction("paraphrase-multilingual-mpnet-base-v2", normalize_embeddings=True)
client = chromadb.PersistentClient(path="Database")
COLLECTION_NAME = "job_docs"
collection = client.get_or_create_collection(
    name = COLLECTION_NAME,
    embedding_function = embedding_func,
    metadata = {"hnsw:space": "cosine"},)

collection.add(
    documents=documents,
    ids=[str(i) for i in job_ids],
    metadatas=[{"name": str(job_names[n])} for n in range(len(data))]
)

def retrieve_relevant_jobs(query, top_k=5):
    results = collection.query(query_texts=[query], n_results=top_k)

    if results and "metadatas" in results:
        retrieved_jobs = []
        for i in range(len(results["ids"][0])):
            job_info = {
                "id": results["ids"][0][i],
                "name": results["metadatas"][0][i].get("name", ""),
                "description": results["documents"][0][i]
            }
            retrieved_jobs.append(job_info)
        return retrieved_jobs
    return []

print(f"Success!")