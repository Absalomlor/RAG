# 🤖 BOSSBOT - just job เรื่อง jib jib
 
 
## Overview
BOSSBOT เป็นเว็บแอป AI Chatbot ที่ช่วยแนะนำงานที่เหมาะกับคุณผ่านเทคโนโลยี **RAG (Retrieval-Augmented Generation)** เพื่อให้บอทสามารถตอบคำถามจากฐานข้อมูลที่กำหนด โดยใช้ **Next.js (Frontend)** และ **FastAPI + WebSocket (Backend)** พร้อม **ChromaDB** สำหรับการจัดเก็บข้อมูลแบบเวกเตอร์
 
 
## Workflow
1️⃣ Frontend → รับข้อความ → ส่งไป WebSocket

2️⃣ Backend → รับข้อความ → ค้นหาข้อมูลจาก VectorDB → ใช้ LLM ตอบกลับ

3️⃣ Frontend แสดงผล → รับข้อความจาก WebSocket → แสดงคำตอบ

4️⃣ Deployment → Frontend ไป Firebase Hosting , Backend ไป Hugging Face
 
 
## **Frontend**
- **Next.js** + **React.js** (UI Framework)
- **TailwindCSS** (Styling)
- **WebSocket** (Real-time communication)
- **Firebase Hosting** (Deployment)
  
 **คลิกที่นี่เพื่อดูการทำงานของ Frontend**:
[Frontend BossBot by Monganio](https://github.com/monganio/frontend_bossbot)
 
## **Backend**
- **FastAPI** (API Framework)
- **WebSocket** (Real-time communication)
- **LLM (Large Language Model)** (AI Chatbot)
- **ChromaDB** (Vector Database for Retrieval)
- **Hugging Face Spaces** (Deployment)
 
 
## Usage
1️⃣ เปิดเว็บ `https://bossbot-bu.web.app/`

2️⃣ พิมพ์ข้อความและกดส่ง

3️⃣ รอให้บอทค้นหาข้อมูลจาก Vector Database และตอบกลับ

4️⃣ หากต้องการล้างแชท กดปุ่ม 🗑️ ล้างแชท
 
 
## Contributors
- **Supharat Sukpong** - [Monganio GitHub Profile](https://github.com/monganio)
- **Krasirit Pairotamonchai** - [Absalomlor GitHub Profile](https://github.com/Absalomlor)
 
