from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from axislabel import AxisLabel
from axisline import AxisLine
from axispointer import AxisPointer
from axistick import AxisTick
from minorsplitline import MinorSplitLine
from minortick import MinorTick
from pydantic import BaseModel
from splitarea import SplitArea
from splitline import SplitLine
from textstyle import TextStyle
from tooltip import ToolTip


class Data(BaseModel):
    value: Optional[str]
    textStyle: Any = TextStyle().dict()


class SingleAxis(BaseModel):
    id: Optional[str]
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "5%"
    top: Union[int, str] = "5%"
    right: Union[int, str] = "5%"
    bottom: Union[int, str] = "5%"
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    orient: Literal["horizontal", "vertical"] = "horizontal"
    type: Literal["value", "category", "time", "log"] = "value"
    name: Optional[str]
    nameLocation: Literal["end", "start", "middle", "center"] = "end"
    nameTextStyle: Any = TextStyle().dict()
    nameGap: int = 15
    nameRotate: Optional[int]
    inverse: bool = False
    boundaryGap: Optional[Union[bool, int]]
    min: Optional[Union[Literal["dataMin"], int]]
    max: Optional[Union[Literal["dataMax"], int]]
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
    tooltip: Any = ToolTip().dict()
