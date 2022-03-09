from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from handlestyle import HandleStyle
from pydantic import BaseModel
from textstyle import TextStyle


class Controller(BaseModel):
    inRange: Optional[str]
    outOfRange: Optional[str]


class VisualMapContinuous(BaseModel):
    type: Literal["continuous"] = "continuous"
    id: Optional[str]
    min: Optional[int]
    max: Optional[int]
    range: Optional[List[int]]
    calculable: bool = False
    realtime: bool = True
    inverse: bool = False
    precision: int = 0
    itemWidth: int = 20
    itemHeight: int = 140
    align: Literal["auto", "left", "right", "top", "bottom"] = "auto"
    text: Optional[List[str]]
    textGap: int = 10
    show: bool = True
    dimension: Optional[str]
    seriesIndex: Optional[Union[int, List[int]]]
    hoverLink: bool = True
    inRange: Optional[str]
    outOfRange: Optional[str]
    controller: Any = Controller().dict()
    zlevel: int = 0
    z: int = 4
    left: Union[int, str] = 0
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = 0
    orient: Literal["horizontal", "vertical"] = "vertical"
    padding: Union[int, List[int]] = 5
    backgroundColor: str = "rgba(0,0,0,0)"
    borderColor: str = "#ccc"
    borderWidth: int = 0
    color: List[str] = ["#bf444c", "#d88273", "#f6efa6"]
    textStyle: Any = TextStyle().dict()
    formatter: Optional[str]
    handleIcon: Optional[str]
    handleSize: str = "120%"
    handleStyle: Any = HandleStyle().dict()
    indicatorIcon: Literal[
        "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow"
    ] = "circle"
    indicatorSize: str = "50%"
    indicatorStyle: Any = HandleStyle().dict()


class VisualMapPiecewise(BaseModel):
    type: Literal["piecewise"] = "piecewise"
    id: Optional[str]
    splitNumber: int = 5
    pieces: Optional[Any]
    categories: Optional[List[str]]
    min: Optional[int]
    max: Optional[int]
    minOpen: Optional[bool]
    maxOpen: Optional[bool]
    selectedMode: Literal["multiple", "single"] = "multiple"
    inverse: bool = False
    precision: Optional[int]
    itemWidth: int = 20
    itemHeight: int = 14
    align: Literal["auto", "left", "right"] = "auto"
    text: Optional[List[str]]
    textGap: int = 10
    showLabel: Optional[bool]
    itemGap: int = 10
    itemSymbol: Literal[
        "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
    ] = "roundRect"
    show: bool = True
    dimension: Optional[str]
    seriesIndex: Optional[Union[int, List[int]]]
    hoverLink: bool = True
    inRange: Optional[str]
    outOfRange: Optional[str]
    controller: Any = Controller().dict()
    zlevel: int = 0
    z: int = 4
    left: Union[int, str] = 0
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = 0
    orient: Literal["horizontal", "vertical"] = "vertical"
    padding: Union[int, List[int]] = 5
    backgroundColor: str = "rgba(0,0,0,0)"
    borderColor: str = "#ccc"
    borderWidth: int = 0
    color: List[str] = ["#bf444c", "#d88273", "#f6efa6"]
    textStyle: Any = TextStyle().dict()
    formatter: Optional[str]


class VisualMap(BaseModel):
    vmc: Any = VisualMapContinuous().dict()
    vmp: Any = VisualMapPiecewise().dict()
