from typing import Any
from pydantic import BaseModel
from itemstyle import ItemStyle


class Progress(BaseModel):
	show: bool = False
	overlap: bool = True
	width: int = 10
	roundCap: bool = False
	clip: bool = False
	itemStyle: Any = ItemStyle().dict()