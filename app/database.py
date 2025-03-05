from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import os

# Azure PostgreSQL Connection (Using ciscoSubscription Database)
DATABASE_URL = f"postgresql://{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}@{os.getenv('PGHOST')}:{os.getenv('PGPORT')}/ciscoSubscription"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Subscription Table
class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    subscription_reference_id = Column(String(255), unique=True, nullable=False)
    account_type_code = Column(String(50))
    adjusted_mrc = Column(DECIMAL(10,2))
    auto_ren_term = Column(Integer)
    bill_day = Column(String(20))
    billing_model = Column(String(50))
    bundle_line = Column(String(50))
    currency_code = Column(String(10))
    days_to_renewal = Column(Integer)
    organization_id = Column(String, nullable=False)
    end_date = Column(TIMESTAMP)
    hosted_offer = Column(String(255))
    initial_term = Column(Integer)
    last_update_date = Column(TIMESTAMP)
    next_true_forward_date = Column(TIMESTAMP)
    order_activation_date = Column(TIMESTAMP)
    order_submission_date = Column(TIMESTAMP)
    over_consumed = Column(String(50))
    po_number = Column(String(50))
    prepay_term = Column(Integer)
    remaining_term = Column(Integer)
    renewal_date = Column(TIMESTAMP)
    renewal_term = Column(Integer)
    so_number = Column(String(50))
    start_date = Column(TIMESTAMP)
    status = Column(String(50))
    tf_consumption_quantity = Column(DECIMAL(10,2))
    transaction_type = Column(String(50))
    web_order_id = Column(String(50))

# Subscription List Metadata Table
class SubscriptionListMetadata(Base):
    __tablename__ = "subscription_list_metadata"

    id = Column(Integer, primary_key=True, index=True)
    page = Column(Integer, nullable=False)
    total_count = Column(Integer, nullable=False)
    total_pages = Column(Integer, nullable=False)
    page_limit = Column(Integer, nullable=False, default=10)
    ref_id = Column(String, unique=True, nullable=False)

# Subscription Minor Lines Table
class SubscriptionMinorLine(Base):
    __tablename__ = "subscription_minor_lines"

    id = Column(Integer, primary_key=True, index=True)
    subscription_reference_id = Column(String, ForeignKey("subscriptions.subscription_reference_id"), nullable=False)
    billing_amount = Column(DECIMAL(10,2))
    charge_type = Column(String(50))
    description = Column(String(255))
    extended_net_price = Column(DECIMAL(10,2))
    quantity = Column(Integer)
    unit_list_price = Column(DECIMAL(10,2))
    unit_net_price = Column(DECIMAL(10,2))
    usage_type = Column(String(50))

# Subscription Credits Table
class SubscriptionCredit(Base):
    __tablename__ = "subscription_credits"

    id = Column(Integer, primary_key=True, index=True)
    subscription_reference_id = Column(String, ForeignKey("subscriptions.subscription_reference_id"), nullable=False)
    applicable_at_renewal = Column(String(5))
    credit_term = Column(Integer)
    currency = Column(String(10))
    end_date = Column(TIMESTAMP)
    monthly_credit_amount = Column(DECIMAL(10,2))
    credit_name = Column(String(255))
    start_date = Column(TIMESTAMP)

# Subscription History Table
class SubscriptionHistory(Base):
    __tablename__ = "subscription_history"

    id = Column(Integer, primary_key=True, index=True)
    subscription_reference_id = Column(String, ForeignKey("subscriptions.subscription_reference_id", ondelete="CASCADE"), nullable=False)
    created_by = Column(String, nullable=True)
    created_date = Column(TIMESTAMP, nullable=True)
    transaction_id = Column(String, unique=True, nullable=False)
    transaction_type = Column(String(50), nullable=True)
    web_order_id = Column(String(50), nullable=True)

# Initialize Database

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()