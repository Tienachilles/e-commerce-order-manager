from app.models.orders_model import (
    add_order, get_order, update_order, delete_order
)
from app.core.connection import fetch_all_orders

class OrdersController:
    def list(self):
        return fetch_all_orders()

    def add(self, oid, cid, date, status):
        return add_order(oid, cid, date, status)

    def update(self, oid, cid, date, status):
        return update_order(oid, cid, date, status)

    def delete(self, oid):
        return delete_order(oid)

    def get(self, oid):
        return get_order(oid)
