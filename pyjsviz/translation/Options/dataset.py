from typing import Optional, List, Sequence, Union, Literal, Any
from pydantic import BaseModel


class Filter(BaseModel):
	type: Literal['filter'] = 'filter'
	config: Optional[dict]
	print: bool = False
 


class Sort(BaseModel):
	type: Literal['sort'] = 'sort'
	config: Optional[dict]
	print: bool = False



class Dataset(BaseModel):
	id: Optional[str]
	source: Optional[Union[List[Any],dict]]
	dimensions: Optional[List[str]]
	sourceHeader: Optional[Literal['null', 'undefine',True, False]]
	transform: Any = [Filter().dict(),Sort().dict()]
	fromDatasetIndex: Optional[int]
	fromDatasetId: Optional[str]
	fromTransformResult: Optional[int]