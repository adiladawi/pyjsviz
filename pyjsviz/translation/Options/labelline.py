from typing import Optional, Union, Any
from pydantic import BaseModel
from linestyle import LineStyle

class LabelLine(BaseModel):
	show: Optional[bool]
	showAbove: Optional[bool]
	length2: Optional[int]
	smooth: Union[bool,float] = False
	minTurnAngle: Optional[int]
	lineStyle: Any = LineStyle().dict()