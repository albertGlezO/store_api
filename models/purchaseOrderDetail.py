from datetime import datetime
from sqlalchemy import Table, Column, engine
from sqlalchemy.sql.sqltypes import DECIMAL, DateTime, Integer, String
from config.db import meta, engine

purchaseOrdersDetails = Table('purchase_order_detail', meta, 
    Column('purchase_order_id', Integer), 
    Column('product_id', Integer), 
    Column('quantity', DECIMAL),
    Column('total', DECIMAL),
    Column('created_at', DateTime, default = datetime.now),
    Column('updated_at', DateTime, default = datetime.now, onupdate=datetime.now) 
)

meta.create_all(engine)