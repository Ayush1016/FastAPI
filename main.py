from fastapi import FastAPI
from Mockdata import Products
app = FastAPI()


@app.get("/Products")
async def get_products():
    return Products


@app.get("/Products/{id}")
async def get_products(id: int):
    for product in Products:
        if product["id"]==id:
            return product
    return {"message":"Product not found"}
