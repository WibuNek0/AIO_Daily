from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class UserInfo(BaseModel):
    name: str
    age: int
    email: str

class Product(BaseModel):
    name: str
    price: float
    description: str = ""

app = FastAPI()

products_db: List[Product] = []

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Bài 1: Hello API
@app.get("/hello")
def hello_api():
    return {"message": "Xin chào từ FastAPI!"}

# Bài 2: API Máy tính
@app.get("/add")
def add_numbers(a: float, b: float):
    result = a + b
    return {"result": result}

@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = a - b
    return {"result": result}

@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = a * b
    return {"result": result}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by 0!"}
    result = a / b
    return {"result": result}

# Bài 3: API Thông tin người dùng (POST)
@app.post("/user")
def create_user(user: UserInfo):
    is_adult = user.age >= 18
    return {
        "message": f"Received user info: {user.name}",
        "user_info": {
            "name": user.name,
            "age": user.age,
            "email": user.email,
            "is_adult": is_adult
        }
    }

# Bài 4: Quản lý danh sách sản phẩm
@app.get("/products")
def get_products():
    return {
        "message": "Products",
        "total": len(products_db),
        "products": products_db
    }

@app.post("/products")
def add_product(product: Product):
    products_db.append(product)
    return {
        "message": f"Add product: {product.name}",
        "product": product,
        "total_products": len(products_db)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
