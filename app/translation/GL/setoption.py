from pydantic import BaseModel
from typing import Optional, Any
from globe import Globe
from geo3d import Geo3D
from mapbox3d import MapBox3D
from grid3d import Grid3D
from xaxis3d import XAxis3D
from yaxis3d import YAxis3D
from zaxis3d import ZAxis3D
from series import Series

class SetOption(BaseModel):
    globe: Any = Globe().dict()
    geo3D: Any = Geo3D().dict()
    mapbox3D: Any = MapBox3D().dict()
    grid3D: Any = Grid3D().dict()
    xAxis3D: Any = XAxis3D().dict()
    yAxis3D: Any = YAxis3D().dict()
    zAxis3D: Any = ZAxis3D().dict()
    series: Any = [i for i in Series().dict().values()]