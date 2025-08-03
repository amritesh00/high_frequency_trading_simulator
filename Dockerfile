# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_ENV=production
CMD ["python", "app/main.py"]
