import mysql.connector
from config import DB_CONFIG


def get_database_schema():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]

    schema = {}

    for table in tables:
        cursor.execute(f"SHOW COLUMNS FROM `{table}`")
        columns = []
        for col, dtype, *_ in cursor.fetchall():
            columns.append(f"{col} {dtype}")
        schema[table] = columns

    cursor.close()
    conn.close()

    return schema


def schema_to_prompt(schema: dict) -> str:
    lines = []
    for table, columns in schema.items():
        lines.append(f"{table}(")
        for col in columns:
            lines.append(f"  {col},")
        lines.append(")\n")
    return "\n".join(lines)
