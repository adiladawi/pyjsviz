from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from action import Action
from echarts import ECHARTS
from echartsInstance import EchartsInstance
from events import Events
from pydantic import BaseModel


class API(BaseModel):
    echarts: Any = ECHARTS().dict()
    echartsInstance: Any = EchartsInstance().dict()
    action: Any = Action().dict()
    events: Any = Events().dict()
