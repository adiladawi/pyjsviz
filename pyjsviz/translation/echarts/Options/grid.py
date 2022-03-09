from typing import Any
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel
from tooltip import ToolTip


class Grid(BaseModel):
    id: Optional[str]
    show: bool = False
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "10%"
    top: Union[int, str] = 60
    right: Union[int, str] = "10%"
    bottom: Union[int, str] = 60
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    containLabel: bool = False
    backgroundColor: str = "transparent"
    borderColor: str = "#ccc"
    borderWidth: int = 1
    shadowBlur: Optional[int]
    shadowColor: Optional[str]
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    tooltip: Any = ToolTip().dict()
