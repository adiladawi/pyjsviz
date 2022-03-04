from typing import Union, Literal
from pydantic import BaseModel

class AxisTick(BaseModel):
	show: bool = True
	alignWithLabel: bool = False
	interval: Union[Literal['auto'],int] = 'auto'
	inside: bool = False
	length: int = 5