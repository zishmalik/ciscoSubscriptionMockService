from tinydb import TinyDB, Query
from typing import List
from app.models import SubscriptionHeader, Subscription
import os

# Database initialization
db_path = os.getenv("DATABASE_URL", "tinydb.json")
db = TinyDB(db_path)
subscriptions_table = db.table("subscriptions")

# Function to retrieve mock subscriptions
def get_mock_subscriptions(subscription_ids: List[str]) -> List[Subscription]:
    SubscriptionQuery = Query()
    results = []
    for sub_id in subscription_ids:
        record = subscriptions_table.search(SubscriptionQuery.header.subscriptionReferenceID == sub_id)
        if record:
            results.extend(record)
    return results
