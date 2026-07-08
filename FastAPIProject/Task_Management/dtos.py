from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    name: str
    price: float=0