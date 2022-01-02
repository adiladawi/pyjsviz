from typing import Optional, Literal,List, Any, Union
from pydantic import BaseModel
from tooltip import ToolTip
from handlestyle import HandleStyle

class Emphasis(BaseModel):
    iconStyle: Any = HandleStyle().dict()
	
	
class SaveAsImage(BaseModel):
	type: Literal['png'] =  'png'
	name: Optional[str]
	backgroundColor: str = 'auto' 
	connectedBackgroundColor: str = '#fff'
	excludeComponents: List[str] = ['toolbox']
	show: bool = True
	title: Literal['save as image'] = 'save as image'
	icon : Optional[Any]
	iconStyle: Any = HandleStyle().dict()
	emphasis: Any = Emphasis().dict()
	pixelRatio: int = 1


class Restore(BaseModel):
	show: bool = True
	title: Literal['restore'] = 'restore'
	icon :Optional[Any]
	iconStyle: Any = HandleStyle().dict()
	emphasis: Any = Emphasis().dict()

class DataView(BaseModel):
	show: bool = True
	title: Literal['data view'] = 'data view'
	icon :Optional[Any]
	iconStyle: Any = HandleStyle().dict()
	emphasis: Any = Emphasis().dict()
	readOnly: bool = False
	optionToContent :Optional[Any]
	contentToOption :Optional[Any]
	lang: List[str] = ['data view', 'turn off', 'refresh']
	backgroundColor: str = '#fff'
	textareaColor: str = '#fff'
	textareaBorderColor: str = '#333'
	textColor: str = '#000'
	buttonColor: str = '#c23531'
	buttonTextColor: str = '#fff'

class TitleMagic(BaseModel):
	line: Literal['for line charts'] =  'for line charts'
	bar: Literal['for bar charts']  = 'for bar charts'
	stack: Literal['for stacked charts'] = 'for stacked charts'
	tiled: Literal['for tiled charts'] = 'for tiled charts'


class IconMagic(BaseModel):
	line :Optional[str]
	bar :Optional[str]
	stack :Optional[str]
	tiled :Optional[str]
	

class Option(BaseModel):
	line :Optional[Any]
	bar :Optional[Any]
	stack :Optional[Any]
	tiled :Optional[Any]
	
class SeriesIndex(BaseModel):
	line :Optional[Any]
	bar :Optional[Any]
	stack :Optional[Any]
	tiled :Optional[Any]
 
 
class BrushStyle(BaseModel):
    color: Optional[str]
    borderColor: str = '#000'
    borderWidth: int = 0
    borderType: Literal['solid','dashed', 'dotted'] = 'solid'
    borderDashOffset: int = 0
    borderCap: Literal['butt','round','square'] = 'butt'
    borderJoin: Literal['bevel','round','miter'] = 'bevel'
    borderMiterLimit: int = 10
    shadowBlur: Optional[int]
    shadowColor: Optional[str]
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
 
 
class DataZoom(BaseModel):
	show: bool = True
	title: Literal['data view'] = 'data view'
	icon :Optional[Any]
	iconStyle: Any = HandleStyle().dict()
	emphasis: Any = Emphasis().dict()
	filterMode: Literal['filter', 'weakFilter', 'empty', 'none'] = 'filter'
	xAxisIndex: Optional[Any]
	yAxisIndex: Optional[Any]
	brushStyle: Any = BrushStyle().dict()


class MagicType(BaseModel):
	show: bool = True
	type: List[str] = ['line' , 'bar' , 'stack' , 'tiled']
	title: Any = TitleMagic().dict()
	icon: Any = IconMagic().dict()
	iconStyle: Any = HandleStyle().dict()
	emphasis: Any = Emphasis().dict()
	option: Any = Option().dict()
	seriesIndex: Any = SeriesIndex().dict()
	
class IconBrush(BaseModel):
	rect :Optional[Any]
	polygon :Optional[Any]
	lineX :Optional[Any]
	lineY :Optional[Any]
	keep :Optional[Any]
	clear :Optional[Any]

	
class TitleBrush(BaseModel):
	rect: Literal['Rectangle selection'] =  'Rectangle selection'
	polygon: Literal[ 'Polygon selection']  =  'Polygon selection'
	lineX: Literal['Horizontal selection'] = 'Horizontal selection'
	lineY: Literal['Vertical selection'] = 'Vertical selection'
	keep: Literal['Keep previous selection'] = 'Keep previous selection'
	clear: Literal[ 'Clear selection'] =  'Clear selection'
	

class Brush(BaseModel):
	type: List[str] = ['rect','polygon', 'lineX','lineY', 'keep', 'clear']
	icon: Any = IconBrush().dict()
	title: Any = TitleBrush().dict()


class Feature(BaseModel):
	saveAsImage: Any = SaveAsImage().dict()
	restore: Any = Restore().dict()
	dataView: Any = DataView().dict()
	dataZoom: Any = DataZoom().dict()
	magicType: Any = MagicType().dict()
	brush: Any = Brush().dict()


class ToolBox(BaseModel):
	id :Optional[str]
	show: bool = True
	orient: Literal['horizontal','vertical'] = 'horizontal'
	itemSize: int = 15
	itemGap: int = 10
	showTitle: bool = True
	feature: Any = Feature().dict()
	iconStyle: Any = HandleStyle().dict()
	emphasis: Any = Emphasis().dict()
	zlevel: int = 0
	z: int = 2
	left: Union[int,str] = 'auto'
	top: Union[int,str] = 'auto'
	right: Union[int,str] = 'auto'
	bottom: Union[int,str] = 'auto'
	width: Union[int,str] = 'auto'
	height: Union[int,str] = 'auto'
	tooltip: Any = ToolTip().dict()