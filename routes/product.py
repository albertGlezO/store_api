from fastapi import APIRouter
from config.db import conn
from models.product import products
from schemas.product import Product

product = APIRouter()

@product.get('/product', tags=['Product'])
def index():
    try:
        result = conn.execute(products.select()).fetchall()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@product.get('/product/{id}', tags=['Product'])
def show(id: int):
    try:
        result =  conn.execute(products.select().where(products.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@product.post('/product', tags=['Product'])
def create(product: Product):
    try:
        data = {'name' : product.name, 'description' : product.description, 'stock': product.stock, 'cost': product.cost}
        result = conn.execute(products.insert().values(data))
        result = conn.execute(products.select().where(products.c.id == result.lastrowid)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@product.put('/product/{id}', tags=['Product'])
def update(id: int, product: Product):
    try:
        conn.execute(products.update().values(name=product.name, description=product.description, stock=product.stock, cost=product.cost).where(products.c.id == id))
        result = conn.execute(products.select().where(products.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@product.delete('/product/{id}', tags=['Product'])
def destroy(id: int):
    try:
        conn.execute(products.delete().where(products.c.id == id))
        return ({'status' : True, 'data' : [], 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})