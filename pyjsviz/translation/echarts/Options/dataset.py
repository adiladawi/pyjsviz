from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Sequence
from typing import Union

from pydantic import BaseModel


class Filter(BaseModel):
    type: Literal["filter"] = "filter"
    config: Optional[dict]
    print: bool = False


class Sort(BaseModel):
    type: Literal["sort"] = "sort"
    config: Optional[dict]
    print: bool = False


class Dataset(BaseModel):
    id: Optional[str]
    source: Optional[Union[List[Any], dict]]
    dimensions: Optional[List[str]]
    sourceHeader: Optional[Literal["null", "undefine", True, False]]
    transform: Any = [Filter().dict(), Sort().dict()]
    fromDatasetIndex: Optional[int]
    fromDatasetId: Optional[str]
    fromTransformResult: Optional[int]
