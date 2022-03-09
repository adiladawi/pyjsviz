from typing import Any

from label import Label
from linestyle import LineStyle
from pydantic import BaseModel


class AxisPointer(BaseModel):
    show: bool = True
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
