#Author Hubert Wawszczak

from pydantic import BaseModel, Field
from typing import Optional

class Person(BaseModel):
    id: Optional[int] = None
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
