from pydantic import BaseModel
from typing import Optional, List, Dict


class QuestionRequest(BaseModel):
    question: str


class AgentResponse(BaseModel):
    intent: str
    answer: str
    sql: Optional[str] = None
    data: Optional[List[Dict]] = None
