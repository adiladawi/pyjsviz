from pydantic import BaseModel
from linestyle import LineStyle
from typing import Any


class MinorSplitLine(BaseModel):
    show: bool = False
    lineStyle: Any = LineStyle().dict()