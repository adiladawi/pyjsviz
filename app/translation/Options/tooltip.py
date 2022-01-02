from typing import List, Optional, Union, Literal, Any
from pydantic import BaseModel
from axispointer import AxisPointer
from textstyle import TextStyle

class ToolTip(BaseModel):
	show: bool = True
	trigger: Literal['item','axis','none'] = 'item'
	axisPointer: Any = AxisPointer().dict()
	showContent: bool = True
	alwaysShowContent: bool = False
	triggerOn: Literal['mousemove|click', 'mousemove','click','none'] = 'mousemove|click'
	showDelay: int = 0
	hideDelay: int = 100
	enterable: bool = True
	renderMode: Literal['html', 'richText'] = 'html'
	confine: bool = False
	appendToBody: bool = False
	className: Optional[str]
	transitionDuration: float = 0.4
	position: Optional[Union[Literal['inside', 'top','left','right','bottom'],List[Any]]]
	formatter: Optional[str]
	backgroundColor: str = 'rgba(50,50,50,0.7)'
	borderColor: str = '#333'
	borderWidth: int = 0
	padding: Union[int, List[int]] = 5
	textStyle: Any = TextStyle().dict()
	extraCssText: Optional[str]
	order: Literal['seriesAsc', 'seriesDesc','valueAsc','valueDesc'] = 'seriesAsc'