from typing import Any, Optional
from pydantic import BaseModel

class X(BaseModel):
    step: Optional[int]
    min: Optional[str]
    max: Optional[str]


class Y(BaseModel):
    step: Optional[str]
    min: Optional[str]
    max: Optional[str]


class SurfaceEquation(BaseModel):
    x: Any = X().dict()
    y: Any = Y().dict()
    z: Optional[Any]