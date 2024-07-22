FROM python:3.12.4-slim

WORKDIR /app
COPY . .
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
