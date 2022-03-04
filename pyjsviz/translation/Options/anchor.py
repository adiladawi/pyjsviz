from typing import List, Literal,Any
from pydantic import BaseModel
from itemstyle import ItemStyle


class Anchor(BaseModel):
	show: bool = True
	showAbove: bool = False
	size: int = 6
	icon: Literal['default','emptyCircle','circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'] = 'default'
	offsetCenter: List[int] = [0, 0]
	keepAspect: bool = False
	itemStyle: Any = ItemStyle().dict()