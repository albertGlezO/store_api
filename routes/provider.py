from fastapi import APIRouter
from config.db import conn
from models.provider import providers
from schemas.provider import Provider

provider = APIRouter()

@provider.get('/provider', tags=['Provider'])
def index():
    try:
        result = conn.execute(providers.select()).fetchall()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@provider.get('/provider/{id}', tags=['Provider'])
def show(id: int):
    try:
        result =  conn.execute(providers.select().where(providers.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@provider.post('/provider', tags=['Provider'])
def create(provider: Provider):
    try:
        data = {'name' : provider.name, 'full_address' : provider.full_address}
        result = conn.execute(providers.insert().values(data))
        result = conn.execute(providers.select().where(providers.c.id == result.lastrowid)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@provider.put('/provider/{id}', tags=['Provider'])
def update(id: int, provider: Provider):
    try:
        conn.execute(providers.update().values(name=provider.name, full_address=provider.full_address).where(providers.c.id == id))
        result = conn.execute(providers.select().where(providers.c.id == id)).first()
        return ({'status' : True, 'data' : result, 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})

@provider.delete('/provider/{id}', tags=['Provider'])
def destroy(id: int):
    try:
        conn.execute(providers.delete().where(providers.c.id == id))
        return ({'status' : True, 'data' : [], 'message' : 'Peticion realizada correctamente'})
    except Exception as ex:
        return ({'status' : False, 'data' : [], 'message' : 'Error inesperado'})