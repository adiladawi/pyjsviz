from typing import List, Optional, Literal, Union, Any
from pydantic import BaseModel
from areastyle import AreaStyle

class SplitArea(BaseModel):
	interval: Optional[Union[Literal['auto'], int]] = 'auto'
	show: bool = False
	areaStyle: Any = AreaStyle().dict()
