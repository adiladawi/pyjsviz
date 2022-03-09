from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class BrushStyle(BaseModel):
    borderWidth: int = 1
    color: str = "rgba(120,140,180,0.3)"
    borderColor: str = "rgba(120,140,180,0.8)"


class Brush(BaseModel):
    id: Optional[str]
    toolbox: List[str] = ["rect", "polygon", "keep", "clear"]
    brushLink: Optional[Union[List[int], Literal["all", "none", "null", "undefined"]]]
    seriesIndex: Union[Literal["all", "Array", "number"], List[int], int] = "all"
    geoIndex: Optional[Any]
    xAxisIndex: Optional[Any]
    yAxisIndex: Optional[Any]
    brushType: Literal["rect", "polygon", "lineX", "lineY"] = "rect"
    brushMode: Literal["single", "multiple"] = "single"
    transformable: bool = True
    brushStyle: dict = BrushStyle().dict()
    throttleType: Literal["fixRate", "debounce"] = "fixRate"
    throttleDelay: int = 0
    removeOnClick: bool = True
    inBrush: Optional[Any]
    outOfBrush: Optional[Any]
    z: int = 10000
