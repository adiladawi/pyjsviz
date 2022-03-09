from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class Bloom(BaseModel):
    enable: bool = False
    bloomIntensity: float = 0.1


class DepthOfField(BaseModel):
    enable: bool = False
    focalDistance: int = 50
    focalRange: int = 20
    fstop: float = 2.8
    blurRadius: int = 10


class SSAO(BaseModel):
    enable: bool = False
    quality: Literal["low", "medium", "high", "ultra"] = "medium"
    radius: int = 2
    intensity: int = 1


class ColorCorrection(BaseModel):
    enable: bool = True
    lookupTexture: Optional[Any]
    exposure: int = 0
    brightness: int = 0
    contrast: int = 1
    saturation: int = 1


class FXAA(BaseModel):
    enable: bool = False


class PostEffect(BaseModel):
    enable: bool = False
    bloom: Any = Bloom().dict()
    depthOfField: Any = DepthOfField().dict()
    screenSpaceAmbientOcclusion: Optional[Any]
    SSAO: Any = SSAO().dict()
    colorCorrection: Any = ColorCorrection().dict()
    FXAA: Any = FXAA().dict()
