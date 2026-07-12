from fastapi import APIRouter, BackgroundTasks, File, UploadFile, Form
from product.service import ProductService
from product.model import Product


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
def store_product(
    name: str = Form(...),
    price: float = Form(...),
    image: UploadFile | None = File(None),
    background_tasks: BackgroundTasks = None,
):
    image_name = None
    if image:
        image_name = image.filename
        upload_dir = "uploads"
        import os
        os.makedirs(upload_dir, exist_ok=True)
        with open(f"{upload_dir}/{image_name}", "wb") as f:
            f.write(image.file.read())

    product = Product(id=0, name=name, price=price, image=image_name)
    return ProductService.create(product, background_tasks)

# update product
@router.put("/{id}")
def update_product(id: int, product: Product):
    return ProductService.update(id, product)

# delete product
@router.delete("/{id}")
def delete_product(id: int):
    return ProductService.delete(id)