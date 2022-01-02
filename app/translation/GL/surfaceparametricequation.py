from typing import Any, Optional, Union
from pydantic import BaseModel


class U(BaseModel):
    step: Optional[int]
    min: Optional[str]
    max: Optional[str]


class V(BaseModel):
    step: Optional[str]
    min: Optional[str]
    max: Optional[str]


class SurfaceParametricEquation(BaseModel):
    u: Any = U().dict()
    v: Any = V().dict()
    x: Optional[Any]
    y: Optional[Any]
    z: Optional[Any]
