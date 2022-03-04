from typing import Optional, Literal
from pydantic import BaseModel


class LineStyle(BaseModel):
	color: str = '#333'
	width: int = 1
	type: Literal['solid','dashed','dotted'] = 'solid'
	shadowBlur: Optional[int]
	shadowColor: Optional[str]
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0
	opacity: Optional[int]
