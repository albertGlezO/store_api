from fastapi import APIRouter
from config.db import conn
from models.purchaseOrder import purchaseOrders
from schemas.purchaseOrder import PurchaseOrder

purchaseOrder = APIRouter()

@purchaseOrder.get('/purchaseOrder', tags=['Purchase Order'])
def index():
    try:
        result = conn.execute(purchaseOrders.select()).fetchall()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrder.get('/purchaseOrder/{id}', tags=['Purchase Order'])
def show(id: int):
    try:
        result =  conn.execute(purchaseOrders.select().where(purchaseOrders.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrder.post('/purchaseOrder', tags=['Purchase Order'])
def create(purchaseOrder: PurchaseOrder):
    try:
        data = {'provider_id' : purchaseOrder.provider_id, 'date' : purchaseOrder.date, 'total' : purchaseOrder.total}
        result = conn.execute(purchaseOrders.insert().values(data))
        result = conn.execute(purchaseOrders.select().where(purchaseOrders.c.id == result.lastrowid)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrder.put('/purchaseOrder/{id}', tags=['Purchase Order'])
def update(id: int, purchaseOrder: PurchaseOrder):
    try:
        conn.execute(purchaseOrders.update().values(provider_id=purchaseOrder.provider_id, date=purchaseOrder.date, total=purchaseOrder.total).where(purchaseOrders.c.id == id))
        result = conn.execute(purchaseOrders.select().where(purchaseOrders.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@purchaseOrder.delete('/purchaseOrder/{id}', tags=['Purchase Order'])
def destroy(id: int):
    try:
        conn.execute(purchaseOrders.delete().where(purchaseOrders.c.id == id))
        return ({'status' : True, 'data' : [], 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})