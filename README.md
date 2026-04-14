# CloudNative DevOps Project

This project implements Tasks 1 and 2 for deploying microservices with various tools in Kubernetes.

## Components

- **APISIX**: API Gateway and Load Balancer
- **OPA (Open Policy Agent)**: Policy enforcement
- **Dapr**: Service mesh for communication
- **YugabyteDB**: Distributed SQL database
- **Kafka**: Message broker
- **KEDA**: Autoscaling
- **Service-1 & Service-2**: Python FastAPI microservices

## Deployment Steps

1. Deploy infrastructure components:
   - kubectl apply -f infrastructure/
   
2. Deploy OPA:
   - kubectl apply -f opa/
   
3. Deploy Dapr components:
   - kubectl apply -f dapr/
   
4. Deploy services:
   - kubectl apply -f service-1/
   - kubectl apply -f service-2/
   
5. Deploy KEDA and autoscaling:
   - kubectl apply -f keda/
   - kubectl apply -f infrastructure/prometheus-deploy.yaml

## Testing

- Service-1: POST /order to create order (saves to Yugabyte, publishes to Kafka)
- Service-2: Receives Kafka messages, provides /validate for direct invocation
- OPA restricts direct communication from Service-1 to Service-2 between 10:00-11:00 UTC

## Helm

Use helm/Chart.yaml for Helm deployment.