from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from areastyle import AreaStyle
from axislabel import AxisLabel
from axisline import AxisLine
from axistick import AxisTick
from minortick import MinorTick
from pydantic import BaseModel
from textstyle import TextStyle


class Data(BaseModel):
    value: Optional[str]
    textStyle: Any = TextStyle().dict()


class ParallelAxis(BaseModel):
    id: Optional[str]
    dim: Optional[int]
    parallelIndex: int = 0
    realtime: bool = True
    areaSelectStyle: Any = AreaStyle().dict()
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
    data: Any = [Data().dict()]
