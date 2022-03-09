from typing import Any
from typing import Literal
from typing import Optional
from typing import Union

from axislabel import AxisLabel
from axisline import AxisLine
from axispointer import AxisPointer
from axistick import AxisTick
from pydantic import BaseModel
from splitarea import SplitArea
from splitline import SplitLine
from textstyle import TextStyle


class Data(BaseModel):
    value: Optional[Any]
    textStyle: Any = TextStyle().dict()


class YAxis3D(BaseModel):
    show: Optional[bool]
    name: str = "X"
    grid3DIndex: int = 0
    nameTextStyle: Any = TextStyle().dict()
    nameGap: int = 20
    type: Literal["value", "category", "time", "log"] = "value"
    min: Optional[Union[Literal["dataMin"], int]]
    max: Optional[Union[Literal["dataMax"], int]]
    scale: bool = False
    splitNumber: int = 5
    minInterval: int = 0
    interval: Optional[int]
    logBase: int = 10
    data: Any = Data().dict()
    axisLine: Any = AxisLine().dict()
    axisLabel: Any = AxisLabel().dict()
    axisTick: Any = AxisTick().dict()
    splitLine: Any = SplitLine().dict()
    splitArea: Any = SplitArea().dict()
    axisPointer: Any = AxisPointer().dict()
