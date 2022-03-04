from typing import Literal,Any, Optional
from pydantic import BaseModel


class Main(BaseModel):
    color: str = '#fff'
    intensity: int = 1
    shadow: bool = False
    shadowQuality: Literal['medium' ,'low','high','ultra'] = 'medium'
    alpha: int = 0
    beta: int = 0
    time: Optional[Any]


class Ambient(BaseModel):
    color: str = '#fff'
    intensity: float = 0.2


class AmbientCubemap(BaseModel):
    texture: Optional[str]
    diffuseIntensity: float = 0.5
    specularIntensity: float = 0.5



class Light(BaseModel):
    main: Any = Main().dict()
    ambient: Any = Ambient().dict()
    ambientCubemap: Any = AmbientCubemap().dict()