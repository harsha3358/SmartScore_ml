# SmartScore AI

## Overview
SmartScore AI is an end-to-end Machine Learning system that predicts student exam performance based on behavioral and academic factors.

This project demonstrates a complete ML lifecycle:
- Data generation
- Model training
- Model evaluation
- API development with FastAPI
- Docker containerization
- AWS EC2 deployment
- Basic MLOps practices

---

## Tech Stack

- Python
- Scikit-learn
- FastAPI
- Docker
- AWS EC2
- Uvicorn

---

## Features

- Random Forest regression model
- REST API endpoint for predictions
- Swagger documentation
- Dockerized deployment
- Logging for monitoring
- Production-ready structure

---

## API Endpoint

POST /predict

Example Input:

{
  "study_hours": 5,
  "sleep_hours": 7,
  "screen_time": 3,
  "attendance": 85,
  "practice_tests": 4
}

Response:

{
  "predicted_score": 78.4
}

---

## Run Locally

1. Train model:
   python model/train.py

2. Start server:
   uvicorn app.main:app --reload

---

## Docker Deployment

docker build -t smartscore-ai .
docker run -p 8000:8000 smartscore-ai

---

## AWS Deployment

- Launch EC2
- Install Docker
- Build image
- Run container
- Access via public IP

---

