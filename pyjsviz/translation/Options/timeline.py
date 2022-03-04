from typing import Optional, List, Union, Literal, Any
from pydantic import BaseModel
from linestyle import LineStyle
from label import Label
from itemstyle import ItemStyle


class Progress(BaseModel):
	lineStyle: Any = LineStyle().dict()
	itemStyle: Any = ItemStyle().dict()
	label: Any = Label().dict()


class CheckpointStyle(BaseModel):
	symbol: Union[Literal['circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'],str] = 'circle'
	symbolSize: Union[int,List[int]] = 13
	symbolRotate: Optional[int]
	symbolKeepAspect: bool = False
	symbolOffset: List[int] = [0, 0]
	color: str = '#316bf3'
	borderColor: str = '#fff'
	borderWidth: int = 2
	borderType: Literal['solid','dashed','dotted'] = 'solid'
	borderDashOffset: int = 0
	borderCap: Literal['butt','round','square'] = 'butt'
	borderJoin: Literal['bevel','round','miter'] = 'bevel'
	borderMiterLimit: int = 10
	shadowBlur: int = 2
	shadowColor: str = 'rgba(0, 0, 0, 0.3)'
	shadowOffsetX: int = 1
	shadowOffsetY: int = 1
	opacity: Optional[int]
	animation: bool = True
	animationDuration: int = 300
	animationEasing: Literal['quinticInOut','linear','quadraticIn','quadraticInOut','cubicIn','cubicOut','cubicInOut','quarticIn','quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut' , 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut','backIn','backOut', 'backInOut','bounceIn','bounceOut','bounceInOut'] = 'quinticInOut'


class ControlStyle(BaseModel):
	show: bool = True
	showPlayBtn: bool = True
	showPrevBtn: bool = True
	showNextBtn: bool = True
	itemSize: int = 22
	itemGap: int = 12
	position: Literal['left','right','top','bottom'] = 'left'
	playIcon: Optional[str] 
	stopIcon: Optional[str]
	prevIcon: Optional[str]
	nextIcon: Optional[str]
	color: str = '#A4B1D7'
	borderColor: str = '#A4B1D7'
	borderWidth: int = 1
	borderType: Literal['solid','dashed','dotted'] = 'solid'
	borderDashOffset: int = 0
	borderCap: Literal['butt','round','square'] = 'butt'
	borderJoin: Literal['bevel','round','miter'] = 'bevel'
	borderMiterLimit: int = 10
	shadowBlur: Optional[int]
	shadowColor: Optional[str]
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0
	opacity: Optional[int]

class Emphasis(BaseModel):
    label: Any = Label
    itemStyle: Any = ItemStyle().dict()
    checkpointStyle: Optional[dict] #CheckpointStyle().dict()
    controlStyle: Optional[dict] #ControlStyle().dict()

class TimeLine(BaseModel):
	show: bool = True
	type: Literal['slider'] = 'slider'
	axisType: Literal['time','category','value'] = 'time'
	currentIndex: int = 0
	autoPlay: bool = False
	rewind: bool = False
	loop: bool = True
	playInterval: int = 2000
	realtime: bool = True
	replaceMerge: Union[str, List[str]] = 'undefined'
	controlPosition: Literal['left','right'] = 'left'
	zlevel: int = 0
	z: int = 2
	left: Union[int,str]  = 'auto'
	top: Union[int,str]  = 'auto'
	right: Union[int,str] = 'auto'
	bottom: Union[int,str] = 'auto'
	padding: Union[int,List[int]] = 5
	orient: Literal['horizontal','vertical'] = 'horizontal'
	inverse: bool = False
	symbol: Literal['emptyCircle', 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'] = 'emptyCircle'
	symbolSize: int = 10
	symbolRotate: Optional[int]
	symbolKeepAspect: bool = False
	symbolOffset: List[int] = [0, 0]
	lineStyle: Any = LineStyle().dict()
	label: Any = Label().dict()
	itemStyle: Any = ItemStyle().dict()
	checkpointStyle: Any = CheckpointStyle().dict()
	controlStyle: Any = ControlStyle().dict()
	progress: Any = Progress().dict()
	emphasis: Any = Emphasis().dict()
	data: Optional[List[Any]]