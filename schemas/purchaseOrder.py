from pydantic import BaseModel

class PurchaseOrder(BaseModel):
    provider_id: int
    date: str
    total: int