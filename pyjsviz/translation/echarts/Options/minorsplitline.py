from typing import Any

from linestyle import LineStyle
from pydantic import BaseModel


class MinorSplitLine(BaseModel):
    show: bool = False
    lineStyle: Any = LineStyle().dict()
