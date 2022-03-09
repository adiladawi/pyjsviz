from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class Legend(BaseModel):
    legendSelect: Optional[Any]
    legendUnSelect: Optional[Any]
    legendToggleSelect: Optional[Any]
    legendAllSelect: Optional[Any]
    legendInverseSelect: Optional[Any]
    legendScroll: Optional[Any]


class ToolTip(BaseModel):
    showTip: Optional[Any]
    hideTip: Optional[Any]


class DataZoom(BaseModel):
    dataZoom: Optional[Any]
    takeGlobalCursor: Optional[Any]


class VisualMap(BaseModel):
    selectDataRange: Optional[Any]


class TimeLine(BaseModel):
    timelineChange: Optional[Any]
    timelinePlayChange: Optional[Any]


class ToolBox(BaseModel):
    restore: Optional[Any]


class Geo(BaseModel):
    geoSelect: Optional[Any]
    geoUnSelect: Optional[Any]
    geoToggleSelect: Optional[Any]


class Brush(BaseModel):
    brush: Optional[Any]
    brushEnd: Optional[Any]
    takeGlobalCursor: Optional[Any]


class Action(BaseModel):
    highlight: Optional[Any]
    downplay: Optional[Any]
    select: Optional[Any]
    unselect: Optional[Any]
    toggleSelected: Optional[Any]
    legend: Any = Legend().dict()
    tooltip: Any = ToolTip().dict()
    dataZoom: Any = DataZoom().dict()
    visualMap: Any = VisualMap().dict()
    timeline: Any = TimeLine().dict()
    toolbox: Any = ToolBox().dict()
    geo: Any = Geo().dict()
    brush: Any = Brush().dict()
