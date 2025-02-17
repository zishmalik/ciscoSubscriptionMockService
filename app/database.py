from tinydb import TinyDB, Query
import os
from typing import List, Optional
from app.models import Subscription, BillingRequest

# Database initialization
db_path = os.getenv("DATABASE_URL", "tinydb.json")
db = TinyDB(db_path)
subscriptions_table = db.table("subscriptions")
billing_table = db.table("billing")

# Function to retrieve mock subscriptions
def get_mock_subscriptions(subscription_ids: List[str]) -> List[Subscription]:
    SubscriptionQuery = Query()
    results = []
    for sub_id in subscription_ids:
        record = subscriptions_table.search(SubscriptionQuery.header.subscriptionReferenceID == sub_id)
        if record:
            results.extend(record)
    return results

# Function to store billing data locally
def store_billing_data(billing_data: BillingRequest):
    billing_table.insert(billing_data.dict())
    return {"message": "Billing data stored successfully."}

# Function to retrieve all stored billing data
def get_all_billing_data():
    return billing_table.all()