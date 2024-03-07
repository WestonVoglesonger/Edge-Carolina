from pydantic import BaseModel, HttpUrl

class ProductData(BaseModel):
    id: int
    name: str
    description: str
    url: str