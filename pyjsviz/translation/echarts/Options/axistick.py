from typing import Literal
from typing import Union

from pydantic import BaseModel


class AxisTick(BaseModel):
    show: bool = True
    alignWithLabel: bool = False
    interval: Union[Literal["auto"], int] = "auto"
    inside: bool = False
    length: int = 5
