from typing import Optional
from pydantic import BaseModel


class Movie(BaseModel):  # By default it already inherits several things, such as data validation!
    id: Optional[int] = None  # is optional
    title: str
    overview: str
