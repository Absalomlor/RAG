FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/pythainlp-data && chmod -R 777 /app/pythainlp-data
ENV PYTHAINLP_DATA_DIR="/app/pythainlp-data"
RUN mkdir -p /app/huggingface && chmod -R 777 /app/huggingface
ENV HF_HOME="/app/huggingface"
ENV TRANSFORMERS_CACHE="/app/huggingface"
ENV HF_HUB_CACHE="/app/huggingface"
RUN mkdir -p /app/Database && chmod -R 777 /app/Database

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

