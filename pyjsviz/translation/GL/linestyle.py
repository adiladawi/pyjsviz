from pydantic import BaseModel


class LineStyle(BaseModel):
    color: str = '#333'
    opacity: int = 1
    width: int = 2