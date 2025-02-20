import logging
import asyncio

import requests
import os
from datetime import datetime, timedelta


class CloudmoreClient:
    def __init__(self):
        self.base_url = os.getenv("CLOUDMORE_API_URL", "https://api-dev.cloudmore.com")
        self.client_id = os.getenv("CLOUDMORE_CLIENT_ID", "ro.customer.client")
        self.client_secret = os.getenv("CLOUDMORE_CLIENT_SECRET")
        self.username = os.getenv("CLOUDMORE_USERNAME")
        self.password = os.getenv("CLOUDMORE_PASSWORD")
        self.token = None
        self.token_expiry = datetime.now()

    async def authenticate(self):
        """Retrieve and store access token for Cloudmore API"""
        url = f"{self.base_url}/connect/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "password",
            "scope": "api",
            "username": self.username,
            "password": self.password
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, payload,headers)
        if response.status_code == 200:
            data = response.json()
            self.token = data["access_token"]
            self.token_expiry = datetime.now() + timedelta(seconds=data["expires_in"])
        else:
            logging.warning(response)
            raise Exception("Failed to authenticate with Cloudmore API")

    async def get_headers(self):
        """Return authentication headers, refreshing token if necessary"""
        if datetime.now() >= self.token_expiry:
            await self.authenticate()
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    async def create_custom_service(self, service_data):
        """Create a custom service in Cloudmore"""
        url = f"{self.base_url}/services"
        headers = await self.get_headers()
        response = requests.post(url, json=service_data, headers=headers)
        return response.json()

    async def add_manual_billing(self, billing_data):
        """Add manual billing line items for an organization"""
        url = f"{self.base_url}/billing/manual"
        headers = await self.get_headers()
        response = requests.post(url, json=billing_data, headers=headers)
        return response.json()

    async def get_organization_billing(self):
        """Retrieve all organizations' billing details"""
        url = f"{self.base_url}/billing/organizations"
        headers = await self.get_headers()
        response = requests.get(url,headers=headers)
        return response.json()


async def main():
    try:
        logging.warning("CloudMore API Client")
        client = CloudmoreClient()
        await client.authenticate()
        headers = await client.get_headers()
        logging.warning("headers: %s" % headers)
    except Exception as e:
        logging.error(e)
        return


if __name__ == '__main__':
    asyncio.run(main())