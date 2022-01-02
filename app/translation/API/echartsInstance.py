from typing import List, Literal,Any, Optional, Union
from pydantic import BaseModel

class EchartsInstance(BaseModel):
    group: Optional[Union[int,str]]
    setOption: Optional[Any] # Options.setOption.SetOption().dict()
    getWidth: Optional[Any]
    getHeight: Optional[Any]
    getDom: Optional[Any]
    getOption: Optional[Any]
    resize: Optional[Any]
    dispatchAction: Optional[Any]
    on: Optional[Any]
    off: Optional[Any]
    convertToPixel: Optional[Any]
    convertFromPixel: Optional[Any]
    containPixel: Optional[Any]
    showLoading: Optional[Any]
    hideLoading: Optional[Any]
    getConnectedDataURL: Optional[Any]
    appendData: Optional[Any]
    clear: Optional[Any]
    isDisposed: Optional[Any]
    dispose: Optional[Any]