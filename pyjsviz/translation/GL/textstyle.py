from typing import Literal
from pydantic import BaseModel


class TextStyle(BaseModel):
    color: str = "#fff"
    borderWidth: int = 0
    borderColor: str = '#fff'
    fontFamily: Literal['sans-serif','serif','monospace','Arial','Coriour New'] = 'sans-serif'
    fontSize: int = 12
    fontWeight:  Literal['normal','bolder','bold','lighter'] = 'normal'