from fastapi import FastAPI
from app.routes import router
from app.database import init_db

#test comment

# Initialize FastAPI app
app = FastAPI(title="Cisco Subscription Mock Service", version="1.0")

#Statup datatbase and initalize database
@app.on_event("startup")
async def startup_event():
    init_db()

# Include API routes
app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "Cisco Subscription Mock Service is running"}