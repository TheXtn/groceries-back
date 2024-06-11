
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection, create_table
from models.product import Product
from dtos.product_dto import ProductCreate, ProductUpdate

app = FastAPI()
create_table()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/products")
@app.get("/products")
async def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    products_list = []
    for product in products:
        print(product)
        product_dict = {
            "id": product[0],
            "name": product[1],
            "weight": product[2],
            "quantity": product[3],
            "price": product[4],
            "category":product[5]
        }
        products_list.append(product_dict)
    return products_list

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

@app.post("/products")
async def create_product(product_create: ProductCreate):
    conn = get_connection()
    cursor = conn.cursor()
    
    new_product = Product(**product_create.dict())  
    cursor.execute("INSERT INTO products (name, weight, quantity, price, category) VALUES (?, ?, ?, ?,?)",
                   (new_product.name, new_product.weight, new_product.quantity, new_product.price, new_product.category))
    conn.commit()
    return {"message": "Product created successfully", "product": new_product}

@app.put("/products/{product_id}")
async def update_product(product_id: int, product_update: ProductUpdate):
    conn = get_connection()
    cursor = conn.cursor()
    updated_product = Product(**product_update.dict())
    cursor.execute("UPDATE products SET name=?, weight=?, quantity=?, price=? WHERE id=?",
                   (updated_product.name, updated_product.weight, updated_product.quantity,
                    updated_product.price, product_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        updated_product.id = product_id
        return {"message": "Product updated successfully", "product": updated_product}

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
