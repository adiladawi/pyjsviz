from typing import Optional
from pydantic import BaseModel

class ShadowStyle(BaseModel):
	color: str = 'rgba(150,150,150,0.3)'
	shadowBlur: Optional[int]
	shadowColor: Optional[str]
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0
	opacity: Optional[float]
