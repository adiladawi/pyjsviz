from typing import Any

from areastyle import AreaStyle
from endlabel import EndLabel
from itemstyle import ItemStyle
from label import Label
from labelline import LabelLine
from linestyle import LineStyle
from pydantic import BaseModel


class Blur(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()
    endLabel: Any = EndLabel().dict()
