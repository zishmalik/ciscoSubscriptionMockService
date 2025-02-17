from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

# Test root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Cisco Subscription Mock Service is running"}

# Test subscription details endpoint
def test_get_subscription_details():
    request_payload = {
        "bundle": True,
        "subscriptionReferenceID": ["SUB12345"]
    }
    headers = {"Authorization": "Bearer test_token", "request-id": "123456"}
    response = client.post("/ccw/subscriptionmanagement/api/v1.0/sub/subscriptionDetails", json=request_payload, headers=headers)
    
    assert response.status_code == 200
    assert "subscriptions" in response.json()
    assert response.json()["subscriptions"][0]["header"]["subscriptionReferenceID"] == "SUB12345"
