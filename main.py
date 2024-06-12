
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection, create_table
from dtos.category_dto import CategoryUpdate
from models.category import Category
from models.product import Product
from dtos.product_dto import ProductCreate, ProductUpdate

app = FastAPI()
create_table()
## ENABLING CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



## ENDPOINT TO GET ALL PRODUCTS
@app.get("/products")
async def get_products(category: Category = None):
    conn = get_connection()
    cursor = conn.cursor()
    if category:
        cursor.execute("SELECT * FROM products WHERE category=?", (category.value,))
    else:
        cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    products_list = []
    for product in products:
        product_dict = {
            "id": product[0],
            "name": product[1],
            "weight": product[2],
            "quantity": product[3],
            "price": product[4],
            "category": Category(product[5]).name
        }
        products_list.append(product_dict)
    return products_list

## ENDPOINT TO GET PRODUCT BY ID
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")
## ENDPOINT TO CREATE PRODUCT
@app.post("/products")
async def create_product(product_create: ProductCreate):
    conn = get_connection()
    cursor = conn.cursor()
    
    new_product = Product(**product_create.dict())  
    cursor.execute("INSERT INTO products (name, weight, quantity, price, category) VALUES (?, ?, ?, ?,?)",
                   (new_product.name, new_product.weight, new_product.quantity, new_product.price, new_product.category))
    conn.commit()
    return {"message": "Product created successfully", "product": new_product}
## ENDPOINT TO UPDATE PRODUCT CATEGORY
@app.put("/products/{product_id}/category")
async def update_product_category(product_id: int, category_update: CategoryUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()
    if product:
        cursor.execute("UPDATE products SET category=? WHERE id=?", (category_update.name, product_id))
        conn.commit()
        return {"message": "Product category updated successfully", "product_id": product_id, "new_category": category_update.name}
    else:
        raise HTTPException(status_code=404, detail="Product not found")
## ENDPOINT TO DELETE PRODUCT
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        deleted_product = Product(id=product_id)
        return {"message": "Product deleted successfully", "product": deleted_product}
