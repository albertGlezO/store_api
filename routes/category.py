from fastapi import APIRouter
from config.db import conn
from models.category import categories
from schemas.category import Category

category = APIRouter()

@category.get('/category', tags=['Category'])
def index():
    try:
        result = conn.execute(categories.select()).fetchall()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@category.get('/category/{id}', tags=['Category'])
def show(id: int):
    try:
        result =  conn.execute(categories.select().where(categories.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@category.post('/category', tags=['Category'])
def create(category: Category):
    try:
        data = {'name' : category.name, 'description' : category.description}
        result = conn.execute(categories.insert().values(data))
        result = conn.execute(categories.select().where(categories.c.id == result.lastrowid)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@category.put('/category/{id}', tags=['Category'])
def update(id: int, category: Category):
    try:
        conn.execute(categories.update().values(name=category.name, description=category.description).where(categories.c.id == id))
        result = conn.execute(categories.select().where(categories.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@category.delete('/category/{id}', tags=['Category'])
def destroy(id: int):
    try:
        conn.execute(categories.delete().where(categories.c.id == id))
        return ({'status' : True, 'data' : [], 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})