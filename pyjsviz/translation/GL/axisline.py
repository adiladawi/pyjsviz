from typing import Any
from pydantic import BaseModel
from linestyle import LineStyle


class AxisLine(BaseModel):
    show: bool = True
    interval: Any = 'auto'
    lineStyle: Any = LineStyle().dict()