from typing import Any
from pydantic import BaseModel
from linestyle import LineStyle


class AxisTick(BaseModel):
    show: bool = True
    interval: Any = 'auto'
    length: int = 5
    lineStyle: Any = LineStyle().dict()