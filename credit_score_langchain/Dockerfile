FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (curl needed for healthcheck)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY credit_score_langchain/ ./credit_score_langchain/
COPY token_callback.py .

EXPOSE 8080
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "credit_score_langchain/app.py", "--server.port=8080", "--server.address=0.0.0.0"]
