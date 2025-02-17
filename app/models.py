from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class Contact(BaseModel):
    email: Optional[str]
    firstName: Optional[str]
    id: Optional[str]
    lastName: Optional[str]
    phone: Optional[str]

class BillToCustomer(BaseModel):
    details: Dict[str, Any]

class EndCustomer(BaseModel):
    address1: str
    address2: Optional[str]
    address3: Optional[str]
    city: str
    country: str
    id: str
    name: str
    postalCode: str
    state: str

class SubscriptionHeader(BaseModel):
    accountTypeCode: str
    adjustedMrc: float
    autoRenTerm: Optional[float]
    billDay: Optional[str]
    billingModel: Optional[str]
    bundleLine: Optional[str]
    currencyCode: str
    daysToRenewal: int
    endCustomer: EndCustomer
    endCustomerContact: Optional[Contact]
    endDate: Optional[str]
    hostedOffer: Optional[str]
    initialTerm: Optional[float]
    lastUpdateDate: Optional[str]
    nextTrueForwardDate: Optional[str]
    orderActivationDate: Optional[str]
    orderSubmissionDate: Optional[str]
    overConsumed: Optional[str]
    poNumber: Optional[str]
    prepayTerm: Optional[float]
    primaryBillingContact: Optional[Contact]
    primaryBusinessContact: Optional[Contact]
    remainingTerm: Optional[float]
    renewalDate: Optional[str]
    renewalTerm: Optional[float]
    reseller: Optional[BillToCustomer]
    resellerContact: Optional[Contact]
    soNumber: Optional[str]
    startDate: Optional[str]
    status: str
    tfConsumptionQuantity: Optional[float]
    transactionType: Optional[str]
    webOrderId: Optional[str]
    subscriptionReferenceID: str
    billToCustomer: Optional[BillToCustomer]

class CreditDetails(BaseModel):
    applicableAtRenewal: Optional[bool]
    creditTerm: Optional[float]
    currency: Optional[str]
    endDate: Optional[str]
    monthlyCreditAmount: Optional[str]
    name: Optional[str]
    startDate: Optional[str]
    timeBoundCredit: Optional[str]

class MinorLine(BaseModel):
    billingAmount: float
    chargeType: str
    credits: Optional[List[CreditDetails]]
    deliveryOption: Optional[str]
    description: Optional[str]
    extendedNetPrice: float
    monthlySubscriptionCredit: Optional[str]
    overConsumed: Optional[str]
    overConsumedQuantity: Optional[str]
    pricingUnitOfMeasure: Optional[str]
    quantity: float
    tfConsumptionQuantity: Optional[str]
    tfEntitlement: Optional[str]
    totalCredits: Optional[float]
    totalDiscount: Optional[float]
    totalDiscountPercentage: Optional[float]
    typeOfQuantity: Optional[str]
    unitListPrice: Optional[float]
    unitNetPrice: Optional[float]
    usageType: Optional[str]

class Subscription(BaseModel):
    header: SubscriptionHeader
    minorLines: Optional[List[MinorLine]]

class SubscriptionResponse(BaseModel):
    subscriptions: List[Subscription]

class SubscriptionRequest(BaseModel):
    bundle: bool
    subscriptionReferenceID: List[str]

class BillingRequest(BaseModel):
    organizationId: str
    description: str
    amount: float
    currency: str
    billingPeriod: str