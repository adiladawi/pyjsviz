from typing import Optional
from pydantic import BaseModel

class Handle(BaseModel):
	show: bool = False
	icon: Optional[str]
	size: int = 45
	margin: int = 50
	color: str = '#333'
	throttle: int = 40
	shadowBlur: int = 3
	shadowColor: str = '#aaa'
	shadowOffsetX: int = 2
	shadowOffsetY: int = 0
