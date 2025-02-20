from fastapi import FastAPI
from vector_db import retrieve_relevant_jobs
from llm import generate_answer_with_llm

app = FastAPI()

@app.get("/rag/{query}")
def get_rag_response(query: str):
    relevant_jobs = retrieve_relevant_jobs(query, top_k=3)

    if not relevant_jobs:
        return {"answer": "ไม่พบข้อมูลที่เกี่ยวข้อง"}

    context = "\n".join([f"{job['name']}: {job['description']}" for job in relevant_jobs])
    answer = generate_answer_with_llm(query, context)

    return {"answer": answer, "related_jobs": relevant_jobs}