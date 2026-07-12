from typing import Optional
from pydantic import BaseModel, constr


class Product(BaseModel):
    id: int
    name: constr(strip_whitespace=True, min_length=1)
    price: float
    image: Optional[str] = None


PRODUCTS = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99},
    {"id": 3, "name": "Product 3", "price": 5.99},
]