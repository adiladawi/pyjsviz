from typing import List, Optional, Union, Any
from pydantic import BaseModel
from tooltip import ToolTip

class Polar(BaseModel):
	id :Optional[str] 
	zlevel: int = 0
	z: int = 2
	center: List[Union[int,str]] = ['50%', '50%']
	radius: Optional[Union[int,str,List[Union[int,str]]]]
	tooltip: Any = ToolTip().dict()