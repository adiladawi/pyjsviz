from typing import List, Literal,Any, Optional
from pydantic import BaseModel
from realisticmaterial import RealisticMaterial
from lambertmaterial import LambertMaterial
from colormaterial import ColorMaterial
from light import Light
from posteffect import PostEffect
from temporalsupersampling import TemporalSuperSampling


class MapBox3D(BaseModel):
    style: Optional[Any]
    center: Optional[List[float]]
    zoom: Optional[int]
    bearing: int = 0
    pitch: int = 0
    altitudeScale: int = 1
    shading: Optional[Literal['color','lambert','realistic']]
    realisticMaterial:  Any = RealisticMaterial().dict()
    lambertMaterial:  Any = LambertMaterial().dict()
    colorMaterial:  Any = ColorMaterial().dict()
    light:  Any = Light().dict()
    postEffect:  Any = PostEffect().dict()
    temporalSuperSampling:  Any = TemporalSuperSampling().dict()