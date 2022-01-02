from typing import Any
from pydantic import BaseModel
from areastyle import AreaStyle


class SplitArea(BaseModel):
    show: bool = False
    interval: Any = 'auto'
    areaStyle: Any = AreaStyle().dict()