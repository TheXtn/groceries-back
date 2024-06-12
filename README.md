# Groceries-Back

This is a FastAPI-based backend service for managing grocery products. The service supports CRUD operations for products, including filtering by categories. The products have attributes such as name, weight, quantity, price, and category. Categories include fruits, meats, vegetables, and all.

## Project Features

- **CRUD Operations**: Create, Read, Update, and Delete products.
- **Filter Products by Category**: Retrieve products based on their category.
- **Update Product Category**: Update the category of an existing product.
- **Database Initialization**: Automatically creates the necessary database table and seeds it with mock data.

## Project Structure

groceries-back/
│
├── main.py                # The main FastAPI application
├── database.py            # Database connection and table creation
├── models/
│   ├── product.py         # Product model
│   └── category.py        # Category enumeration
├── dtos/
│   ├── product_dto.py     # Data Transfer Objects for products
│   └── category_dto.py    # Data Transfer Objects for categories
├── mock_products.py       # Mock data for seeding the database
├── requirements.txt       # Project dependencies
├── Dockerfile             # Docker configuration
└── README.md              # Project documentation

## How to Run

### Normal Method

1. **Clone the repository:**
    ```git clone https://github.com/TheXtn/groceries-back.git
    cd groceries-back
2. **Install the dependencies:**
    ```pip install -r requirements.txt
3. **Run using fastapi**
    ```fastapi dev main.py
    
### Docker Method

1. **Clone the repository:**
    ```git clone https://github.com/TheXtn/groceries-back.git
    cd groceries-back

2. **Build the Docker image:**
    ```docker build -t groceries-back .


3. **Run the Docker container:**
    docker run -d -p 8000:8000 groceries-back

## API Endpoints

- **GET /products**: Retrieve all products or filter by category.
- **GET /products/{product_id}**: Retrieve a specific product by ID.
- **POST /products**: Create a new product.
- **PUT /products/{product_id}**: Update an existing product.
- **PUT /products/{product_id}/category**: Update the category of a specific product.
- **DELETE /products/{product_id}**: Delete a specific product.