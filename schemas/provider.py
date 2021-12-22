from pydantic import BaseModel

class Provider(BaseModel):
    name: str
    full_address:str