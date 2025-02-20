import requests
from dotenv import load_dotenv
import os

load_dotenv()

TYPHOON_API_KEY = os.getenv("TYPHOON_API_KEY")
TYPHOON_ENDPOINT = "https://api.opentyphoon.ai/v1/chat/completions"

def generate_answer_with_llm(query, context):
    """
    ส่งข้อมูลไปให้ LLM (OpenTyphoon) เพื่อสร้างคำตอบ
    :param query: คำถามจากผู้ใช้
    :param context: ข้อมูลประกอบที่ใช้ตอบคำถาม
    :return: คำตอบจาก LLM
    """
    
    prompt = f"ข้อมูลที่เกี่ยวข้อง:\n{context}\n\nตอบคำถามต่อไปนี้:\n{query}"

    response = requests.post(TYPHOON_ENDPOINT, json={
        "model": "typhoon-v2-70b-instruct",
        "max_tokens": 512,
        "messages": [{"content": prompt, "role": "user"}],
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": -1,
        "repetition_penalty": 1.05,
        "min_p": 0 
    }, headers={
        "Authorization": f"Bearer {TYPHOON_API_KEY}",
    })

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error calling LLM API: {response.text}")