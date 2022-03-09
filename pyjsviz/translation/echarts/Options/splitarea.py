from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from areastyle import AreaStyle
from pydantic import BaseModel


class SplitArea(BaseModel):
    interval: Optional[Union[Literal["auto"], int]] = "auto"
    show: bool = False
    areaStyle: Any = AreaStyle().dict()
