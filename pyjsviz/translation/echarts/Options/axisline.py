from typing import List
from typing import Optional

from linestyle import LineStyle
from pydantic import BaseModel


class AxisLine(BaseModel):
    show: bool = True
    onZero: bool = True
    onZeroAxisIndex: Optional[int]
    symbol: str = "none"
    symbolSize: List[int] = [10, 15]
    symbolOffset: List[int] = [0, 0]
    lineStyle: dict = LineStyle().dict()
