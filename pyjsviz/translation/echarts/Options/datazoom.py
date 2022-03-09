from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from areastyle import AreaStyle
from handlestyle import HandleStyle
from linestyle import LineStyle
from pydantic import BaseModel
from textstyle import TextStyle


class DataBackground(BaseModel):
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()


class Emphasis(BaseModel):
    handleStyle: Any = HandleStyle().dict()
    moveHandleStyle: Any = HandleStyle().dict()


class dataZoomInside(BaseModel):
    type: Literal["inside"] = "inside"
    id: Optional[str]
    disabled: bool = False
    xAxisIndex: Optional[Union[int, List[int]]]
    yAxisIndex: Optional[Union[int, List[int]]]
    radiusAxisIndex: Optional[Union[int, List[int]]]
    angleAxisIndex: Optional[Union[int, List[int]]]
    filterMode: Literal["filter", "weakFilter", "empty", "none"] = "filter"
    start: int = 0
    end: int = 100
    startValue: Optional[Union[int, str]]
    endValue: Optional[Union[int, str]]
    minSpan: Optional[int]
    maxSpan: Optional[int]
    minValueSpan: Optional[Union[int, str]]
    maxValueSpan: Optional[Union[int, str]]
    orient: Optional[Literal["horizontal", "vertical"]]
    zoomLock: bool = False
    throttle: int = 100
    rangeMode: Optional[List[str]]
    zoomOnMouseWheel: Literal[True, False, "shift", "ctrl", "alt"] = True
    moveOnMouseMove: Literal[True, False, "shift", "ctrl", "alt"] = True
    moveOnMouseWheel: Literal[True, False, "shift", "ctrl", "alt"] = False
    preventDefaultMouseMove: bool = True


class dataZoomSlider(BaseModel):
    type: Literal["slider"] = "slider"
    id: Optional[str]
    show: bool = True
    backgroundColor: str = "rgba(47,69,84,0)"
    dataBackground: Any = DataBackground().dict()
    selectedDataBackground: Any = DataBackground().dict()
    fillerColor: str = "rgba(47,69,84,0.25)"
    borderColor: str = "#ddd"
    handleIcon: Optional[str]
    handleSize: Union[int, str] = "100%"
    handleStyle: Any = HandleStyle().dict()
    moveHandleIcon: Optional[str]
    moveHandleSize: int = 7
    moveHandleStyle: Any = HandleStyle().dict()
    labelPrecision: Union[int, str] = "auto"
    labelFormatter: Optional[str]
    showDetail: bool = True
    showDataShadow: str = "auto"
    realtime: bool = True
    textStyle: Any = TextStyle().dict()
    xAxisIndex: Optional[Union[int, List[int]]]
    yAxisIndex: Optional[Union[int, List[int]]]
    radiusAxisIndex: Optional[Union[int, List[int]]]
    angleAxisIndex: Optional[Union[int, List[int]]]
    filterMode: Literal["filter", "weakFilter", "empty", "none"] = "filter"
    start: int = 0
    end: int = 100
    startValue: Optional[Union[int, str]]
    endValue: Optional[Union[int, str]]
    minSpan: Optional[int]
    maxSpan: Optional[int]
    minValueSpan: Optional[Union[int, str]]
    maxValueSpan: Optional[Union[int, str]]
    orient: Optional[Literal["horizontal", "vertical"]]
    zoomLock: bool = False
    throttle: int = 100
    rangeMode: Optional[List[str]]
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "auto"
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    brushSelect: bool = True
    brushStyle: Any = HandleStyle().dict()
    emphasis: Any = Emphasis().dict()


class DataZoom(BaseModel):
    dzi: Any = dataZoomInside().dict()
    dzs: Any = dataZoomSlider().dict()
