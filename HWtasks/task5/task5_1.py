from fastapi import FastAPI
from pydantic import BaseModel
from .db import sample_products

app = FastAPI()

class Product(BaseModel):
    product_id : int
    name : str
    category : str
    price : float


@app.get("/product/{product_id}")
def get_product(product_id : int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    return {"message" : "Product not found!"}

@app.get("/products/search")
def get_products(keyword : str, category : str = "", limit : int = 10):
    result_products = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower() and category.lower() in product["category"].lower():
            result_products.append(product)

    return result_products[:limit]

