# Stage 1: Build bluevi-gpt app
FROM python:3.11-slim AS app
USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Remove cache
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs -r rm -rf

# Copy the rest of the application code
COPY . .

# Load and download the model using secrets for HF_TOKEN and MODEL_NAME
RUN --mount=type=secret,id=hf_token \
    --mount=type=secret,id=model_name \
    bash -c "HF_TOKEN=$(cat /run/secrets/hf_token) \
    MODEL_NAME=$(cat /run/secrets/model_name) \
    python -c 'from app.model.model import BlueViGptModel; BlueViGptModel().load_model()'"

# Command to run the application
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "-b", "0.0.0.0:8000"]
