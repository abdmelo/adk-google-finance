FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY credit_score_orchestration/ ./credit_score_orchestration/
COPY token_callback.py .

EXPOSE 8080
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "credit_score_orchestration/app.py", "--server.port=8080", "--server.address=0.0.0.0"]
