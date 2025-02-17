from app.models import Subscription

# Sample mock subscription data
mock_subscriptions = [
    Subscription(
        header={
            "accountTypeCode": "Annuity",
            "adjustedMrc": 250.5,
            "autoRenTerm": 12,
            "billDay": "15",
            "billingModel": "Standard",
            "bundleLine": "Yes",
            "currencyCode": "USD",
            "daysToRenewal": 30,
            "endCustomer": {
                "address1": "123 Main St",
                "address2": "Suite 400",
                "address3": "",
                "city": "San Francisco",
                "country": "US",
                "id": "7686473",
                "name": "Tech Solutions Inc.",
                "postalCode": "94105",
                "state": "CA"
            },
            "endCustomerContact": {
                "email": "contact@techsolutions.com",
                "firstName": "John",
                "id": "C12345",
                "lastName": "Doe",
                "phone": "+1-800-555-1234"
            },
            "startDate": "2024-01-01",
            "endDate": "2025-01-01",
            "status": "ACTIVE",
            "subscriptionReferenceID": "SUB12345"
        },
        minorLines=[
            {
                "billingAmount": 99.99,
                "chargeType": "Usage",
                "credits": [],
                "description": "Premium Support Package",
                "quantity": 10,
                "unitListPrice": 10.00,
                "unitNetPrice": 9.99,
                "usageType": "Cloud Services"
            }
        ]
    )
]
