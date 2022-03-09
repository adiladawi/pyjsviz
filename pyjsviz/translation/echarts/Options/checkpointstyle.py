from typing import Any
from typing import List
from typing import Literal
from typing import Optional

from pydantic import BaseModel


class CheckpointStyle(BaseModel):
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "circle"
    symbolSize: int = 13
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    color: str = "#316bf3"
    borderColor: str = "#fff"
    borderWidth: int = 2
    borderType: Literal["solid", "dashed", "dotted"] = "solid"
    shadowBlur: int = 2
    shadowColor: str = "rgba(0, 0, 0, 0.3)"
    shadowOffsetX: int = 1
    shadowOffsetY: int = 1
    opacity: Optional[float]
    animation: bool = True
    animationDuration: int = 300
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
    ] = "quinticInOut"
