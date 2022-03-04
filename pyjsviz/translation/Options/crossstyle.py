from typing import Optional, Literal,List, Union
from pydantic import BaseModel

class CrossStyle(BaseModel):
    color: str = '#555'
    width: int = 1
    type: Union[str,int, List[int]] = 'dashed'
    dashOffset: int = 0
    cap: Literal['butt','round','square'] = 'butt'
    join: Literal['bevel','round','miter'] = 'bevel'
    miterLimit: int = 10
    shadowBlur: Optional[int]
    shadowColor: Optional[str]
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    opacity: float = 0.45