from typing import Any, Optional, Union
from pydantic import BaseModel


class ItemStyle(BaseModel):
    color: Any = 'adaptive'
    opacity: float = 0.8
    borderWidth: int = 0
    borderColor: str = '#fff'