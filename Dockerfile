FROM python:3.10-slim

WORKDIR /app

COPY . .

# Use ENTRYPOINT so docker passes args like "greet Alice" to app.py
ENTRYPOINT ["python", "app.py"]

