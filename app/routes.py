from fastapi import APIRouter, Header, HTTPException, Depends
from typing import List
from app.models import SubscriptionRequest, SubscriptionResponse
from app.database import get_mock_subscriptions

router = APIRouter(prefix="/ccw/subscriptionmanagement/api/v1.0/sub")

def authenticate_request(request_id: str = Header(...), authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Missing or invalid token")
    return authorization

@router.post("/subscriptionDetails", response_model=SubscriptionResponse)
def get_subscription_details(
    request: SubscriptionRequest,
    auth: str = Depends(authenticate_request)
):
    subscriptions = get_mock_subscriptions(request.subscriptionReferenceID)
    if not subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for given IDs")
    return {"subscriptions": subscriptions}
