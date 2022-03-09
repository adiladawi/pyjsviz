from typing import Any

from itemstyle import ItemStyle
from pydantic import BaseModel


class Progress(BaseModel):
    show: bool = False
    overlap: bool = True
    width: int = 10
    roundCap: bool = False
    clip: bool = False
    itemStyle: Any = ItemStyle().dict()
