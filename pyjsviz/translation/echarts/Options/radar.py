from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from axislabel import AxisLabel
from axisline import AxisLine
from axistick import AxisTick
from indicator import Indicator
from name import Name
from pydantic import BaseModel
from splitarea import SplitArea
from splitline import SplitLine


class Radar(BaseModel):
    id: Optional[str]
    zlevel: int = 0
    z: int = 2
    center: List[Union[int, str]] = ["50%", "50%"]
    radius: Optional[Union[int, str, List[int], List[str]]] = "75%"
    startAngle: int = 90
    name: dict = Name().dict()
    nameGap: int = 15
    splitNumber: int = 5
    shape: Literal["polygon", "circle"] = "polygon"
    scale: bool = False
    silent: bool = False
    triggerEvent: bool = False
    axisLine: Any = AxisLine().dict()
    axisTick: Any = AxisTick().dict()
    axisLabel: Any = AxisLabel().dict()
    splitLine: Any = SplitLine().dict()
    splitArea: Any = SplitArea().dict()
    indicator: Any = Indicator().dict()
