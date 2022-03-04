from typing import Optional, List, Union, Literal, Any
from pydantic import BaseModel
from textstyle import TextStyle
from axisline import AxisLine
from axistick import AxisTick
from minortick import MinorTick
from axislabel import AxisLabel

class Data(BaseModel):
	value: Optional[str]
	textStyle: Any = TextStyle().dict()
 


class ParallelAxisDefault(BaseModel):
	type: Literal['value','category','time','log'] = 'value'
	name :Optional[str] 
	nameLocation: Literal['end','start','middle','center'] = 'end'
	nameTextStyle: Any = TextStyle().dict()
	nameGap: int = 15
	nameRotate: Optional[int]
	inverse: bool = False
	boundaryGap: Optional[Union[bool, int]]
	min: Optional[Union[Literal['dataMin'], int]]
	max: Optional[Union[Literal['dataMax'], int]]
	scale: bool = False
	splitNumber: int = 5
	minInterval: int = 0
	maxInterval: Optional[int]
	interval: Optional[int]
	logBase: int = 10
	silent: bool = False
	triggerEvent: bool = False
	axisLine: Any = AxisLine().dict()
	axisTick: Any = AxisTick().dict()
	minorTick: Any = MinorTick().dict()
	axisLabel: Any = AxisLabel().dict()
	data: Any = Data().dict()


class Parallel(BaseModel):
	id :Optional[str]
	zlevel: int = 0
	z: int = 2
	left: Union[int,str] = 80
	top: Union[int,str] = 60
	right: Union[int,str] = 80
	bottom: Union[int,str] = 60
	width: Union[int,str] = 'auto'
	height: Union[int,str] = 'auto'
	layout: Literal['horizontal','vertical'] = 'horizontal'
	axisExpandable: bool = False
	axisExpandCenter :Optional[int]
	axisExpandCount: int = 0
	axisExpandWidth: int = 50
	axisExpandTriggerOn: Literal['click','mousemove'] = 'click'
	parallelAxisDefault: Any = ParallelAxisDefault().dict()