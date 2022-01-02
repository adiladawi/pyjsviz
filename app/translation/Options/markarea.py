from typing import List, Optional, Literal, Union, Dict, Any
from pydantic import BaseModel
from label import Label
from itemstyle import ItemStyle
from blur import Blur

class Emphasis(BaseModel):
	label: Any = Label().dict()
	itemStyle: Any = ItemStyle().dict()


class DataStart(BaseModel):
	name: str = 'start'
	x : Optional[int]
	y : Optional[int]
	value: Optional[int]
	itemStyle: Any = ItemStyle().dict()
	label: Any = Label().dict()
	emphasis: Any = Emphasis().dict()
	blur: Any = Blur().dict()
	

class DataEnd(BaseModel):
	name: str = 'end'
	x : Optional[int]
	y : Optional[int]
	value: Optional[int]
	itemStyle: Any = ItemStyle().dict()
	label: Any = Label().dict()
	emphasis: Any = Emphasis().dict()
	blur: Any = Blur().dict()

class MarkArea(BaseModel):
	silent: bool = False
	label: Any = Label().dict()
	itemStyle: Any = ItemStyle().dict()
	emphasis: Any = Emphasis().dict()
	blur: Any = Blur().dict()
	data: Dict[int,Any] = {0:DataStart().dict(), 1:DataEnd().dict()}
	animation: bool = True
	animationThreshold: int = 2000
	animationDuration: int = 1000
	animationEasing: Literal['quinticInOut','linear','quadraticIn','quadraticInOut','cubicIn','cubicOut','cubicInOut','quarticIn','quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut' , 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut','backIn','backOut', 'backInOut','bounceIn','bounceOut','bounceInOut'] = 'cubicOut'
	animationDelay: int = 0
	animationDurationUpdate: int = 300
	animationEasingUpdate: Literal['quinticInOut','linear','quadraticIn','quadraticInOut','cubicIn','cubicOut','cubicInOut','quarticIn','quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut' , 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut','backIn','backOut', 'backInOut','bounceIn','bounceOut','bounceInOut'] = 'cubicOut'
	animationDelayUpdate: int = 0
