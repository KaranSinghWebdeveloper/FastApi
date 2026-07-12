from product.model import PRODUCTS


class ProductRepository:
    products = PRODUCTS

    @classmethod
    def index(cls):
        return cls.products