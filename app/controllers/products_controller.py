from app.models.products_model import (
    add_product, get_product, update_product, delete_product
)
from app.core.connection import fetch_all_products

class ProductsController:
    def list(self):
        return fetch_all_products()

    def add(self, pid, name, price):
        return add_product(pid, name, price)

    def update(self, pid, name, price):
        return update_product(pid, name, price)

    def delete(self, pid):
        return delete_product(pid)
