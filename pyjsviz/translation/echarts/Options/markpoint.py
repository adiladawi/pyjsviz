from typing import Any
from typing import List
from typing import Literal
from typing import Optional

from blur import Blur
from itemstyle import ItemStyle
from label import Label
from pydantic import BaseModel


class Emphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class Data(BaseModel):
    name: str = ""
    type: Optional[Literal["min", "max", "average"]]
    valueIndex: Optional[int]
    valueDim: Optional[str]
    coord: Optional[List]
    x: Optional[int]
    y: Optional[int]
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
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Emphasis().dict()


class MarkPoint(BaseModel):
    symbol: Literal[
        "pin",
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "arrow",
        "none",
    ] = "pin"
    symbolSize: int = 50
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: Optional[List] = [0, 0]
    silent: bool = False
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = Emphasis().dict()
    blur: Any = Blur().dict()
    data: Any = Data().dict()
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
