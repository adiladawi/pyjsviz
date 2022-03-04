from typing import List, Literal,Any, Optional, Union
from pydantic import BaseModel

class ViewControl(BaseModel):
    projection: Literal['perspective' ,'orthogonal'] = 'perspective'
    autoRotate: bool = False
    autoRotateDirection: Literal['cw' ,'ccw'] = 'cw'
    autoRotateSpeed: int = 10
    autoRotateAfterStill: int = 3
    damping: float = 0.8
    rotateSensitivity: Union[int,List[int]] = 1
    zoomSensitivity: int = 1
    panSensitivity: int = 0
    panMouseButton: Literal['left' ,'middle', 'right'] = 'left'
    rotateMouseButton: Literal['left' ,'middle', 'right'] = 'middle'
    distance: int = 150
    minDistance: int = 40
    maxDistance: int = 400
    orthographicSize: int = 150
    maxOrthographicSize: int = 20
    minOrthographicSize: int = 400
    alpha: int = 0
    beta: int = 0
    center: Optional[List[int]]
    minAlpha: int = -90
    maxAlpha: int = 90
    minBeta: Optional[Any]
    maxBeta: Optional[Any]
    animation: bool = True
    animationDurationUpdate: int = 1000
    animationEasingUpdate: Literal['quinticInOut','linear','quadraticIn','quadraticInOut','cubicIn','cubicOut','cubicInOut','quarticIn','quarticOut', 'quarticInOut', 'quinticIn', 'quinticOut', 'sinusoidalIn', 'sinusoidalOut', 'sinusoidalInOut' , 'exponentialIn', 'exponentialOut', 'exponentialInOut', 'circularIn', 'circularOut', 'circularInOut', 'elasticIn', 'elasticOut', 'elasticInOut','backIn','backOut', 'backInOut','bounceIn','bounceOut','bounceInOut'] = 'cubicInOut'
    targetCoord: Optional[List[float]]