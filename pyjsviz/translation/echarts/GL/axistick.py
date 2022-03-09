from typing import Any

from linestyle import LineStyle
from pydantic import BaseModel


class AxisTick(BaseModel):
    show: bool = True
    interval: Any = "auto"
    length: int = 5
    lineStyle: Any = LineStyle().dict()
