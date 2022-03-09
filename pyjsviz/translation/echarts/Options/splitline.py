from typing import Any
from typing import Literal
from typing import Optional
from typing import Union

from linestyle import LineStyle
from pydantic import BaseModel


class SplitLine(BaseModel):
    show: bool = True
    interval: Optional[Union[Literal["auto"], int]] = "auto"
    lineStyle: Any = LineStyle().dict()
