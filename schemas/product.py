from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description:str
    stock:int
    cost:int