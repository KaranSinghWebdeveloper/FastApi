from product.repository import ProductRepository

class ProductService:
    @staticmethod
    def index():
        return ProductRepository.index()

    @staticmethod
    def find(id: int):
        for product in ProductRepository.products:
            if product["id"] == id:
                return product
        return {"message": "Product not found."}

    @staticmethod
    def create(product: dict):
        ProductRepository.products.append(product)
        return product

    @staticmethod
    def update(id: int, product: dict):
        for i, p in enumerate(ProductRepository.products):
            if p["id"] == id:
                ProductRepository.products[i] = product
                return product
        return {"message": "Product not found."}

    @staticmethod
    def delete(id: int):
        for i, product in enumerate(ProductRepository.products):
            if product["id"] == id:
                del ProductRepository.products[i]
                return {"message": "Product deleted."}
        return {"message": "Product not found."}