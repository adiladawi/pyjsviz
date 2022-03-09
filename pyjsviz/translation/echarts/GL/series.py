from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from colormaterial import ColorMaterial
from itemstyle import ItemStyle
from label import Label
from lambertmaterial import LambertMaterial
from light import Light
from linestyle import LineStyle
from posteffect import PostEffect
from pydantic import BaseModel
from realisticmaterial import RealisticMaterial
from surfaceequation import SurfaceEquation
from surfaceparametricequation import SurfaceParametricEquation
from temporalsupersampling import TemporalSuperSampling
from textstyle import TextStyle
from viewcontrol import ViewControl


class Scatter3DEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()


class Scatter3D(BaseModel):
    type: Literal["scatter3D"] = "scatter3D"
    name: Optional[str]
    coordinateSystem: Optional[Literal["cartesian3D", "geo3D", "globe"]]
    grid3DIndex: int = 0
    geo3DIndex: int = 0
    globeIndex: int = 0
    symbol: str = "circle"
    symbolSize: int = 10
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Scatter3DEmphasis().dict()
    data: Optional[Any]
    blendMode: Literal[
        "source-over",
        "clear",
        "copy",
        "destination-over",
        "source-in",
        "destination-in",
        "source-out",
        "destination-out",
        "source-atop",
        "destination-atop",
        "xor",
        "lighter",
    ] = "source-over"
    zlevel: int = -10
    silent: bool = False
    animation: bool = True
    animationDurationUpdate: int = 500
    animationEasingUpdate: Literal[
        "quinticInOut",
        "linear",
        "quadraticIn",
        "quadraticInOut",
        "cubicIn",
        "cubicOut",
        "cubicInOut",
        "quarticIn",
        "quarticOut",
        "quarticInOut",
        "quinticIn",
        "quinticOut",
        "sinusoidalIn",
        "sinusoidalOut",
        "sinusoidalInOut",
        "exponentialIn",
        "exponentialOut",
        "exponentialInOut",
        "circularIn",
        "circularOut",
        "circularInOut",
        "elasticIn",
        "elasticOut",
        "elasticInOut",
        "backIn",
        "backOut",
        "backInOut",
        "bounceIn",
        "bounceOut",
        "bounceInOut",
    ] = "cubicOut"


class Bar3DData(BaseModel):
    name: Optional[str]
    value: Optional[Any]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Scatter3DEmphasis().dict()


class Bar3D(BaseModel):
    type: Literal["bar3D"] = "bar3D"
    name: Optional[str]
    coordinateSystem: Literal["cartesian3D", "geo3D", "globe"] = "cartesian3D"
    grid3DIndex: int = 0
    geo3DIndex: int = 0
    globeIndex: int = 0
    bevelSize: int = 0
    bevelSmoothness: int = 2
    stack: Optional[str]
    minHeight: int = 0
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Scatter3DEmphasis().dict()
    data: Any = [Bar3DData().dict()]
    shading: Optional[Literal["color", "lambert", "realistic"]]
    realisticMaterial: Any = RealisticMaterial().dict()
    lambertMaterial: Any = LambertMaterial().dict()
    colorMaterial: Any = ColorMaterial().dict()
    zlevel: int = -10
    silent: bool = False
    animation: bool = True
    animationDurationUpdate: int = 500
    animationEasingUpdate: Literal[
        "quinticInOut",
        "linear",
        "quadraticIn",
        "quadraticInOut",
        "cubicIn",
        "cubicOut",
        "cubicInOut",
        "quarticIn",
        "quarticOut",
        "quarticInOut",
        "quinticIn",
        "quinticOut",
        "sinusoidalIn",
        "sinusoidalOut",
        "sinusoidalInOut",
        "exponentialIn",
        "exponentialOut",
        "exponentialInOut",
        "circularIn",
        "circularOut",
        "circularInOut",
        "elasticIn",
        "elasticOut",
        "elasticInOut",
        "backIn",
        "backOut",
        "backInOut",
        "bounceIn",
        "bounceOut",
        "bounceInOut",
    ] = "cubicOut"


class Line3DData(BaseModel):
    name: Optional[str]
    value: Optional[Any]
    itemStyle: Any = ItemStyle().dict()


