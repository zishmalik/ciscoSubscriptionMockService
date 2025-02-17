# Cisco Subscription Mock Service

This is a **FastAPI-based mock service** for simulating Cisco's Subscription Management API and integrating with Cloudmore for billing and service management. The service provides mock responses for subscription details and pushes billing data to Cloudmore.

## Features
- 🚀 FastAPI for rapid development
- 📄 OpenAPI documentation (`/docs` for Swagger, `/redoc` for ReDoc)
- 📦 Lightweight database support using TinyDB (for mock data storage)
- 🔗 Integration with Cloudmore API for **billing and custom service creation**
- ✅ Unit tests for API validation

## Project Structure
```
ciscoSubscriptionMockService/
│── app/
│   ├── __init__.py
│   ├── main.py  # FastAPI application
│   ├── models.py  # Pydantic models
│   ├── routes.py  # API routes
│   ├── mock_data.py  # Mock response data
│   ├── database.py  # Lightweight DB or storage integration
│   ├── cloudmore_client.py  # Cloudmore API integration
│   ├── billing_service.py  # Push billing data to Cloudmore
│── tests/
│   ├── test_main.py  # Unit tests
│── .gitignore  # Ignore unnecessary files
│── requirements.txt  # Dependencies
│── README.md  # Project documentation
│── .env  # Environment variables
│── .env.example  # Example environment variables
│── start.sh  # (Optional) Startup script
```

## Installation
### Prerequisites
- Python 3.8+
- Cloudmore API credentials

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/zishmalik/ciscoSubscriptionMockService.git
   cd ciscoSubscriptionMockService
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # For Unix-based systems
   .venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application
```sh
uvicorn app.main:app --reload
```
- The API will be available at: `http://127.0.0.1:8000`
- OpenAPI Documentation:
  - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Pushing Billing Data to Cloudmore
To manually trigger billing data uploads to Cloudmore, run:
```sh
curl -X 'POST' 'http://127.0.0.1:8000/push-billing'
```

## Running Tests
```sh
pytest tests/
```

## Contributing
All documentation should be maintained in **Confluence**, and all code should be stored in **GitHub**.

## License
MIT License