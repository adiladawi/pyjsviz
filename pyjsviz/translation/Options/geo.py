from typing import List, Optional, Union, Literal, Any
from pydantic import BaseModel
from label import Label
from itemstyle import ItemStyle
from selecte import Selecte

class Emphasis(BaseModel):
	focus: Literal['none','self'] = 'none'
	label: Any = Label().dict()
	itemStyle: Any = ItemStyle().dict()

class ScaleLimit(BaseModel):
	min: int = 1
	max: int = 1


class Select(BaseModel):
	label: Any =  Label().dict()
	itemStyle: Any = ItemStyle().dict()



class Regions(BaseModel):
	name :Optional[str]
	selected: bool = False
	itemStyle: dict = ItemStyle().dict()
	label: dict = Label().dict()
	emphasis: dict = Emphasis().dict()
	select: dict = Selecte().dict()



class Geo(BaseModel):
	id : Optional[str]
	show: bool = True
	map: str = ''
	roam: Literal[False,True,'scale','move'] = False
	center: Optional[List[int]]
	aspectScale: float = 0.75
	boundingCoords: Optional[List[int]]
	zoom: int = 1
	scaleLimit: Any = ScaleLimit().dict()
	nameMap: Optional[Any]
	nameProperty: str =  'name'
	selectedMode: Literal[False,'single','multiple'] = False
	label: Any = Label().dict()
	itemStyle: Any = ItemStyle().dict()
	emphasis: Any = Emphasis().dict()
	select: Any = Selecte().dict()
	zlevel: int = 0
	z: int = 2
	left: Union[int,str]  = 'auto'
	top: Union[int,str]  = 'auto'
	right: Union[int,str] = 'auto'
	bottom: Union[int,str] = 'auto'
	layoutCenter: Optional[List[int]]
	layoutSize :Optional[int]
	regions: Any = [Regions().dict()]
	silent: bool = False
