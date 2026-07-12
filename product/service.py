from pathlib import Path
from fastapi import BackgroundTasks
from product.repository import ProductRepository
from product.model import Product
from response import success, created, not_found, deleted
from core.email import send_email_background


class ProductService:
    @staticmethod
    def index():
        return success(ProductRepository.index(), "Products fetched successfully.")

    @staticmethod
    def find(id: int):
        for product in ProductRepository.products:
            if product["id"] == id:
                return success(product)
        return not_found("Product not found.")

    @staticmethod
    def create(product: Product, background_tasks: BackgroundTasks | None = None):
        if product.image:
            upload_dir = Path("uploads")
            upload_dir.mkdir(exist_ok=True)
            file_path = upload_dir / product.image
            if not file_path.exists():
                file_path.write_bytes(b"")

        ProductRepository.products.append(product.dict())

        if background_tasks is not None:
            send_email_background(
                background_tasks,
                "Product created",
                f"Product '{product.name}' was created successfully.",
                "admin@example.com",
            )

        return created(product.dict(), "Product created.")

    @staticmethod
    def update(id: int, product: Product):
        for i, p in enumerate(ProductRepository.products):
            if p["id"] == id:
                ProductRepository.products[i] = product.dict()
                return success(product.dict(), "Product updated.")
        return not_found("Product not found.")

    @staticmethod
    def delete(id: int):
        for i, product in enumerate(ProductRepository.products):
            if product["id"] == id:
                del ProductRepository.products[i]
                return deleted(None, "Product deleted.")
        return not_found("Product not found.")