from typing import Optional, List, Union, Literal
from pydantic import BaseModel

class AxisLabel(BaseModel):
	show: bool = True
	interval: Union[Literal['auto'],int] = 'auto'
	inside: bool = False
	rotate: int = 0
	margin: int = 8
	formatter: Optional[str]
	showMinLabel: Optional[bool]
	showMaxLabel: Optional[bool]
	color: Optional[str]
	fontStyle: Literal['normal','italic','oblique'] = 'normal'
	fontWeight: Literal['normal','bolder','bold','lighter'] = 'normal'
	fontFamily: Literal['sans-serif','serif','monospace','Arial','Coriour New'] = 'sans-serif'
	fontSize: int = 12
	align : Literal['auto', 'left', 'right', 'center'] = 'auto'
	verticalAlign : Literal['auto', 'top', 'bottom', 'middle'] = 'auto'
	lineHeight : Optional[int]
	backgroundColor: str =  'transparent'
	borderColor:  Optional[str]
	borderWidth: int = 0
	borderRadius: int = 0
	padding: Union[int, List[int]] = 5
	shadowColor: str = 'transparent'
	shadowBlur: int = 0
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0
	width : Optional[int]
	height : Optional[int]
	textBorderColor : Optional[str]
	textBorderWidth : Optional[int]
	textShadowColor: str = 'transparent'
	textShadowBlur: int = 0
	textShadowOffsetX: int = 0
	textShadowOffsetY: int = 0
	overflow: Literal['none','truncate','break','breakAll'] = 'none'
	ellipsis: str = '...' 
	lineOverflow: Literal['none','truncate'] = 'none'
	rich: Optional[dict]