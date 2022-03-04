from typing import Optional, Literal,List, Any
from pydantic import BaseModel
from label import Label
from linestyle import LineStyle
from shadowstyle import ShadowStyle
from handle import Handle
from crossstyle import CrossStyle

class AxisPointer(BaseModel):
    id : Optional[bool]
    show: bool = False
    type: Literal['line','shadow','none'] = 'line'
    axis: str = 'auto'
    snap: Optional[bool]
    z: Optional[int]
    label: dict = Label().dict()
    lineStyle: dict = LineStyle().dict()
    shadowStyle: dict = ShadowStyle().dict()
    triggerTooltip: bool = True
    value: Optional[int]
    status: Optional[Literal['show','hide']]
    handle: Any = Handle().dict()
    link: Optional[Any]
    triggerOn: Literal['mousemove|click','mousemove', 'click', 'none'] = 'mousemove|click'