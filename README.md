# FastAPI Products API

A simple and beginner-friendly FastAPI project that serves product data through a few REST endpoints. This project is a great starting point for learning how to build APIs with Python and FastAPI.

## 🚀 Features

- Simple home endpoint
- Fetch all products
- Fetch a single product by ID
- Clean and minimal FastAPI structure

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn

## 📁 Project Structure

```bash
FastApi/
├── main.py
├── products.py
└── README.md
```

## ▶️ Installation

1. Clone the repository
   ```bash
   git clone <your-repository-url>
   ```

2. Navigate into the project folder
   ```bash
   cd FastApi
   ```

3. Install the required dependencies
   ```bash
   pip install fastapi uvicorn
   ```

## ▶️ Run the Application

Start the server with:

```bash
uvicorn main:app --reload
```

Then open your browser or API client at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/products
- http://127.0.0.1:8000/products/1

## 📌 API Endpoints

- GET / : Returns a welcome message
- GET /products : Returns the full list of products
- GET /products/{id} : Returns a product matching the given ID

## 💡 Example Response

### Home Endpoint

```json
{
  "message": "Now i am a Python Developer."
}
```

### Products Endpoint

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": 10.99
  }
]
```

## 🌟 About

This project was created as a first step into Python backend development with FastAPI. It is simple, educational, and perfect for showcasing your first API project on GitHub.
