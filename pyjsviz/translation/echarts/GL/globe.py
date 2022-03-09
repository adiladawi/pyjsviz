from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from colormaterial import ColorMaterial
from lambertmaterial import LambertMaterial
from light import Light
from posteffect import PostEffect
from pydantic import BaseModel
from realisticmaterial import RealisticMaterial
from temporalsupersampling import TemporalSuperSampling
from viewcontrol import ViewControl


class Layers(BaseModel):
    show: bool = True
    type: Literal["overlay", "blend"] = "overlay"
    name: Optional[str]
    blendTo: Literal["albedo", "emission"] = "albedo"
    intensity: int = 1
    shading: Literal["color", "lambert", "realistic"] = "lambert"
    distance: Optional[int]
    texture: Optional[Any]


class Globe(BaseModel):
    show: bool = True
    zlevel: int = -10
    left: Union[int, str] = "auto"
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    globeRadius: int = 100
    globeOuterRadius: int = 150
    environment: str = "auto"
    baseTexture: Optional[Any]
    heightTexture: Optional[Any]
    displacementTexture: Optional[Any]
    displacementScale: int = 0
    displacementQuality: Literal["low", "medium", "high", "ultra"] = "medium"
    shading: Optional[Literal["color", "lambert", "realistic"]]
    realisticMaterial: Any = RealisticMaterial().dict()
    lambertMaterial: Any = LambertMaterial().dict()
    colorMaterial: Any = ColorMaterial().dict()
    light: Any = Light().dict()
    postEffect: Any = PostEffect().dict()
    temporalSuperSampling: Any = TemporalSuperSampling
    viewControl: Any = ViewControl().dict()
    layers: Any = [Layers().dict()]
