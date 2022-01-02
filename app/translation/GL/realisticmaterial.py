from typing import  Any, Optional
from pydantic import BaseModel

class RealisticMaterial(BaseModel):
    detailTexture: Optional[Any] 
    textureTiling: int = 1
    textureOffset: int = 0
    roughness: Optional[Any] = 0.5
    metalness: Optional[Any]  = 0
    roughnessAdjust: float = 0.5
    metalnessAdjust: float = 0.5
    normalTexture: Optional[Any]