from typing import Any, Optional, Union
from pydantic import BaseModel
from linestyle import LineStyle
from axisline import AxisLine
from axislabel import AxisLabel
from axistick import AxisTick
from splitline import SplitLine
from splitarea import SplitArea
from axispointer import AxisPointer


class Grid3D(BaseModel):
    show: Optional[bool]
    boxWidth: int = 100
    boxHeight: int = 100
    boxDepth: int = 100
    axisLine: Any = AxisLine().dict()
    axisLabel: Any = AxisLabel().dict()
    axisTick: Any = AxisTick().dict()
    splitLine: Any = SplitLine().dict()
    splitArea: Any = SplitArea().dict()
    axisPointer: Any = AxisPointer().dict()
    environment: str = 'auto'
    light: Any = LineStyle().dict()
    postEffect: Any = LineStyle().dict()
    temporalSuperSampling: Any = LineStyle().dict()
    viewControl: Any = LineStyle().dict()
    zlevel: int = -10
    left: Union[int,str] = 'auto'
    top: Union[int,str] = 'auto'
    right: Union[int,str] = 'auto'
    bottom: Union[int,str] = 'auto'
    width: Union[int,str] = 'auto'
    height: Union[int,str] = 'auto'