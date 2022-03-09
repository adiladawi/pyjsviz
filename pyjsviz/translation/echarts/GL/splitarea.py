from typing import Any

from areastyle import AreaStyle
from pydantic import BaseModel


class SplitArea(BaseModel):
    show: bool = False
    interval: Any = "auto"
    areaStyle: Any = AreaStyle().dict()
