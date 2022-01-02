from typing import Any, Optional
from pydantic import BaseModel
from textstyle import TextStyle


class Label(BaseModel):
    show: bool = False
    distance: Optional[int]
    formatter: Optional[Any]
    textStyle: Any = TextStyle().dict()