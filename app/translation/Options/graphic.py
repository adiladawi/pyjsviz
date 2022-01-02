from typing import Optional, Literal, Any, List, Union, Any
from pydantic import BaseModel


class LayoutRect(BaseModel):
	x: Optional[int]
	y: Optional[int]
	width: Optional[int]
	height: Optional[int]


class TextConfig(BaseModel):
	position: Literal['left','right','top','bottom','inside','insideLeft','insideRight','insideTop','insideBottom','insideTopLeft','insideTopRight' ,'insideBottomLeft','insideBottomRight'] = 'inside'
	rotation: Optional[int]
	layoutRect: Optional[LayoutRect]
	offset: Optional[List[int]]
	origin: Optional[Any]
	distance: int = 5
	local: bool = False
	insideFill: Optional[str]
	insideStroke: Optional[str]
	outsideFill: Optional[str]
	outsideStroke: Optional[str]
	inside: Optional[bool]

class Text(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'text'
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge' #$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]


class Group(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'group'
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]

	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}

class Image(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'image'
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]

	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}


class Rect(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'rect'
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]

	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}

class Circle(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'circle' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]

	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}

class Ring(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'ring' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]
 
	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}

class Arc(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'arc' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]
 
	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}


class Polygon(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'polygon' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]
 
	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}


class Polyline(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'polyline' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]
 
	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}


class Line(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'line' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]

	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}


class BezierCurve(BaseModel):
	type: Literal['group', 'image', 'text', 'circle', 'sector', 'ring', 'polygon', 'polyline', 'rect', 'line', 'bezierCurve', 'arc'] = 'bezierCurve' 
	id: Optional[str]
	action:  Literal['merge', 'replace', 'remove'] = 'merge'#$action
	x: int = 0
	y: int = 0
	rotation: int = 0
	scaleX: int = 1
	scaleY: int = 1
	originX: int = 0
	originY: int = 0
	left: Union[int,str] = 'undefined'
	right: Union[int,str] = 'undefined'
	top: Union[int,str] = 'undefined'
	bottom: Union[int,str] = 'undefined'
	bounding: Literal['all', 'raw'] = 'all'
	z: int = 0
	zlevel: int = 0
	info: Optional[Any]
	silent: bool = False
	invisible: bool = False
	ignore: bool = False
	textContent: Optional[dict] #Text().dict()
	textConfig: Any = TextConfig().dict()
	cursor: str = 'pointer'
	draggable: bool = False
	progressive: bool = False
	width: int = 0
	height: int = 0
	diffChildrenByName: bool = False
	children: Optional[Any]
	onclick: Optional[Any]
	onmouseover: Optional[Any]
	onmouseout: Optional[Any]
	onmousemove: Optional[Any]
	onmousewheel: Optional[Any]
	onmousedown: Optional[Any]
	onmouseup: Optional[Any]
	ondrag: Optional[Any]
	ondragstart: Optional[Any]
	ondragend: Optional[Any]
	ondragenter: Optional[Any]
	ondragleave: Optional[Any]
	ondragover: Optional[Any]
	ondrop: Optional[Any]

	def dict(self):
		return {
		'type': self.type,
		'id' :  self.id,
		'$action' : self.action,
		'x': self.x,
		'y': self.y,
		'rotation': self.rotation,
		'scaleX': self.scaleX,
		'scaleY': self.scaleY,
		'originX': self.originX,
		'originY': self.originY,
		'left': self.left,
		'right': self.right,
		'top': self.top,
		'bottom': self.bottom,
		'bounding': self.bounding,
		'z': self.z,
		'zlevel': self.zlevel,
		'info': self.info,
		'silent': self.silent,
		'invisible': self.invisible,
		'ignore': self.ignore,
		'textContent': self.textContent,
		'textConfig': self.textConfig,
		'cursor': self.cursor,
		'draggable': self.draggable,
		'progressive': self.progressive,
		'width': self.width,
		'height': self.height,
		'diffChildrenByName': self.diffChildrenByName,
		'children': self.children,
		'onclick': self.onclick,
		'onmouseover': self.onmouseover,
		'onmouseout': self.onmouseout,
		'onmousemove': self.onmousemove,
		'onmousewheel': self.onmousewheel,
		'onmousedown': self.onmousedown,
		'onmouseup': self.onmouseup,
		'ondrag': self.ondrag,
		'ondragstart': self.ondragstart,
		'ondragend': self.ondragend,
		'ondragenter': self.ondragenter,
		'ondragleave': self.ondragleave,
		'ondragover': self.ondragover,
		'ondrop': self.ondrop,
		}


class Elements(BaseModel):
	group : Any = Group().dict()
	image : Any = Image().dict()
	text : Any = Text().dict()
	rect : Any = Rect().dict()
	circle : Any = Circle().dict()
	ring : Any = Ring().dict()
	arc : Any = Arc().dict()
	polygon :Any = Polygon().dict()
	polyline :Any = Polyline().dict()
	line :Any = Line().dict()
	bezierCurve :Any = BezierCurve().dict()


	

class Graphic(BaseModel):
	id :Optional[str]
	elements: Any = [i for i in Elements().dict().values()]