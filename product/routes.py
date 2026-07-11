from product.service import ProductService
from fastapi import APIRouter


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# get all products
@router.get("/")
def get_all_products():
    return ProductService.index()

# get product by id
@router.get("/{id}")
def get_product_by_id(id: int):
    return ProductService.find(id)

# store product
@router.post("/")
def store_product(product: dict):
    return ProductService.create(product)

# update product
@router.put("/{id}")
def update_product(id: int, product: dict):
    return ProductService.update(id, product)

# delete product
@router.delete("/{id}")
def delete_product(id: int):
    return ProductService.delete(id)