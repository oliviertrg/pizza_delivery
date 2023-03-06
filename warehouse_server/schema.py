from pydantic import BaseModel,EmailStr
from typing import Optional


class Order(BaseModel):
    pizza_size : str
    flavour : str
    quantity : int