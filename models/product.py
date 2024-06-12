
from pydantic import BaseModel

from models.category import Category


class Product(BaseModel):
    id: int = None
    name: str
    weight: float
    quantity: int
    price: float
    category: Category

