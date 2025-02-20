from fastapi import FastAPI
from app.routes import router
from app.database import init_db

# Initialize FastAPI app
app = FastAPI(title="Cisco Subscription Mock Service", version="1.0")

# Initialize database
init_db()

# Include API routes
app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "Cisco Subscription Mock Service is running"}