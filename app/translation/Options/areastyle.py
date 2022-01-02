from typing import List, Optional
from pydantic import BaseModel

class AreaStyle(BaseModel):
	color: List[str] = ['rgba(250,250,250,0.3)','rgba(200,200,200,0.3)']
	shadowBlur: Optional[int] 
	shadowColor: Optional[str]
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0
	opacity: Optional[float]