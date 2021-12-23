from datetime import datetime
from sqlalchemy import Table, Column, engine
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime, Integer, String
from config.db import meta, engine

purchaseOrders = Table('purchase_order', meta, 
    Column('id', Integer, primary_key=True), 
    Column('provider_id', Integer), 
    Column('date', DateTime),
    Column('total', DECIMAL),
    Column('created_at', DateTime, default = datetime.now),
    Column('updated_at', DateTime, default = datetime.now, onupdate=datetime.now) 
)

meta.create_all(engine)