from typing import Optional, List, Union, Literal
from pydantic import BaseModel

class Label(BaseModel):
	show: bool = False
	precision: str = 'auto'
	formatter :Optional[str]
	margin: int = 3
	color: str = '#fff'
	fontStyle: Literal['normal','italic','oblique'] = 'normal'
	fontWeight: Literal['normal','bolder','bold','lighter'] = 'normal'
	fontFamily: Literal['sans-serif','serif','monospace','Arial','Coriour New'] = 'sans-serif'
	fontSize: int = 12
	lineHeight: Optional[int]
	width: Optional[int]
	height: Optional[int]
	textBorderColor: Optional[str]
	textBorderWidth: Optional[int]
	textShadowColor: str = 'transparent'
	textShadowBlur: int = 0
	textShadowOffsetX: int = 0
	textShadowOffsetY: int = 0
	overflow: Literal['none','truncate', 'break','breakAll'] = 'none'
	ellipsis: str = '...' 
	lineOverflow: Literal['none','truncate'] = 'none'
	padding: Union[int, List[int]] = [5, 7, 5, 7]
	backgroundColor: str = 'auto'
	borderColor: Optional[str]
	borderWidth: int = 0
	shadowBlur: int = 3
	shadowColor: str = '#aaa'
	shadowOffsetX: int = 0
	shadowOffsetY: int = 0