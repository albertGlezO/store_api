from datetime import datetime
from sqlalchemy import Table, Column, engine
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime, Integer, String
from config.db import meta, engine

products = Table('product', meta, 
    Column('id', Integer, primary_key=True), 
    Column('name', String(255)), 
    Column('description', String(255)),
    Column('stock', Integer),
    Column('cost', DECIMAL),
    Column('created_at', DateTime, default = datetime.now),
    Column('updated_at', DateTime, default = datetime.now, onupdate=datetime.now) 
)

meta.create_all(engine)