FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements from root
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY credit_score_adk/ ./credit_score_adk/
COPY token_callback.py .

# Expose port
EXPOSE 8080

# Environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["streamlit", "run", "credit_score_adk/app.py", "--server.port=8080", "--server.address=0.0.0.0"]
