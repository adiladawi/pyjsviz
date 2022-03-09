from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class LabelLayout(BaseModel):
    hideOverlap: Optional[bool]
    moveOverlap: Optional[Literal["shiftX", "shiftY"]]
    x: Optional[Union[int, str]]
    y: Optional[Union[int, str]]
    dx: Optional[int]
    dy: Optional[int]
    rotate: Optional[int]
    width: Optional[int]
    height: Optional[int]
    align: Optional[Literal["left", "right", "center"]]
    verticalAlign: Optional[Literal["top", "bottom", "middle"]]
    fontSize: Optional[int]
    draggable: Optional[bool]
    labelLinePoints: Optional[List]
