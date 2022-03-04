from typing import List, Optional, Literal, Any
from pydantic import BaseModel
from label import Label
from labelline import LabelLine
from itemstyle import ItemStyle
from linestyle import LineStyle
from areastyle import AreaStyle
from endlabel import EndLabel

class Selecte(BaseModel):
	label: Any = Label().dict()
	labelLine: Any = LabelLine().dict()
	itemStyle: Any = ItemStyle().dict()
	lineStyle: Any = LineStyle().dict()
	areaStyle: Any = AreaStyle().dict()
	endLabel: Any = EndLabel().dict()
	selectedMode: bool = False
	smooth: bool = False
	smoothMonotone: Optional[Literal['x', 'y']]
	sampling: Optional[Literal['lttb', 'average', 'max', 'min', 'sum']]
	dimensions: Optional[List[str]]
	encode: Optional[dict]
	seriesLayoutBy: Literal['column','row'] = 'column'
	datasetIndex: int = 0