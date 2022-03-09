from typing import Any
from typing import Optional

from pydantic import BaseModel
from textstyle import TextStyle


class AxisLabel(BaseModel):
    show: bool = True
    margin: int = 8
    interval: Any = "auto"
    formatter: Optional[Any]
    textStyle: Any = TextStyle().dict()
