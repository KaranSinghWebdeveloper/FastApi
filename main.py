from fastapi import FastAPI
from products import Products

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Now i am a Python Developer."}


@app.get("/products")
def get_user():
        return Products.products

@app.get("/products/{id}")
def get_user(id: int):
        for product in Products.products:
            if product["id"] == id:
                return product
            else:
                return {"message": "Product not found."}