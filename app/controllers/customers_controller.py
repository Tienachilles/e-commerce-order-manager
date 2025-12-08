from app.models.customers_model import (
    add_customer, get_customer, update_customer, delete_customer
)
from app.core.connection import fetch_all_customers

class CustomersController:
    def list(self):
        return fetch_all_customers()

    def add(self, cid, name):
        return add_customer(cid, name)

    def update(self, cid, name):
        return update_customer(cid, name)

    def delete(self, cid):
        return delete_customer(cid)
