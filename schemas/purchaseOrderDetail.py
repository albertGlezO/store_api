from pydantic import BaseModel

class PurchaseOrderDetail(BaseModel):
    purchase_order_id: int
    product_id: int
    quantity: int
    total: int