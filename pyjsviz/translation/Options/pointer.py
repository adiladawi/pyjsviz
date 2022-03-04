from typing import List, Optional, Union, Literal
from pydantic import BaseModel


class Pointer(BaseModel):
	show: bool = True
	icon: Optional[Literal['emptyCircle','circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none']]
	offsetCenter: List[int] = [0, 0]
	length: Union[int,str] = '60%'
	width: int = 6
	keepAspect: bool = False
