from fastapi import FastAPI
from dapr.clients import DaprClient
import uvicorn

app = FastAPI()

@app.get("/healthz")
async def health():
    return {"status": "ok"}

@app.post("/order")
async def create_order(order: dict):
    with DaprClient() as d:
        # Task 1.2: Save to YugabyteDB via Dapr State Store
        d.save_state(store_name='statestore', key=order['id'], value=order['data'])
        
        # Task 1.4a: Direct Service Invocation
        try:
            resp = d.invoke_method('service-2', 'validate', data=order)
            print(f"Validation response: {resp}")
        except Exception as e:
            print(f"Direct invocation failed: {e}")
        
        # Task 1.4b: Pub/Sub with Kafka
        d.publish_event(pubsub_name='pubsub', topic_name='orders', data=order)
        
    return {"status": "Order Sent", "id": order['id']}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)