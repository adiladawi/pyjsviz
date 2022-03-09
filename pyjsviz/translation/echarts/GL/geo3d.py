from typing import Any
from typing import Literal
from typing import Optional
from typing import Union

from colormaterial import ColorMaterial
from label import Label
from lambertmaterial import LambertMaterial
from light import Light
from posteffect import PostEffect
from pydantic import BaseModel
from realisticmaterial import RealisticMaterial
from temporalsupersampling import TemporalSuperSampling
from textstyle import TextStyle
from viewcontrol import ViewControl


class groundPlane(BaseModel):
    show: bool = False
    color: str = "#aaa"


class ItemStyle(BaseModel):
    color: Any = "adaptive"
    opacity: int = 1
    borderWidth: int = 0
    borderColor: str = "#333"


class Emphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class Regions(BaseModel):
    name: Optional[str]
    regionHeight: Optional[int]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Emphasis().dict()


class Geo3D(BaseModel):
    show: bool = True
    map: Optional[str]
    boxWidth: int = 100
    boxHeight: int = 10
    boxDepth: Union[int, str] = "auto"
    regionHeight: int = 3
    environment: str = "auto"
    groundPlane: groundPlane
    instancing: bool = False
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = Emphasis().dict()
    regions: Any = [Regions().dict()]
    shading: Optional[Literal["color", "lambert", "realistic"]]
    realisticMaterial: Any = RealisticMaterial().dict()
    lambertMaterial: Any = LambertMaterial().dict()
    colorMaterial: Any = ColorMaterial().dict()
    light: Any = Light().dict()
    postEffect: Any = PostEffect().dict()
    temporalSuperSampling: Any = TemporalSuperSampling().dict()
    viewControl: Any = ViewControl().dict()
    zlevel: int = -10
    left: Union[int, str] = "auto"
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
