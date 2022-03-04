from typing import Any
from pydantic import BaseModel
from linestyle import LineStyle
from label import Label


class AxisPointer(BaseModel):
    show: bool = True
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()