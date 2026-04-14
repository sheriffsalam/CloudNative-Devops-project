FROM python:3.9-slim
WORKDIR /app          
RUN pip install fastapi uvicorn dapr dapr-ext-fastapi
COPY main.py .
EXPOSE 8000
CMD ["python", "main.py"]
