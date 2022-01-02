from typing import List, Optional, List, Union, Literal, Any
from pydantic import BaseModel
from textstyle import TextStyle
from itemstyle import ItemStyle
from linestyle import LineStyle
from selectorlabel import SelectorLabel


class Emphasis(BaseModel):
    selectorLabel:  Any = SelectorLabel().dict()

class Data(BaseModel):
    name: Optional[str]
    icon: Optional[str]
    itemstyle: Any = ItemStyle().dict()
    linestyle: Any = LineStyle().dict()
    textStyle: Optional[Any] # TextStyle().dict()
 

class PageIcons(BaseModel):
    horizontal : List[str]  = ['M0,0L12,-10L12,10z', 'M0,0L-12,-10L-12,10z']
    vertical : List[str]  = ['M0,0L12,-10L12,10z', 'M0,0L-12,-10L-12,10z']


class Legend(BaseModel):
    id : Optional[str]
    type :Literal['plain','scroll'] ='plain'
    show: bool = True
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = 'auto'
    top: Union[int, str] = 'auto'
    right: Union[int, str] = 'auto'
    bottom: Union[int, str] = 'auto'
    width: Union[int, str] = 'auto'
    height: Union[int, str] = 'auto'
    orient: Literal['horizontal','vertical'] = 'horizontal'
    align: Literal['auto','left','right'] = 'auto'
    padding: Union[int, List[int]] = 5
    itemGap: int = 10
    itemWidth: int = 25
    itemHeight: int = 14
    itemstyle: Any = ItemStyle().dict()
    lineStyle: Any = ItemStyle().dict()
    formatter: Optional[Any]
    selectedMode: Literal[True, False, 'single' ,'multiple'] = True
    inactiveColor: str = '#ccc'
    inactiveBorderColor: str = '#ccc'
    inactiveBorderWidth: str = 'auto'
    selected: Optional[Any]
    textStyle: Any = TextStyle().dict()
    tooltip :Optional[Any] # ToolTip().dict()
    icon : Optional[str]
    data: Any = [Data().dict()]
    backgroundColor: str = 'transparent'
    borderColor: str = '#ccc'
    borderWidth: int =  1
    borderRadius:int = 0
    shadowBlur: Optional[int]
    shadowColor: Optional[str]
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    scrollDataIndex: int = 0
    pageButtonItemGap: int = 5
    pageButtonGap: Optional[int]
    pageButtonPosition: Literal['end','start'] = 'end'
    pageFormatter: str = '{current}/{total}'
    pageIcons: Any = PageIcons().dict()
    pageIconColor: str = '#2f4554'
    pageIconInactiveColor: str = '#aaa' 
    pageIconSize: int = 15
    pageTextStyle: Any = TextStyle().dict()
    animation : Optional[bool]
    animationDurationUpdate: int = 800
    emphasis: Any = Emphasis().dict()
    selector: bool = False
    selectorLabel: Any = SelectorLabel().dict()
    selectorPosition: Literal['auto','end','start'] = 'auto'
    selectorItemGap: int = 7
    selectorButtonGap: int = 10