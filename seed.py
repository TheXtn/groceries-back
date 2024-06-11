
from database import get_connection
from models.product import Product
from models.category import Category

mock_products = [
    Product( name="Apple", weight=0.2, quantity=10, price=1.99, category=Category.fruits),
    Product( name="Banana", weight=0.15, quantity=15, price=1.49, category=Category.fruits),
    Product( name="Carrot", weight=0.1, quantity=20, price=0.99, category=Category.vegetables),
    Product( name="Potato", weight=0.3, quantity=12, price=0.79, category=Category.vegetables),
    Product( name="Chicken Breast", weight=0.5, quantity=8, price=3.99, category=Category.meats),
    Product( name="Salmon Fillet", weight=0.6, quantity=6, price=5.99, category=Category.meats),
    Product( name="Milk", weight=1.0, quantity=5, price=2.49, category=Category.all),
    Product( name="Bread", weight=0.4, quantity=7, price=1.29, category=Category.all),
    Product( name="Orange", weight=0.25, quantity=10, price=1.79, category=Category.fruits),
    Product( name="Beef Steak", weight=0.7, quantity=4, price=7.99, category=Category.meats),
]

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    for product in mock_products:
        cursor.execute("INSERT INTO products (name, weight, quantity, price, category) VALUES (?, ?, ?, ?, ?)",
                       (product.name, product.weight, product.quantity, product.price, product.category.value))
    conn.commit()

seed_database()