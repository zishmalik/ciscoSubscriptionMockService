from fastapi import FastAPI
from app.routes import router as subscription_router
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