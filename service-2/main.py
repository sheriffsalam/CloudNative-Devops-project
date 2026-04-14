from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/healthz")
async def health():
    return {"status": "ok"}

# Task 1.4a: Direct Service Invocation endpoint
@app.post("/validate")
async def validate(data: dict):
    print(f"Service 2 received validation request: {data}")
    return {"valid": True, "source": "service-2"}

# Task 1.4b: Kafka Pub/Sub endpoint
@app.post("/orders-handler")
async def handle_order(event: dict):
    print(f"Service 2 received Kafka message: {event['data']}")
    return {"status": "processed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)