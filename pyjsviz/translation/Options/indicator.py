from typing import Optional
from pydantic import BaseModel

class Indicator(BaseModel):
	name :Optional[str]
	max :Optional[int]
	min :Optional[int]
	color :Optional[str]
