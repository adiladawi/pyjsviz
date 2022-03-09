from typing import Any
from typing import List
from typing import Literal
from typing import Optional

from areastyle import AreaStyle
from endlabel import EndLabel
from itemstyle import ItemStyle
from label import Label
from labelline import LabelLine
from linestyle import LineStyle
from pydantic import BaseModel


class Selecte(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()
    endLabel: Any = EndLabel().dict()
    selectedMode: bool = False
    smooth: bool = False
    smoothMonotone: Optional[Literal["x", "y"]]
    sampling: Optional[Literal["lttb", "average", "max", "min", "sum"]]
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
