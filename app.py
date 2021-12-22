from fastapi import FastAPI
from routes.category import category
from routes.product import product
from routes.provider import provider
from routes.purchaseOrder import purchaseOrder
from routes.purchaseOrderDetail import purchaseOrderDetail

app = FastAPI(
    title       =   "HMH Sistemas [STORE-API]",
    description =   "Ejercicio Backend Store",
    version     =   "0.1"
)

app.include_router(category)
app.include_router(product)
app.include_router(provider)
app.include_router(purchaseOrder)
app.include_router(purchaseOrderDetail)