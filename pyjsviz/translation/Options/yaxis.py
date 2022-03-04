from typing import List, Optional, List, Union, Literal, Any
from pydantic import BaseModel
from textstyle import TextStyle
from axisline import AxisLine
from axistick import AxisTick
from minortick import MinorTick
from axislabel import AxisLabel
from splitline import SplitLine
from minorsplitline import MinorSplitLine
from splitarea import SplitArea
from axispointer import AxisPointer

class Data(BaseModel):
	value: Optional[str]
	textStyle: Any = TextStyle().dict()


class YAxis(BaseModel):
	id :Optional[str]
	show: bool = True
	gridIndex: int = 0
	position: Optional[Literal['top','bottom']]
	offset: int = 0
	realtimeSort: bool = False
	sortSeriesIndex: int = 0
	type: Literal['category','value','time','log'] = 'category'
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
	splitLine: Any = SplitLine().dict()
	minorSplitLine: Any = MinorSplitLine().dict()
	splitArea: Any = SplitArea().dict()
	data: Any = [Data().dict()]
	axisPointer: Any = AxisPointer().dict()
	zlevel: int = 0
	z: int = 0