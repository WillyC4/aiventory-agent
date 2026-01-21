import vertexai
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME
from schema_reader import get_database_schema, schema_to_prompt
from schema_context import SCHEMA_CONTEXT

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION
)

model = GenerativeModel(MODEL_NAME)

_schema_cache = None


def generate_sql(question: str) -> str:
    global _schema_cache

    if _schema_cache is None:
        schema_dict = get_database_schema()
        _schema_cache = schema_to_prompt(schema_dict)

    prompt = f"""
Eres un asistente experto en MySQL

Database schema:
{_schema_cache}

Tablas explicadas:
{SCHEMA_CONTEXT}

Reglas:
- Genera SOLO UNA consulta SQL de tipo SELECT
- NUNCA uses INSERT, UPDATE, DELETE, DROP, ALTER
- Usa siempre LIMIT 50
- Utiliza únicamente las tablas y columnas listadas
- NO expliques la consulta
- Devuelve ÚNICAMENTE la consulta SQL, sin texto adicional
- NO inventes columnas
- Si una columna no existe en el schema, NO la uses
- Si no estás seguro de una columna, usa otra tabla relacionada

Pregunta:
{question}
"""
    response = model.generate_content(prompt)
    return response.text.strip()


def beautify_answer(question: str, data) -> str:
    prompt = f"""
Pregunta del usuario:
{question}

Resultado SQL:
{data}

Explica el resultado como si fueras un asistente conversacional de inventarios.
- Usa un tono claro y cercano.
- No repitas la consulta SQL.
- Responde en español natural, como en un chat.
- Si no hay resultados, dilo de forma empática.
"""
    response = model.generate_content(prompt)
    return response.text.strip()


def chat_response(question: str) -> str:
    prompt = f"""
Eres un asistente conversacional amable de un sistema de inventarios.
Responde de forma natural y breve.

Mensaje del usuario:
{question}
"""
    response = model.generate_content(prompt)
    return response.text.strip()