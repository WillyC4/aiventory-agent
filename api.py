from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict

from llm import generate_sql, beautify_answer, chat_response
from sql_guard import validate_sql
from db import run_query
from intent import detect_intent

app = FastAPI(
    title="AIventory Agent API",
    description="Agente inteligente para consultas de AIventory",
    version="1.0.0"
)

# --------------------- CORS ---------------------
origins = [
    "http://localhost:8000",  # tu frontend local (Laravel)
    "http://127.0.0.1:8000",
    "https://aiventory-819682124232.us-central1.run.app",  # despliegue en Cloud Run
    # agrega aquí cualquier otro dominio que necesites
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, etc.
    allow_headers=["*"],        # Content-Type, Authorization, etc.
)

# ---------- SCHEMAS (integrados) ----------

class QuestionRequest(BaseModel):
    question: str


class AgentResponse(BaseModel):
    intent: str
    answer: str
    sql: Optional[str] = None
    data: Optional[List[Dict]] = None


# ---------- ENDPOINT ----------

@app.post("/ask", response_model=AgentResponse)
def ask_agent(req: QuestionRequest):
    question = req.question.strip()

    if not question:
        raise HTTPException(status_code=400, detail="La pregunta no puede estar vacía")

    intent = detect_intent(question)

    # ----- CHAT -----
    if intent == "CHAT":
        answer = chat_response(question)
        return AgentResponse(
            intent="CHAT",
            answer=answer
        )

    # ----- DB -----
    try:
        sql_raw = generate_sql(question)
        sql = validate_sql(sql_raw)
        data = run_query(sql)
        answer = beautify_answer(question, data)

        return AgentResponse(
            intent="DB",
            sql=sql,
            data=data,
            answer=answer
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
