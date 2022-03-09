from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from itemstyle import ItemStyle
from linestyle import LineStyle
from pydantic import BaseModel


class SplitLine(BaseModel):
    show: bool = True
    lineStyle: dict = LineStyle().dict()


class DayLabel(BaseModel):
    show: bool = True
    firstDay: int = 0
    margin: int = 0
    position: Literal["start", "end"] = "start"
    nameMap: Union[Literal["en", "cn"], List[str]] = "en"
    color: str = "#000"
    fontStyle: Literal["normal", "italic", "oblique"] = "normal"
    fontWeight: Literal["normal", "bolder", "bold", "lighter"] = "normal"
    fontFamily: Literal[
        "sans-serif", "serif", "monospace", "Arial", "Coriour New"
    ] = "sans-serif"
    fontSize: int = 12
    align: Optional[Literal["left", "center", "right"]]
    verticalAlign: Optional[Literal["top", "middle", "bottom"]]
    lineHeight: Optional[int]
    backgroundColor: str = "transparent"
    borderColor: Optional[str]
    borderWidth: int = 0
    borderType: Literal["solid", "dashed", "dotted"] = "solid"
    borderDashOffset: int = 0
    borderRadius: int = 0
    padding: int = 0
    shadowColor: str = "transparent"
    shadowBlur: int = 0
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    width: Optional[int]
    height: Optional[int]
    textBorderColor: Optional[str]
    textBorderWidth: Optional[int]
    textBorderType: Literal["solid", "dashed", "dotted"] = "solid"
    textBorderDashOffset: int = 0
    textShadowColor: str = "transparent"
    textShadowBlur: int = 0
    textShadowOffsetX: int = 0
    textShadowOffsetY: int = 0
    overflow: Literal["none", "truncate", "break", "breakAll"] = "none"
    ellipsis: str = "..."
    lineOverflow: Literal["none", "truncate"] = "none"
    rich: Optional[dict]


class MonthLabel(BaseModel):
    show: bool = True
    align: Optional[Literal["left", "center", "right"]]
    margin: int = 0
    position: Literal["start", "end"] = "start"
    formatter: Optional[str]
    color: str = "#000"
    fontStyle: Literal["normal", "italic", "oblique"] = "normal"
    fontWeight: Literal["normal", "bolder", "bold", "lighter"] = "normal"
    fontFamily: Literal[
        "sans-serif", "serif", "monospace", "Arial", "Coriour New"
    ] = "sans-serif"
    fontSize: int = 12
    verticalAlign: Optional[Literal["top", "middle", "bottom"]]
    lineHeight: Optional[int]
    backgroundColor: str = "transparent"
    borderColor: Optional[str]
    borderWidth: int = 0
    borderType: Literal["solid", "dashed", "dotted"] = "solid"
    borderDashOffset: int = 0
    borderRadius: int = 0
    padding: int = 0
    shadowColor: str = "transparent"
    shadowBlur: int = 0
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    width: Optional[int]
    height: Optional[int]
    textBorderColor: Optional[str]
    textBorderWidth: Optional[int]
    textBorderType: Literal["solid", "dashed", "dotted"] = "solid"
    textBorderDashOffset: int = 0
    textShadowColor: str = "transparent"
    textShadowBlur: int = 0
    textShadowOffsetX: int = 0
    textShadowOffsetY: int = 0
    overflow: Literal["none", "truncate", "break", "breakAll"] = "none"
    ellipsis: str = "..."
    lineOverflow: Literal["none", "truncate"] = "none"
    rich: Optional[dict]


class YearLabel(BaseModel):
    show: bool = True
    align: Optional[Literal["left", "center", "right"]]
    margin: int = 0
    position: Literal["start", "end"] = "start"
    formatter: Optional[str]
    color: str = "#000"
    fontStyle: Literal["normal", "italic", "oblique"] = "normal"
    fontWeight: Literal["normal", "bolder", "bold", "lighter"] = "normal"
    fontFamily: Literal[
        "sans-serif", "serif", "monospace", "Arial", "Coriour New"
    ] = "sans-serif"
    fontSize: int = 12
    verticalAlign: Optional[Literal["top", "middle", "bottom"]]
    lineHeight: Optional[int]
    backgroundColor: str = "transparent"
    borderColor: Optional[str]
    borderWidth: int = 0
    borderType: Literal["solid", "dashed", "dotted"] = "solid"
    borderDashOffset: int = 0
    borderRadius: int = 0
    padding: int = 0
    shadowColor: str = "transparent"
    shadowBlur: int = 0
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    width: Optional[int]
    height: Optional[int]
    textBorderColor: Optional[str]
    textBorderWidth: Optional[int]
    textBorderType: Literal["solid", "dashed", "dotted"] = "solid"
    textBorderDashOffset: int = 0
    textShadowColor: str = "transparent"
    textShadowBlur: int = 0
    textShadowOffsetX: int = 0
    textShadowOffsetY: int = 0
    overflow: Literal["none", "truncate", "break", "breakAll"] = "none"
    ellipsis: str = "..."
    lineOverflow: Literal["none", "truncate"] = "none"
    rich: Optional[dict]


class Calendar(BaseModel):
    id: Optional[str]
    zlevel: int = 0
    z: int = 2
    left: int = 80
    top: int = 60
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    range: Optional[Union[int, str, List[str]]]
    cellSize: Union[int, str, List[Any]] = 20
    orient: Literal["horizontal", "vertical"] = "horizontal"
    splitLine: Any = SplitLine().dict()
    itemStyle: Any = ItemStyle().dict()
    dayLabel: Any = DayLabel().dict()
    monthLabel: Any = MonthLabel().dict()
    yearLabel: Any = YearLabel().dict()
    silent: bool = False
