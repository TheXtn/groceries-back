
from pydantic import BaseModel

from models.category import Category



class ProductCreate(BaseModel):
    name: str
    weight: float
    quantity: int
    price: float
    category: Category



class ProductUpdate(BaseModel):
    name: str
    weight: float
    quantity: int
    price: float
    category: Category

