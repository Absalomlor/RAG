from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from vector_db import retrieve_relevant_jobs
from llm import generate_answer_with_llm
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get("/rag/{query}")
def get_rag_response(query: str):
    relevant_jobs = retrieve_relevant_jobs(query, top_k=3)
 
    if not relevant_jobs:
        return {"answer": "ไม่พบข้อมูลที่เกี่ยวข้อง"}
 
    context = "\n".join([f"{job['name']}: {job['description']}" for job in relevant_jobs])
    answer = generate_answer_with_llm(query, context)
 
    return {"answer": answer, "related_jobs": relevant_jobs}
 
@app.websocket("/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        relevant_jobs = retrieve_relevant_jobs(data, top_k=3)
 
        if not relevant_jobs:
            await websocket.send_text("ไม่พบข้อมูลที่เกี่ยวข้อง")
            continue
        context = "\n".join([f"{job['name']}: {job['description']}" for job in relevant_jobs])
        answer = generate_answer_with_llm(data, context)
 
        await websocket.send_text(answer)