class Line3D(BaseModel):
    type: Literal["line3D"] = "line3D"
    name: Optional[str]
    coordinateSystem: Literal["cartesian3D", "geo3D", "globe"] = "cartesian3D"
    grid3DIndex: int = 0
    lineStyle: Any = LineStyle().dict()
    data: Any = [Line3DData().dict()]
    zlevel: int = -10
    silent: bool = False
    animation: bool = True
    animationDurationUpdate: int = 500
    animationEasingUpdate: Literal[
        "quinticInOut",
        "linear",
        "quadraticIn",
        "quadraticInOut",
        "cubicIn",
        "cubicOut",
        "cubicInOut",
        "quarticIn",
        "quarticOut",
        "quarticInOut",
        "quinticIn",
        "quinticOut",
        "sinusoidalIn",
        "sinusoidalOut",
        "sinusoidalInOut",
        "exponentialIn",
        "exponentialOut",
        "exponentialInOut",
        "circularIn",
        "circularOut",
        "circularInOut",
        "elasticIn",
        "elasticOut",
        "elasticInOut",
        "backIn",
        "backOut",
        "backInOut",
        "bounceIn",
        "bounceOut",
        "bounceInOut",
    ] = "cubicOut"


class Lines3DEffect(BaseModel):
    show: bool = False
    period: int = 4
    constantSpeed: Optional[int]
    trailWidth: int = 4
    trailLength: float = 0.1
    trailColor: Optional[str]
    trailOpacity: Optional[str]


class Lines3DData(BaseModel):
    coords: Optional[Any]
    value: Optional[Any]
    lineStyle: Any = LineStyle().dict()


class Lines3D(BaseModel):
    type: Literal["lines3D"] = "lines3D"
    name: Optional[str]
    coordinateSystem: Optional[Literal["cartesian3D", "geo3D", "globe"]]
    geo3DIndex: int = 0
    globeIndex: int = 0
    polyline: bool = False
    effect: Any = Lines3DEffect().dict()
    lineStyle: Any = LineStyle().dict()
    data: Any = [Lines3DData().dict()]
    blendMode: Literal[
        "source-over",
        "clear",
        "copy",
        "destination-over",
        "source-in",
        "destination-in",
        "source-out",
        "destination-out",
        "source-atop",
        "destination-atop",
        "xor",
        "lighter",
    ] = "source-over"
    zlevel: int = -10
    silent: bool = False


class Map3DGroundPlane(BaseModel):
    show: bool = False
    color: str = "#aaa"


class Map3DData(BaseModel):
    name: Optional[str]
    value: Optional[Any]
    regionHeight: Optional[int]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = Scatter3DEmphasis().dict()


class Map3D(BaseModel):
    type: Literal["map3D"] = "map3D"
    name: Optional[str]
    map: Optional[str]
    boxWidth: int = 100
    boxHeight: int = 10
    boxDepth: Union[int, str] = "auto"
    regionHeight: int = 3
    environment: str = "auto"
    groundPlane: Any = Map3DGroundPlane().dict()
    instancing: bool = False
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = Scatter3DEmphasis().dict()
    data: Any = [Map3DData().dict()]
    shading: Optional[Literal["color", "lambert", "realistic"]]
    realisticMaterial: Any = RealisticMaterial().dict()
    lambertMaterial: Any = LambertMaterial().dict()
    colorMaterial: Any = ColorMaterial().dict()
    light: Any = Light().dict()
    postEffect: Any = PostEffect().dict()
    temporalSuperSampling: Any = TemporalSuperSampling().dict()
    viewControl: Any = ViewControl().dict()
    zlevel: int = -10
    left: Union[int, str] = "auto"
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"


class SurfaceWireframe(BaseModel):
    show: bool = True
    lineStyle: Any = LineStyle().dict()


class SurfaceData(BaseModel):
    name: Optional[str]
    value: Optional[Any]
    itemStyle: Any = ItemStyle().dict()


