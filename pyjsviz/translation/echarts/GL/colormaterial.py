from typing import Any
from typing import Optional

from pydantic import BaseModel


class ColorMaterial(BaseModel):
    detailTexture: Optional[Any]
    textureTiling: int = 1
    textureOffset: int = 0
