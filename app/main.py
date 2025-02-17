from fastapi import FastAPI
from app.routes import router as subscription_router
from app.billing_service import push_billing_data
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Cisco Subscription Mock Service", version="1.0.0")

# Enable CORS for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(subscription_router)

@app.get("/")
def root():
    return {"message": "Cisco Subscription Mock Service is running"}

@app.post("/push-billing")
def push_billing():
    """Trigger the billing data push to Cloudmore."""
    push_billing_data()
    return {"message": "Billing data pushed successfully."}