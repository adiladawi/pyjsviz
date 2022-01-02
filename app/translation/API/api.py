from typing import List, Literal,Any, Optional, Union
from pydantic import BaseModel
from echarts import ECHARTS
from echartsInstance import EchartsInstance
from action import Action
from events import Events

class API(BaseModel):
    echarts: Any = ECHARTS().dict()
    echartsInstance: Any = EchartsInstance().dict()
    action: Any = Action().dict()
    events: Any = Events().dict()