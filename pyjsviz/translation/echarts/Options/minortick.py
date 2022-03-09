from typing import Any

from linestyle import LineStyle
from pydantic import BaseModel


class MinorTick(BaseModel):
    show: bool = False
    splitNumber: int = 5
    length: int = 3
    lineStyle: Any = LineStyle().dict()
