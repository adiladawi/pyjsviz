from typing import Optional, Literal
from pydantic import BaseModel


class HandleStyle(BaseModel):
	color: str = '#fff'
	borderColor: str = '#ACB8D1'
	borderWidth: int = 0
	borderType: Literal['solid','dashed','dotted'] = 'solid'
	shadowBlur: Optional[int]
	shadowColor: Optional[str]
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0
	opacity: Optional[float]
