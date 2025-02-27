from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EndCustomer(BaseModel):
    address1: Optional[str]
    address2: Optional[str]
    address3: Optional[str]
    city: str
    country: str
    id: str
    name: str
    postalCode: str
    state: str

class Contact(BaseModel):
    email: Optional[str]
    firstName: Optional[str]
    id: Optional[str]
    lastName: Optional[str]
    phone: Optional[str]

class SubscriptionHeader(BaseModel):
    accountTypeCode: str
    adjustedMrc: float
    autoRenTerm: Optional[int]
    billDay: Optional[str]
    billingModel: Optional[str]
    bundleLine: Optional[str]
    currencyCode: str
    daysToRenewal: int
    endCustomer: EndCustomer
    endCustomerContact: Optional[Contact]
    endDate: Optional[datetime]
    hostedOffer: Optional[str]
    initialTerm: Optional[int]
    lastUpdateDate: Optional[datetime]
    nextTrueForwardDate: Optional[datetime]
    orderActivationDate: Optional[datetime]
    orderSubmissionDate: Optional[datetime]
    overConsumed: Optional[str]
    poNumber: Optional[str]
    prepayTerm: Optional[int]
    remainingTerm: Optional[int]
    renewalDate: Optional[datetime]
    renewalTerm: Optional[int]
    soNumber: Optional[str]
    startDate: Optional[datetime]
    status: str
    tfConsumptionQuantity: Optional[float]
    transactionType: Optional[str]
    webOrderId: Optional[str]
    subscriptionReferenceID: str

class Subscription(BaseModel):
    header: SubscriptionHeader

class SubscriptionResponse(BaseModel):
    subscriptions: List[Subscription]

class SubscriptionRequest(BaseModel):
    bundle: bool
    subscriptionReferenceID: List[str]

# ✅ Define Request Model for subscriptionList
class SubscriptionListRequest(BaseModel):
    startDate: date
    endDate: date
    page: Optional[int] = 1
    pageLimit: Optional[int] = 10
    refID: str

# ✅ Define Response Model for subscriptionList
class SubscriptionListResponse(BaseModel):
    page: int
    totalCount: int
    totalPages: int
    refID: str
    subscriptions: List[dict]  # You can refine this with a Pydantic model

class SubscriptionHistory(BaseModel):
    createdBy: str
    createdDate: datetime
    transactionId: str
    transactionType: str
    webOrderId: str