from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# ✅ Define EndCustomer Model
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

# ✅ Define Contact Model
class Contact(BaseModel):
    email: Optional[str]
    firstName: Optional[str]
    id: Optional[str]
    lastName: Optional[str]
    phone: Optional[str]

# ✅ Define Subscription Header
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

# ✅ Subscription Model
class Subscription(BaseModel):
    header: SubscriptionHeader

# ✅ Subscription Response
class SubscriptionResponse(BaseModel):
    subscriptions: List[Subscription]

# ✅ Subscription Request
class SubscriptionRequest(BaseModel):
    bundle: bool
    subscriptionReferenceID: List[str]

# ✅ Define Request Model for subscriptionList (Updated to reflect POST request)
class SubscriptionListRequest(BaseModel):
    startDate: date
    endDate: date
    page: Optional[int] = 1
    pageLimit: Optional[int] = 10
    refID: str

# ✅ Define Subscription List Item (Explicit Model)
class SubscriptionListItem(BaseModel):
    subscriptionReferenceID: str
    status: str
    startDate: Optional[datetime]
    endDate: Optional[datetime]
    adjustedMrc: float
    currencyCode: str
    accountTypeCode: str

# ✅ Define Response Model for subscriptionList
class SubscriptionListResponse(BaseModel):
    page: int
    totalCount: int
    totalPages: int
    refID: str
    subscriptions: List[SubscriptionListItem]  # Now using a structured model instead of `dict`

# ✅ Subscription History Model
class SubscriptionHistory(BaseModel):
    createdBy: str
    createdDate: datetime
    transactionId: str
    transactionType: str
    webOrderId: str