# Cisco Subscription Mock Service

This is a **FastAPI-based mock service** for simulating Cisco's Subscription Management API. The service provides mock responses for subscription details and history.

## Features
- 🚀 FastAPI for rapid development
- 📄 OpenAPI documentation (`/docs` for Swagger, `/redoc` for ReDoc)
- 📦 Lightweight database support using TinyDB (for mock data storage)
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
│── tests/
│   ├── test_main.py  # Unit tests
│── .gitignore  # Ignore unnecessary files
│── requirements.txt  # Dependencies
│── README.md  # Project documentation
│── .env.example  # Example environment variables
```

## Installation
### Prerequisites
- Python 3.8+

### Steps
1. **Clone the repository**
   ```sh
   git clone https://github.com/YOUR_USERNAME/ciscoSubscriptionMockService.git
   cd ciscoSubscriptionMockService
   ```

2. **Create a virtual environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Unix-based systems
   venv\Scripts\activate  # For Windows
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

## Running Tests
```sh
pytest tests/
```

## Contributing
Feel free to open issues or submit pull requests!

## License
MIT License