import re

FORBIDDEN_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP",
    "ALTER", "TRUNCATE", "REPLACE"
]


def normalize_sql(sql: str) -> str:
    sql = sql.strip()

    if sql.startswith("```"):
        sql = re.sub(r"^```sql\s*", "", sql, flags=re.IGNORECASE)
        sql = re.sub(r"^```\s*", "", sql)
        sql = re.sub(r"\s*```$", "", sql)

    return sql.strip()


def validate_sql(sql: str) -> str:
    cleaned = normalize_sql(sql).rstrip(";")
    sql_upper = cleaned.upper()

    if not re.match(r"^SELECT\s", sql_upper):
        raise ValueError("❌ Solo se permiten consultas SELECT")

    for word in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{word}\b", sql_upper):
            raise ValueError(f"❌ SQL no permitido: {word}")

    if ";" in cleaned:
        raise ValueError("❌ Solo una consulta permitida")

    if "COUNT(" not in sql_upper:
        if not re.search(r"\bLIMIT\s+\d+\b", sql_upper):
            raise ValueError("❌ La consulta debe usar LIMIT")

    return cleaned
