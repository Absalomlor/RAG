FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/pythainlp-data && chmod -R 777 /app/pythainlp-data
ENV PYTHAINLP_DATA_DIR="/app/pythainlp-data"

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