class Surface(BaseModel):
    type: Literal["surface"] = "surface"
    name: Optional[str]
    coordinateSystem: Literal["cartesian3D", "geo3D", "globe"] = "cartesian3D"
    grid3DIndex: int = 0
    parametric: bool = False
    wireframe: Any = SurfaceWireframe().dict()
    equation: Any = SurfaceEquation().dict()
    parametricEquation: Any = SurfaceParametricEquation().dict()
    itemStyle: Any = ItemStyle().dict()
    data: Any = [SurfaceData().dict()]
    shading: Optional[Literal["color", "lambert", "realistic"]]
    realisticMaterial: Any = RealisticMaterial().dict()
    lambertMaterial: Any = LambertMaterial().dict()
    colorMaterial: Any = ColorMaterial().dict()
    zlevel: int = -10
    silent: bool = False
    animation: bool = True
    animationDurationUpdate: int = 500
    animationEasingUpdate: Literal[
        "quinticInOut",
        "linear",
        "quadraticIn",
        "quadraticInOut",
        "cubicIn",
        "cubicOut",
        "cubicInOut",
        "quarticIn",
        "quarticOut",
        "quarticInOut",
        "quinticIn",
        "quinticOut",
        "sinusoidalIn",
        "sinusoidalOut",
        "sinusoidalInOut",
        "exponentialIn",
        "exponentialOut",
        "exponentialInOut",
        "circularIn",
        "circularOut",
        "circularInOut",
        "elasticIn",
        "elasticOut",
        "elasticInOut",
        "backIn",
        "backOut",
        "backInOut",
        "bounceIn",
        "bounceOut",
        "bounceInOut",
    ] = "cubicOut"


class Polygons3DEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()


class Polygons3DData(BaseModel):
    coords: Optional[Any]


class Polygons3D(BaseModel):
    type: Literal["polygons3D"] = "polygons3D"
    multiPolygon: bool = True
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = Polygons3DEmphasis().dict()
    data: Any = Polygons3DData().dict()
    progressiveThreshold: int = 1000


class ScatterGLData(BaseModel):
    name: Optional[str]
    value: Optional[Any]
    itemStyle: Any = ItemStyle().dict()


class ScatterGL(BaseModel):
    type: Literal["scatterGL"] = "scatterGL"
    name: Optional[str]
    coordinateSystem: Literal["cartesian2d", "polar", "geo"] = "cartesian2d"
    symbol: str = "circle"
    symbolSize: int = 10
    itemStyle: Any = ItemStyle().dict()
    data: Any = [ScatterGLData().dict()]
    blendMode: Literal[
        "source-over",
        "clear",
        "copy",
        "destination-over",
        "source-in",
        "destination-in",
        "source-out",
        "destination-out",
        "source-atop",
        "destination-atop",
        "xor",
        "lighter",
    ] = "source-over"
    zlevel: int = 10
    progressiveThreshold: int = 100000
    progressive: int = 100000


class GraphGLForceAtlas2(BaseModel):
    GPU: bool = True
    steps: int = 1
    stopThreshold: int = 1
    barnesHutOptimize: Optional[bool]
    repulsionByDegree: bool = True
    linLogMode: bool = False
    gravity: int = 1
    gravityCenter: Optional[Any]
    scaling: Optional[int]
    edgeWeightInfluence: int = 1
    edgeWeight: Union[int, List[int]] = [1, 4]
    nodeWeight: Union[int, List[int]] = [1, 4]
    preventOverlap: bool = False


class GraphGLLinks(BaseModel):
    source: Optional[Any]
    target: Optional[Any]
    value: Optional[Any]
    lineStyle: Any = LineStyle().dict()


class GraphGL(BaseModel):
    type: Literal["graphGL"] = "graphGL"
    name: Optional[str]
    layout: Literal["forceAtlas2"] = "forceAtlas2"
    forceAtlas2: Any = GraphGLForceAtlas2().dict()
    symbol: str = "circle"
    symbolSize: int = 5
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    data: Any = [ScatterGLData().dict()]
    nodes: Optional[Any]  # ScatterGLData().dict()
    links: Any = [GraphGLLinks().dict()]
    edges: Optional[Any]  # GraphGLLinks().dict()
    zlevel: int = 10


class FlowGL(BaseModel):
    type: Literal["flowGL"] = "flowGL"
    particleDensity: int = 128
    particleType: Literal["point", "line"] = "point"
    particleSize: int = 1
    particleSpeed: int = 1
    particleTrail: int = 2
    supersampling: int = 1
    gridWidth: Union[int, str] = "auto"
    gridHeight: Union[int, str] = "auto"
    data: Optional[Any]
    itemStyle: Any = ItemStyle().dict()


class Series(BaseModel):
    scatter3D: Any = Scatter3D().dict()
    bar3D: Any = Bar3D().dict()
    line3D: Any = Line3D().dict()
    lines3D: Any = Lines3D().dict()
    map3D: Any = Map3D().dict()
    surface: Any = Surface().dict()
    polygons3D: Any = Polygons3D().dict()
    scatterGL: Any = ScatterGL().dict()
    graphGL: Any = GraphGL().dict()
    flowGL: Any = FlowGL().dict()
