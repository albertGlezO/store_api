from datetime import datetime
from sqlalchemy import Table, Column, engine
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta, engine

providers = Table('provider', meta, 
    Column('id', Integer, primary_key=True), 
    Column('name', String(255)), 
    Column('full_address', String(255)),
    Column('created_at', DateTime, default = datetime.now),
    Column('updated_at', DateTime, default = datetime.now, onupdate=datetime.now) 
)

meta.create_all(engine)