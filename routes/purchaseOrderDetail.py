from fastapi import APIRouter
from config.db import conn
from models.purchaseOrderDetail import purchaseOrdersDetails
from schemas.purchaseOrderDetail import PurchaseOrderDetail

purchaseOrderDetail = APIRouter()

@purchaseOrderDetail.get('/purchaseOrderDetail', tags=['Purchase Order Detail'])
def index():
    try:
        result = conn.execute(purchaseOrdersDetails.select()).fetchall()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrderDetail.get('/purchaseOrderDetail/{id}', tags=['Purchase Order Detail'])
def show(id: int):
    try:
        result =  conn.execute(purchaseOrdersDetails.select().where(purchaseOrdersDetails.c.purchase_order_id == id)).fetchall()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrderDetail.post('/purchaseOrderDetail', tags=['Purchase Order Detail'])
def create(purchaseOrderDetail: PurchaseOrderDetail):
    try:
        data = {'purchase_order_id' : purchaseOrderDetail.purchase_order_id, 'product_id' : purchaseOrderDetail.product_id, 'quantity' : purchaseOrderDetail.quantity, 'total' : purchaseOrderDetail.total}
        conn.execute(purchaseOrdersDetails.insert().values(data))
        result = conn.execute(purchaseOrdersDetails.select().where(purchaseOrdersDetails.c.purchase_order_id == purchaseOrderDetail.purchase_order_id, purchaseOrdersDetails.c.product_id == purchaseOrderDetail.product_id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrderDetail.put('/purchaseOrderDetail/{purchase_order_id}/{product_id}', tags=['Purchase Order Detail'])
def update(purchase_order_id: int, product_id: int, purchaseOrderDetail: PurchaseOrderDetail):
    try:
        conn.execute(purchaseOrdersDetails.update().values(purchase_order_id=purchaseOrderDetail.purchase_order_id, product_id=purchaseOrderDetail.product_id, quantity=purchaseOrderDetail.quantity, total=purchaseOrderDetail.total).where(purchaseOrdersDetails.c.purchase_order_id == purchase_order_id, purchaseOrdersDetails.c.product_id == product_id))
        result = conn.execute(purchaseOrdersDetails.select().where(purchaseOrdersDetails.c.purchase_order_id == purchaseOrderDetail.purchase_order_id, purchaseOrdersDetails.c.product_id == purchaseOrderDetail.product_id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrderDetail.delete('/purchaseOrderDetail/{purchase_order_id}/{product_id}', tags=['Purchase Order Detail'])
def destroy(purchase_order_id: int, product_id: int):
    try:
        conn.execute(purchaseOrdersDetails.delete().where(purchaseOrdersDetails.c.purchase_order_id == purchase_order_id, purchaseOrdersDetails.c.product_id == product_id))
        return ({'status' : True, 'data' : [], 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})