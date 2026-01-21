FROM python:3.11-slim

# Evita buffers raros en logs
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Dependencias del sistema (mysqlclient no lo usas, mysql-connector sí)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiamos requirements primero (mejor cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY . .

# Cloud Run escucha en 8080
EXPOSE 8080

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
