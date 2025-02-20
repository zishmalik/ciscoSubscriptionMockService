# Cisco Subscription Mock Service

## High-Level Features
- **Simulated Cisco Subscription Management API**
- **Retrieve Subscription Details & Transaction History**
- **Generate Mock Data for Testing**
- **Seamless Integration with PostgreSQL**
- **REST API with FastAPI Framework**
- **Deployable as an Azure Web App**
- **Environment variables managed via Azure Web App Settings**

## Project Structure
```
.
├── app
│   ├── database.py       # Database models and connections
│   ├── main.py           # FastAPI app initialization
│   ├── models.py         # Pydantic models for API requests/responses
│   ├── routes.py         # API endpoints
│   ├── mock_data.py      # Script to generate mock data
│   ├── test_routes.py    # Unit tests
├── requirements.txt      # Dependencies
├── README.md             # Documentation
```

## Prerequisites
- **Python 3.9+** installed
- **PostgreSQL Database** setup
- **Azure CLI** installed if deploying to Azure Web App

## Installation Steps
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/your-repo/cisco-subscription-mock.git
   cd cisco-subscription-mock
   ```

2. **Create a Virtual Environment:**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Environment variables should be configured directly within Azure Web App settings.
   - The application expects values such as `DATABASE_URL` to be set within the Azure environment.

## Running the Application Locally
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## How to Deploy on Azure Web App
For detailed instructions, follow the [official Microsoft documentation](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal).

### Quick Steps for Azure Deployment
1. **Login to Azure CLI:**
   ```sh
   az login
   ```
2. **Create an App Service Plan:**
   ```sh
   az appservice plan create --name CiscoSubscriptionPlan --resource-group MyResourceGroup --sku B1 --is-linux
   ```
3. **Create the Web App:**
   ```sh
   az webapp create --resource-group MyResourceGroup --plan CiscoSubscriptionPlan --name CiscoSubscriptionMock --runtime "PYTHON|3.9"
   ```
4. **Configure Environment Variables in Azure Web App Settings:**
   - In Azure Portal, go to **Configuration → Environment Variables**.
   - Add necessary variables such as `DATABASE_URL`.

5. **Deploy the Application:**
   ```sh
   az webapp up --name CiscoSubscriptionMock --resource-group MyResourceGroup
   ```

## License
MIT License
