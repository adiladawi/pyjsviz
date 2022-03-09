from typing import Any
from typing import Optional
from typing import Union

from linestyle import LineStyle
from pydantic import BaseModel


class LabelLine(BaseModel):
    show: Optional[bool]
    showAbove: Optional[bool]
    length2: Optional[int]
    smooth: Union[bool, float] = False
    minTurnAngle: Optional[int]
    lineStyle: Any = LineStyle().dict()
