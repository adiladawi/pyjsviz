from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from blur import Blur
from label import Label
from linestyle import LineStyle
from pydantic import BaseModel


class Emphasis(BaseModel):
    label: Any = Label().dict()
    lineStyle: Any = LineStyle().dict()


class DataStart(BaseModel):
    name: str = "starting point"
    x: Optional[int]
    y: Optional[int]
    xAxis: Optional[Union[int, str]]
    yAxis: Optional[Union[int, str]]
    value: Optional[int]
    symbol: Optional[
        Literal[
            "pin",
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "arrow",
            "none",
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: Optional[list] = [0, 0]
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Emphasis().dict()
    blur: Any = Blur().dict()


class DataEnd(BaseModel):
    name: str = "ending point"
    x: Optional[int]
    y: Optional[int]
    xAxis: Optional[Union[int, str]]
    yAxis: Optional[Union[int, str]]
    value: Optional[int]
    symbol: Optional[
        Literal[
            "pin",
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "arrow",
            "none",
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: Optional[list] = [0, 0]
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Emphasis().dict()
    blur: Any = Blur().dict()


class MarkLine(BaseModel):
    silent: bool = False
    symbol: Optional[
        Literal[
            "pin",
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "arrow",
            "none",
        ]
    ]
    symbolSize: Optional[int]
    precision: int = 2
    label: Any = Label().dict()
    lineStyle: Any = LineStyle().dict()
    emphasis: Any = Emphasis().dict()
    blur: Any = Blur().dict()
    data: Dict[int, Any] = {0: DataStart().dict(), 1: DataEnd().dict()}
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
        "quinticInOut",
        "linear",
        "quadraticIn",
        "quadraticInOut",
        "cubicIn",
        "cubicOut",
        "cubicInOut",
        "quarticIn",
        "quarticOut",
        "quarticInOut",
        "quinticIn",
        "quinticOut",
        "sinusoidalIn",
        "sinusoidalOut",
        "sinusoidalInOut",
        "exponentialIn",
        "exponentialOut",
        "exponentialInOut",
        "circularIn",
        "circularOut",
        "circularInOut",
        "elasticIn",
        "elasticOut",
        "elasticInOut",
        "backIn",
        "backOut",
        "backInOut",
        "bounceIn",
        "bounceOut",
        "bounceInOut",
    ] = "cubicOut"
    animationDelay: int = 0
    animationDurationUpdate: int = 300
    animationEasingUpdate: Literal[
        "quinticInOut",
        "linear",
        "quadraticIn",
        "quadraticInOut",
        "cubicIn",
        "cubicOut",
        "cubicInOut",
        "quarticIn",
        "quarticOut",
        "quarticInOut",
        "quinticIn",
        "quinticOut",
        "sinusoidalIn",
        "sinusoidalOut",
        "sinusoidalInOut",
        "exponentialIn",
        "exponentialOut",
        "exponentialInOut",
        "circularIn",
        "circularOut",
        "circularInOut",
        "elasticIn",
        "elasticOut",
        "elasticInOut",
        "backIn",
        "backOut",
        "backInOut",
        "bounceIn",
        "bounceOut",
        "bounceInOut",
    ] = "cubicOut"
    animationDelayUpdate: int = 0
