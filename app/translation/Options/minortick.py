from pydantic import BaseModel
from linestyle import LineStyle
from typing import Any


class MinorTick(BaseModel):
	show: bool = False
	splitNumber: int = 5
	length: int = 3
	lineStyle: Any = LineStyle().dict()