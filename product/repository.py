from product.model import Products


class ProductRepository:
    products = Products.products

    @classmethod
    def index(cls):
        return cls.products