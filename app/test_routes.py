import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, init_db
from sqlalchemy.orm import sessionmaker

# Test client setup
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    init_db()
    db = SessionLocal()
    yield db
    db.close()

# Test health check endpoint
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Cisco Subscription Mock Service is running"}

# Test subscription details endpoint
def test_subscription_details(setup_db):
    payload = {"bundle": True, "subscriptionReferenceID": ["SUB12345"]}
    response = client.post("/ccw/subscriptionmanagement/api/v1.0/sub/subscriptionDetails", json=payload)
    assert response.status_code in [200, 404]  # 200 if data exists, 404 if no subscriptions found

# Test subscription list endpoint
def test_subscription_list(setup_db):
    response = client.get("/ccw/subscriptionmanagement/api/v1.0/sub/subscriptionList?page=1&ref_id=test_ref")
    assert response.status_code in [200, 404]  # 200 if data exists, 404 if not found

# Test subscription history endpoint
def test_subscription_history(setup_db):
    response = client.get("/ccw/subscriptionmanagement/api/v1.0/sub/SUB12345/history")
    assert response.status_code in [200, 404]  # 200 if history exists, 404 if no history found