from sqlalchemy.orm import Session
from app.database import Subscription, SubscriptionListMetadata, SubscriptionHistory
import random
from datetime import datetime, timedelta

def generate_mock_subscriptions(db: Session, count: int = 10):
    for i in range(count):
        sub = Subscription(
            subscription_reference_id=f"SUB{i+1000}",
            account_type_code="Enterprise",
            adjusted_mrc=random.uniform(10.0, 500.0),
            auto_ren_term=random.randint(1, 36),
            bill_day="15",
            billing_model="Standard",
            bundle_line="BundleX",
            currency_code="USD",
            days_to_renewal=random.randint(1, 90),
            organization_id=f"ORG{i+1}",
            end_date=datetime.utcnow() + timedelta(days=365),
            hosted_offer="Premium Support",
            initial_term=12,
            last_update_date=datetime.utcnow(),
            next_true_forward_date=datetime.utcnow() + timedelta(days=30),
            order_activation_date=datetime.utcnow() - timedelta(days=5),
            order_submission_date=datetime.utcnow() - timedelta(days=10),
            over_consumed="No",
            po_number=f"PO-{i+1000}",
            prepay_term=12,
            remaining_term=random.randint(1, 12),
            renewal_date=datetime.utcnow() + timedelta(days=180),
            renewal_term=12,
            so_number=f"SO-{i+1000}",
            start_date=datetime.utcnow() - timedelta(days=30),
            status="Active",
            tf_consumption_quantity=random.uniform(1.0, 100.0),
            transaction_type="New Order",
            web_order_id=f"WO-{i+1000}"
        )
        db.add(sub)
    db.commit()

def generate_mock_subscription_list_metadata(db: Session):
    """Ensures metadata exists for subscription listing"""
    ref_id = "mock123"  # Fixed reference ID
    existing_metadata = db.query(SubscriptionListMetadata).filter_by(ref_id=ref_id).first()
    
    if not existing_metadata:
        metadata = SubscriptionListMetadata(
            ref_id=ref_id,
            total_count=10,
            total_pages=1,
            page_limit=10
        )
        db.add(metadata)
        db.commit()
        print(f"✅ Created metadata for ref_id: {ref_id}")
    else:
        print(f"🔍 Metadata already exists for ref_id: {ref_id}")

def generate_mock_subscription_history(db: Session, count: int = 5):
    for i in range(count):
        history = SubscriptionHistory(
            subscription_reference_id=f"SUB{random.randint(1000, 1010)}",
            created_by="System Admin",
            created_date=datetime.utcnow() - timedelta(days=random.randint(1, 100)),
            transaction_id=f"TXN{random.randint(10000, 99999)}",
            transaction_type=random.choice(["New Order", "Renewal", "Cancellation"]),
            web_order_id=f"WO-{random.randint(1000, 2000)}"
        )
        db.add(history)
    db.commit()

def populate_mock_data(db: Session, scenario: str = "random", count: int = 10):
    if scenario == "random":
        generate_mock_subscriptions(db, count)
        generate_mock_subscription_list_metadata(db)
        generate_mock_subscription_history(db, count=5)
    elif scenario == "basic":
        generate_mock_subscriptions(db, count=5)
        generate_mock_subscription_list_metadata(db)
    elif scenario == "full":
        generate_mock_subscriptions(db, count)
        generate_mock_subscription_list_metadata(db)
        generate_mock_subscription_history(db, count)
    else:
        raise ValueError("Invalid scenario provided")

if __name__ == "__main__":
    from app.database import SessionLocal
    db = SessionLocal()
    populate_mock_data(db)
    db.close()
