from typing import Any
from typing import List
from typing import Literal

from itemstyle import ItemStyle
from pydantic import BaseModel


class Anchor(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): base model from pydantic
    """

    show: bool = True
    showAbove: bool = False
    size: int = 6
    icon: Literal[
        "default",
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "default"
    offsetCenter: List[int] = [0, 0]
    keepAspect: bool = False
    itemStyle: Any = ItemStyle().dict()
