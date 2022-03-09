from typing import Any
from typing import List
from typing import Literal
from typing import Optional

from crossstyle import CrossStyle
from handle import Handle
from label import Label
from linestyle import LineStyle
from pydantic import BaseModel
from shadowstyle import ShadowStyle


class AxisPointer(BaseModel):
    id: Optional[bool]
    show: bool = False
    type: Literal["line", "shadow", "none"] = "line"
    axis: str = "auto"
    snap: Optional[bool]
    z: Optional[int]
    label: dict = Label().dict()
    lineStyle: dict = LineStyle().dict()
    shadowStyle: dict = ShadowStyle().dict()
    triggerTooltip: bool = True
    value: Optional[int]
    status: Optional[Literal["show", "hide"]]
    handle: Any = Handle().dict()
    link: Optional[Any]
    triggerOn: Literal[
        "mousemove|click", "mousemove", "click", "none"
    ] = "mousemove|click"
