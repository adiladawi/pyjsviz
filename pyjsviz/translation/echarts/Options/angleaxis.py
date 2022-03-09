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


class Data(BaseModel):
    value: Optional[str]
    textStyle: Any = TextStyle().dict()


class AngleAxis(BaseModel):
    id: Optional[str]
    polarIndex: int = 0
    startAngle: int = 90
    clockwise: bool = True
    type: Literal["category", "value", "time", "log"] = "category"
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
    data: Any = Data().dict()
    axisPointer: Any = AxisPointer().dict()
    zlevel: int = 0
    z: int = 0


print(AngleAxis().json())
