from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    price: float
    quantity: int
