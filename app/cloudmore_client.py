import requests
import os
from datetime import datetime, timedelta

class CloudmoreClient:
    def __init__(self):
        self.base_url = os.getenv("CLOUDMORE_API_URL", "https://api.cloudmore.com")
        self.client_id = os.getenv("CLOUDMORE_CLIENT_ID")
        self.client_secret = os.getenv("CLOUDMORE_CLIENT_SECRET")
        self.token = None
        self.token_expiry = datetime.utcnow()
        self.authenticate()

    def authenticate(self):
        """Retrieve and store access token for Cloudmore API"""
        url = f"{self.base_url}/auth/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.token = data["access_token"]
            self.token_expiry = datetime.utcnow() + timedelta(seconds=data["expires_in"])
        else:
            raise Exception("Failed to authenticate with Cloudmore API")
    
    def get_headers(self):
        """Return authentication headers, refreshing token if necessary"""
        if datetime.utcnow() >= self.token_expiry:
            self.authenticate()
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
    
    def create_custom_service(self, service_data):
        """Create a custom service in Cloudmore"""
        url = f"{self.base_url}/services"
        response = requests.post(url, json=service_data, headers=self.get_headers())
        return response.json()
    
    def add_manual_billing(self, billing_data):
        """Add manual billing line items for an organization"""
        url = f"{self.base_url}/billing/manual"
        response = requests.post(url, json=billing_data, headers=self.get_headers())
        return response.json()
    
    def get_organization_billing(self):
        """Retrieve all organizations' billing details"""
        url = f"{self.base_url}/billing/organizations"
        response = requests.get(url, headers=self.get_headers())
        return response.json()

# Example Usage
if __name__ == "__main__":
    client = CloudmoreClient()
    print(client.get_organization_billing())
