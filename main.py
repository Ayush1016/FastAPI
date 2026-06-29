from fastapi import FastAPI
from Mockdata import Products
from dtos import ProductDTO
app = FastAPI()


# query param
@app.get("/Products")
async def get_products(total_products=2):
    return {"products":f"Total Products: {total_products}" }


# path params
@app.get("/Products/{id}")
async def get_products(id: int):
    for product in Products:
        if product["id"]==id:
            return product
    return {"message":"Product not found"}

@app.post("/create_products")
async def create_products(data: ProductDTO):
    data=data.model_dump()
    Products.append(data)
    return {"status":"Product created successfully","data":Products}
    # return {"message":"Product created"}
