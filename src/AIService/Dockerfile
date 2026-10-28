# ==============================================================================
# DOCKERFILE FOR AI DYNAMIC PRICING & CHATBOT MICROSERVICE (PYTHON FLASK)
# ==============================================================================
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt waitress

COPY . .

ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

EXPOSE 5050
CMD ["python", "app.py"]
