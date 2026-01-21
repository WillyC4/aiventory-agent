import vertexai
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel(MODEL_NAME)


def detect_intent(question: str) -> str:
    prompt = f"""
Clasifica el mensaje del usuario.
Responde SOLO con una palabra:
- DB → si requiere consultar una base de datos
- CHAT → si es saludo, charla o pregunta general
Mensaje:
{question}
"""
    response = model.generate_content(prompt)
    intent = response.text.strip().upper()

    if intent not in ("DB", "CHAT"):
        return "CHAT"  # fallback seguro

    return intent
