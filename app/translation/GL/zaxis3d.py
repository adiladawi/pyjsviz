from typing import Any, Optional, Union , Literal
from pydantic import BaseModel
from textstyle import TextStyle
from axisline import AxisLine
from axislabel import AxisLabel
from axistick import AxisTick
from splitline import SplitLine
from splitarea import SplitArea
from axispointer import AxisPointer

class Data(BaseModel):
    value: Optional[Any]
    textStyle: Any = TextStyle().dict()


class ZAxis3D(BaseModel):
    show: Optional[bool]
    name: str = 'X'
    grid3DIndex: int = 0
    nameTextStyle: Any = TextStyle().dict()
    nameGap: int = 20
    type: Literal['value','category','time', 'log'] = 'value'
    min: Optional[Union[Literal['dataMin'],int]]
    max: Optional[Union[Literal['dataMax'],int]]
    scale: bool = False
    splitNumber: int = 5
    minInterval: int = 0
    interval: Optional[int]
    logBase: int = 10
    data: Any = TextStyle().dict()
    axisLine: Any = AxisLine().dict()
    axisLabel: Any = AxisLabel().dict()
    axisTick: Any = AxisTick().dict()
    splitLine: Any = SplitLine().dict()
    splitArea: Any = SplitArea().dict()
    axisPointer: Any = AxisPointer().dict()