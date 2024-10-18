# Minimalistic App with Auto-scaling and Monitoring

This repository contains a simple Node.js app with monitoring, auto-scaling, and CI/CD integration.

## Features
- Basic Express app for demonstration.
- Dockerized for containerization.
- Kubernetes deployment for scalability.
- Horizontal Pod Autoscaler (HPA) set via a Python script.
- Traffic simulation with K6 to test auto-scaling.

## Prerequisites
- Node.js
- Docker
- Kubernetes (kubectl & Minikube)
- Python
- K6 (for load testing)
- Git

## Steps to Run the App

### 1. Install dependencies
```bash
npm install
```

### 2. Build Docker Image
```bash
docker build -t minimalistic-app2 .
```

### 3. Start Minikube
```bash
minikube start
```

### 4. Apply Kubernetes Deployment
```bash
kubectl apply -f k8s-deployment.yaml
```

### 5. Create or Update HPA using Python
```bash
python hpa_autoscaler.py
```

### 6. Simulate Traffic with K6
```bash
k6 run load_test.js
```

This will simulate traffic to test the auto-scaling of the deployment.
