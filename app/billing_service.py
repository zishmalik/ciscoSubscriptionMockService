from app.cloudmore_client import CloudmoreClient
from app.database import subscriptions_table

def get_organization_id(cloudmore_client, cisco_customer_id):
    """Fetch Cloudmore organizations and match the correct organizationId."""
    organizations = cloudmore_client.get_organizations()
    for org in organizations:
        if org.get("externalReference") == cisco_customer_id:
            return org.get("organizationId")
    return None

def push_billing_data():
    """Retrieve subscription data and push billing line items to Cloudmore."""
    cloudmore_client = CloudmoreClient()

    for record in subscriptions_table.all():
        cisco_customer_id = record["header"]["endCustomer"]["id"]
        organization_id = get_organization_id(cloudmore_client, cisco_customer_id)

        if not organization_id:
            print(f"❌ No matching Cloudmore organization for Cisco Customer ID {cisco_customer_id}")
            continue

        billing_data = {
            "organizationId": organization_id,
            "description": f"Billing for {record['header']['subscriptionReferenceID']}",
            "amount": record["header"]["adjustedMrc"],
            "currency": record["header"]["currencyCode"],
            "billingPeriod": "2024-02"  # This should be dynamic in real scenarios
        }

        response = cloudmore_client.add_manual_billing(billing_data)
        print(f"✅ Pushed billing data for {record['header']['subscriptionReferenceID']} to organization {organization_id}: {response}")

if __name__ == "__main__":
    push_billing_data()