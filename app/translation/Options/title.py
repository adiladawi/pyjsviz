from typing import List, Optional, Union, Literal, Any
from pydantic import BaseModel
from textstyle import TextStyle


class Title(BaseModel):
    id : Optional[str]
    show: bool = True
    text: str = '' 
    link: Optional[str]
    target: Literal['blank','self'] = 'blank'
    textStyle: Any = TextStyle().dict()
    subtext: Optional[str]
    sublink: Optional[str]
    subtarget: Literal['blank','self'] = 'blank'
    subtextStyle: Any = TextStyle().dict()
    rich: Optional[dict]
    textAlign:  Literal['auto', 'left', 'right', 'center'] = 'auto' 
    textVerticalAlign:  Literal['auto', 'top', 'bottom', 'middle'] = 'auto'
    triggerEvent: bool = False
    padding: Union[int, List[int]] = 5
    itemGap: int = 10
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = 'auto'
    top: Union[int, str] = 'auto'
    right: Union[int, str] = 'auto'
    bottom: Union[int, str] = 'auto'
    backgroundColor: str = 'transparent'
    borderColor: str = '#ccc'
    borderWidth: int = 1
    borderRadius: Union[int, List[int]] = 0
    shadowBlur: Optional[int]
    shadowColor: Optional[str]
    shadowOffsetX: Optional[int]
    shadowOffsetY: Optional[int]