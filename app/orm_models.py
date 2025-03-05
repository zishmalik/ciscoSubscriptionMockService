from sqlalchemy import Column, Integer, String
from database import Base  # Ensure you have a Base class from SQLAlchemy

class SubscriptionListMetadata(Base):
    __tablename__ = "subscription_list_metadata"

    id = Column(Integer, primary_key=True, index=True)
    page = Column(Integer, nullable=False)
    total_count = Column(Integer, nullable=False)
    total_pages = Column(Integer, nullable=False)
    ref_id = Column(String, nullable=False, unique=True)
    page_limit = Column(Integer, nullable=False, default=10)  # ✅ Ensure this exists