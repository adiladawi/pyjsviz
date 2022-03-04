from pydantic import BaseModel
from typing import Any
from label import Label
from labelline import LabelLine
from itemstyle import ItemStyle
from linestyle import LineStyle
from areastyle import AreaStyle
from endlabel import EndLabel

class Blur(BaseModel):
	label: Any = Label().dict()
	labelLine: Any = LabelLine().dict()
	itemStyle: Any = ItemStyle().dict()
	lineStyle: Any = LineStyle().dict()
	areaStyle: Any = AreaStyle().dict()
	endLabel: Any = EndLabel().dict()