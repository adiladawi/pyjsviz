


from typing import List
from pydantic import BaseModel


class AreaStyle(BaseModel):
    color: List[str] = ['rgba(250,250,250,0.3)','rgba(200,200,200,0.3)']