from typing import Any
from pydantic import BaseModel
from linestyle import LineStyle


class SplitLine(BaseModel):
    show: bool = True
    interval: Any = 'auto'
    lineStyle: Any = LineStyle().dict()