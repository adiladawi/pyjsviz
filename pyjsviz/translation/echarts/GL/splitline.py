from typing import Any

from linestyle import LineStyle
from pydantic import BaseModel


class SplitLine(BaseModel):
    show: bool = True
    interval: Any = "auto"
    lineStyle: Any = LineStyle().dict()
