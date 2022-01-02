from typing import Any, Optional, Literal, Union
from pydantic import BaseModel
from linestyle import LineStyle

class SplitLine(BaseModel):
	show: bool = True
	interval: Optional[Union[Literal['auto'], int]] = 'auto'
	lineStyle: Any = LineStyle().dict()