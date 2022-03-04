from typing import List, Literal,Any, Optional, Union
from pydantic import BaseModel

class MouseEvents(BaseModel):
    click: Optional[Any]
    dblclick: Optional[Any]
    mousedown: Optional[Any]
    mousemove: Optional[Any]
    mouseup: Optional[Any]
    mouseover: Optional[Any]
    mouseout: Optional[Any]
    globalout: Optional[Any]
    contextmenu: Optional[Any]


class Events(BaseModel): 
    Mouseevents: Any = MouseEvents().dict()
    highlight: Optional[Any]
    downplay: Optional[Any]
    selectchanged: Optional[Any]
    legendselectchanged: Optional[Any]
    legendselected: Optional[Any]
    legendunselected: Optional[Any]
    legendselectall: Optional[Any]
    legendinverseselect: Optional[Any]
    legendscroll: Optional[Any]
    datazoom: Optional[Any]
    datarangeselected: Optional[Any]
    timelinechanged: Optional[Any]
    timelineplaychanged: Optional[Any]
    restore: Optional[Any]
    dataviewchanged: Optional[Any]
    magictypechanged: Optional[Any]
    geoselectchanged: Optional[Any]
    geoselected: Optional[Any]
    geounselected: Optional[Any]
    axisareaselected: Optional[Any]
    brush: Optional[Any]
    brushEnd: Optional[Any]
    brushselected: Optional[Any]
    globalcursortaken: Optional[Any]
    rendered: Optional[Any]
    finished: Optional[Any]
    
    def dict(self):
        return {
            'Mouse events': self.Mouseevents,
            'highlight': self.highlight,
            'downplay': self.downplay,
            'selectchanged': self.selectchanged,
            'legendselectchanged': self.legendselectchanged,
            'legendselected': self.legendselected,
            'legendunselected': self.legendunselected,
            'legendselectall': self.legendselectall,
            'legendinverseselect': self.legendinverseselect,
            'legendscroll': self.legendscroll,
            'datazoom': self.datazoom,
            'datarangeselected': self.datarangeselected,
            'timelinechanged': self.timelinechanged,
            'timelineplaychanged': self.timelineplaychanged,
            'restore': self.restore,
            'dataviewchanged': self.dataviewchanged,
            'magictypechanged': self.magictypechanged,
            'geoselectchanged': self.geoselectchanged,
            'geoselected': self.geoselected,
            'geounselected': self.geounselected,
            'axisareaselected': self.axisareaselected,
            'brush': self.brush,
            'brushEnd': self.brushEnd,
            'brushselected': self.brushselected,
            'globalcursortaken': self.globalcursortaken,
            'rendered': self.rendered,
            'finished': self.finished,
        }