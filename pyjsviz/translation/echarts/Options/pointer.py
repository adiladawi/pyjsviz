from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class Pointer(BaseModel):
    show: bool = True
    icon: Optional[
        Literal[
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "pin",
            "arrow",
            "none",
        ]
    ]
    offsetCenter: List[int] = [0, 0]
    length: Union[int, str] = "60%"
    width: int = 6
    keepAspect: bool = False
