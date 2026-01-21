from llm import generate_sql, beautify_answer, chat_response
from sql_guard import validate_sql
from db import run_query
from intent import detect_intent


def ask_agent(question: str):
    print("\nPregunta:", question)

    intent = detect_intent(question)
    print("Intención detectada:", intent)

    if intent == "CHAT":
        answer = chat_response(question)
        print("\nRespuesta:\n", answer)
        return

    # ---- FLUJO DB ----
    sql_raw = generate_sql(question)
    print("\nSQL generado (raw):\n", sql_raw)

    sql = validate_sql(sql_raw)
    print("\nSQL ejecutado:\n", sql)

    data = run_query(sql)
    print("\nResultado crudo:\n", data)

    answer = beautify_answer(question, data)
    print("\n💬 Respuesta final:\n", answer)


if __name__ == "__main__":
    while True:
        q = input("\nPregunta (o 'salir'): ")
        if q.lower() == "salir":
            break
        ask_agent(q)
