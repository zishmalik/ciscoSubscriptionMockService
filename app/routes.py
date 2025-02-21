from fastapi import APIRouter, Header, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from app.database import SessionLocal, Subscription, SubscriptionListMetadata, SubscriptionHistory
from app.mock_data import populate_mock_data, generate_mock_subscriptions, generate_mock_subscription_list_metadata, generate_mock_subscription_history
from app.models import SubscriptionRequest, SubscriptionResponse
import random
import os

# Fetch the API key from environment variables
API_KEY = os.getenv("CISCO_SERVICE_API_KEY", "default-secret-key")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_request(x_api_key: str = Header(...)):
    """Check if the provided API key matches the expected value"""
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    return x_api_key

router = APIRouter(prefix="/ccw/subscriptionmanagement/api/v1.0/sub")

@router.post("/subscriptionDetails", response_model=SubscriptionResponse)
def get_subscription_details(
    request: SubscriptionRequest,
    db: Session = Depends(get_db),
    auth: str = Depends(authenticate_request)
):
    subscriptions = db.query(Subscription).filter(Subscription.subscription_reference_id.in_(request.subscriptionReferenceID)).all()
    if not subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for given IDs")
    return {"subscriptions": subscriptions}

@router.get("/subscriptionList")
def get_subscription_list(
    page: int, ref_id: str, db: Session = Depends(get_db), auth: str = Depends(authenticate_request)
):
    metadata = db.query(SubscriptionListMetadata).filter_by(ref_id=ref_id).first()
    if not metadata:
        raise HTTPException(status_code=404, detail="Subscription list metadata not found")
    subscriptions = db.query(Subscription).limit(10).offset((page - 1) * 10).all()
    return {"page": page, "totalCount": metadata.total_count, "totalpages": metadata.total_pages, "refID": ref_id, "subscriptions": subscriptions}

@router.get("/{subscriptionReferenceId}/history")
def get_subscription_history(
    subscriptionReferenceId: str, db: Session = Depends(get_db), auth: str = Depends(authenticate_request)
):
    history_records = db.query(SubscriptionHistory).filter_by(subscription_reference_id=subscriptionReferenceId).all()
    if not history_records:
        raise HTTPException(status_code=404, detail="No history found for given subscriptionReferenceId")
    return history_records

@router.post("/generate-mock-data")
def generate_mock_data(
    scenario: str = Body("random", embed=True),
    count: int = Body(10, embed=True),
    db: Session = Depends(get_db)
):
    if scenario in ["basic", "full"]:
        generate_mock_subscription_list_metadata(db)  # ✅ Ensure metadata exists

    if scenario == "random":
        populate_mock_data(db)
    elif scenario == "basic":
        generate_mock_subscriptions(db, count=5)
    elif scenario == "full":
        generate_mock_subscriptions(db, count=10)
        generate_mock_subscription_history(db, count=5)
    else:
        raise HTTPException(status_code=400, detail="Invalid scenario provided")
    
    return {"message": f"Mock data generated successfully for scenario: {scenario}"}