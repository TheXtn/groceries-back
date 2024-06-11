
from pydantic import BaseModel
from enum import Enum

from models.category import Category


class Product(BaseModel):
    id: int = None
    name: str
    weight: float
    quantity: int
    price: float
    category: Category

