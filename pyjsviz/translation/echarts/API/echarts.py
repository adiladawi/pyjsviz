from typing import Any
from typing import Optional

from pydantic import BaseModel


class Graphic(BaseModel):
    extendShape: Optional[Any]
    registerShape: Optional[Any]
    getShapeClass: Optional[Any]
    clipPointsByRect: Optional[Any]
    clipRectByRect: Optional[Any]


class ECHARTS(BaseModel):
    init: Optional[Any]
    connect: Optional[Any]
    disconnect: Optional[Any]
    dispose: Optional[Any]
    getInstanceByDom: Optional[Any]
    use: Optional[Any]
    registerMap: Optional[Any]
    getMap: Optional[Any]
    registerTheme: Optional[Any]
    registerLocale: Optional[Any]
    graphic: Any = Graphic().dict()
