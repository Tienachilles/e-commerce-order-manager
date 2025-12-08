from app.models.order_items_model import (
    add_order_item, get_order_item, update_order_item, delete_order_item
)
from app.core.connection import fetch_order_items

class OrderItemsController:
    def list(self, order_id=None):
        return fetch_order_items(order_id)

    def add(self, oid, pid, qty, price):
        return add_order_item(oid, pid, qty, price)

    def update(self, oid, pid, qty, price):
        return update_order_item(oid, pid, qty, price)

    def delete(self, oid, pid):
        return delete_order_item(oid, pid)

    def get(self, oid, pid):
        return get_order_item(oid, pid)
