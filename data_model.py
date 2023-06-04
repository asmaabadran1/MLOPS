from pydantic import BaseModel
from typing import Optional

class sample_data(BaseModel):
    age: int
    name: str
    fav_numbers: list[int]
    country : Optional[str]