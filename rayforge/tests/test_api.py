import pytest
from fastapi.testclient import TestClient
from rayforge.deployment.serve_fastapi import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_endpoint():
    payload = {
        "model_id": "distilbert-base-uncased-finetuned-sst-2-english",
        "source": "huggingface",
        "input": "This movie was fantastic!"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "output" in response.json()
