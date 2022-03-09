from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class EndLabel(BaseModel):
    show: bool = False
    distance: int = 5
    rotate: Optional[int]
    offset: Optional[List[int]]
    formatter: Optional[str]
    color: str = "#fff"
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
    padding: Union[int, List[int]] = 0
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
    valueAnimation: Optional[bool]
