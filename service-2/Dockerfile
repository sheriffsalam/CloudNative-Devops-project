FROM python:3.9-slim
RUN pip install fastapi uvicorn dapr dapr-ext-fastapi
COPY main.py .
EXPOSE 8001
CMD ["python", "main.py"]