from typing import Any
from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from anchor import Anchor
from areastyle import AreaStyle
from axislabel import AxisLabel
from axisline import AxisLine
from axistick import AxisTick
from blur import Blur
from endlabel import EndLabel
from itemstyle import ItemStyle
from label import Label
from labellayout import LabelLayout
from labelline import LabelLine
from linestyle import LineStyle
from markarea import MarkArea
from markline import MarkLine
from markpoint import MarkPoint
from pointer import Pointer
from progress import Progress
from pydantic import BaseModel
from selecte import Selecte
from splitline import SplitLine
from title import Title
from tooltip import ToolTip


class LineEmphasis(BaseModel):
    scale: bool = True
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()
    endLabel: Any = Label().dict()


class LineDataEmphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class LineData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "circle"
    symbolSize: int = 4
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = LineDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class BarEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class BarDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class BarData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = BarDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class PieEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class PieDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class PieData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    selected: bool = False
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = PieDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class ScatterEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class ScatterDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class ScatterData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    symbol: Optional[
        Literal[
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "pin",
            "arrow",
            "none",
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = ScatterDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class EffectScatterEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class EffectScatterDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class EffectScatterData(BaseModel):
    symbol: Optional[
        Literal[
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "pin",
            "arrow",
            "none",
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = EffectScatterDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class RippleEffect(BaseModel):
    color: Optional[str]
    period: int = 4
    scale: float = 2.5
    brushType: Literal["fill", "stroke"] = "fill"


class RadarEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class RadarDataEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    lineStyle: Any = LabelLine().dict()
    areaStyle: Any = AreaStyle().dict()


class RadarData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    symbol: Optional[
        Literal[
            "emptyCircle",
            "circle",
            "rect",
            "roundRect",
            "triangle",
            "diamond",
            "pin",
            "arrow",
            "none",
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()
    emphasis: Any = RadarDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class TreeEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class TreeDataEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LabelLine().dict()
    label: Any = Label().dict()


class TreeLeaves(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = TreeDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class TreeData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = TreeDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class LabelLine(BaseModel):
    show: Optional[bool]
    showAbove: Optional[bool]
    length2: Optional[int]
    smooth: Union[bool, float] = False
    minTurnAngle: Optional[int]
    lineStyle: Any = LineStyle().dict()


class TreeMapEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class TreeMapDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    upperLabel: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class TreeMapBreadcrumbEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()


class TreeMapBreadcrumb(BaseModel):
    show: bool = True
    left: Union[str, int] = "center"
    top: Union[str, int] = "auto"
    right: Union[str, int] = "auto"
    bottom: Union[str, int] = 0
    height: int = 22
    emptyItemWidth: int = 25
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = TreeMapBreadcrumbEmphasis().dict()


class TreeMapLevels(BaseModel):
    visualDimension: int = 0
    visualMin: Optional[int]
    visualMax: Optional[int]
    color: Optional[List[str]]
    colorAlpha: Optional[List[float]]
    colorSaturation: Optional[List[float]]
    colorMappingBy: Literal["value", "id", "index"] = "index"
    visibleMin: int = 10
    childrenVisibleMin: Optional[int]
    label: Any = Label().dict()
    upperLabel: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = TreeMapDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class TreeMapData(BaseModel):
    value: Optional[Union[int, List[int]]]
    id: Optional[str]
    name: Optional[str]
    visualDimension: int = 0
    visualMin: Optional[int]
    visualMax: Optional[int]
    color: Optional[List[str]]
    colorAlpha: Optional[List[float]]
    colorSaturation: Optional[List[float]]
    colorMappingBy: Literal["value", "id", "index"] = "index"
    visibleMin: int = 10
    childrenVisibleMin: Optional[int]
    label: Any = Label().dict()
    upperLabel: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = TreeMapDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    link: Optional[str]
    target: Literal["blank", "self"] = "blank"
    children: Optional[list]
    tooltip: Any = ToolTip().dict()


class SunBurstEmphasis(BaseModel):
    scale: bool = True
    scaleSize: int = 10
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class SunBurstLevelsEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class SunBurstData(BaseModel):
    value: Optional[Union[int, List[int]]]
    name: Optional[str]
    link: Optional[str]
    target: Literal["blank", "self"] = "blank"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class SunBurstLevels(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = SunBurstLevelsEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class BoxPlotEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    itemStyle: Any = ItemStyle().dict()


class BoxPlotDataEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()


class BoxPlotData(BaseModel):
    name: Optional[str]
    value: Optional[Union[int, List[int]]]
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = BoxPlotDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class CandleSticEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    itemStyle: Any = ItemStyle().dict()


class CandleSticDataEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()


class CandleStickData(BaseModel):
    name: Optional[str]
    value: Optional[Union[int, List[int]]]
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = CandleSticDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class HeatMapEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()


class HeatMapDataEmphasis(BaseModel):
    name: Optional[str]
    value: Optional[Union[int, List[int]]]
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class HeatMapData(BaseModel):
    name: Optional[str]
    value: Optional[Union[int, List[int]]]
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = HeatMapDataEmphasis().dict()


class MapEmphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class MapDataEmphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    labelLine: Any = LabelLine().dict()


class MapData(BaseModel):
    name: Optional[str]
    value: Optional[Union[int, List[int]]]
    selected: bool = False
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    emphasis: Any = MapDataEmphasis().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class ParallelEmphasis(BaseModel):
    lineStyle: Any = LineStyle().dict()


class ParallelData(BaseModel):
    name: Optional[str]
    value: Optional[Union[int, List[int]]]
    lineStyle: Any = LineStyle().dict()
    color: str = "#000"
    width: int = 2
    type: Literal["solid", "dashed", "dotted"] = "solid"
    dashOffset: int = 0
    cap: Literal["butt", "round", "square"] = "butt"
    join: Literal["bevel", "round", "miter"] = "bevel"
    miterLimit: int = 10
    shadowBlur: Optional[int]
    shadowColor: Optional[str]
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    opacity: float = 0.45
    emphasis: Any = ParallelEmphasis().dict()


class LinesEffect(BaseModel):
    show: bool = False
    period: int = 4
    delay: Optional[int]
    constantSpeed: int = 0
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "circle"
    symbolSize: int = 3
    color: Optional[str]
    trailLength: float = 0.2
    loop: bool = True


class LinesEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()


class LinesDataEmphasis(BaseModel):
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()


class LinesData(BaseModel):
    name: Optional[str]
    coords: Optional[List[float]]
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = LinesDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class GraphCircular(BaseModel):
    rotateLabel: bool = False


class GraphForce(BaseModel):
    initLayout: Optional[str]
    repulsion: int = 50
    gravity: float = 0.1
    edgeLength: int = 30
    layoutAnimation: bool = True
    friction: float = 0.6


class GraphEdgeLabel(BaseModel):
    show: bool = False
    position: Literal["middle", "start", "end"] = "middle"
    formatter: Optional[str]
    color: str = "#fff"
    fontStyle: Literal["normal", "italic", "oblique"] = "normal"
    fontWeight: Union[Literal["normal", "bold", "bolder", "lighter"], int] = "normal"
    fontFamily: Literal[
        "sans-serif", "serif", "monospace", "Arial", "Courier New"
    ] = "sans-serif"
    fontSize: int = 12
    align: Optional[Literal["left", "center", "right"]]
    verticalAlign: Optional[Literal["top", "middle", "bottom"]]
    lineHeight: Optional[int]
    backgroundColor: str = "transparent"
    borderColor: Optional[str]
    borderWidth: int = 0
    borderType: Literal["solid", "dashed", "dotted"] = "solid"
    borderDashOffset: int = 0
    borderRadius: int = 0
    padding: int = 0
    shadowColor: str = "transparent"
    shadowBlur: int = 0
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    width: Optional[int]
    height: Optional[int]
    textBorderColor: Optional[str]
    textBorderWidth: Optional[int]
    textBorderType: Literal["solid", "dashed", "dotted"] = "solid"
    textBorderDashOffset: int = 0
    textShadowColor: str = "transparent"
    textShadowBlur: int = 0
    textShadowOffsetX: int = 0
    textShadowOffsetY: int = 0
    overflow: Literal["none", "truncate", "break", "breakAll"] = "none"
    ellipsis: str = "..."
    lineOverflow: Literal["none", "truncate"] = "none"
    rich: Optional[dict]


class GraphEmphasis(BaseModel):
    scale: bool = True
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    edgeLabel: Any = Label().dict()


class GraphDataEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()


class GraphCategoriesEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()


class GraphCategories(BaseModel):
    name: Optional[str]
    symbol: Optional[
        Literal[
            "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = GraphCategoriesEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class GraphLinks(BaseModel):
    source: Optional[Union[str, int]]
    target: Optional[Union[str, int]]
    value: Optional[str]
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = GraphCategoriesEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    symbol: Optional[
        Literal[
            "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
        ]
    ]
    symbolSize: Optional[int]
    ignoreForceLayout: bool = False


class GraphData(BaseModel):
    name: Optional[str]
    x: Optional[int]
    y: Optional[int]
    fixed: Optional[bool]
    value: Optional[Union[int, List[int]]]
    category: Optional[int]
    symbol: Optional[
        Literal[
            "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
        ]
    ]
    symbolSize: Optional[int]
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = GraphDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class SankeyEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()


class SankeyDataEmphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()


class SankeyLevelsEmphasis(BaseModel):
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()


class SankeylinksEmphasis(BaseModel):
    lineStyle: Any = LineStyle().dict()


class SankeyLevels(BaseModel):
    depth: Optional[int]
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    emphasis: Any = SankeyLevelsEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class SankeyData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    depth: Optional[int]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    emphasis: Any = SankeyDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class SankeyLinks(BaseModel):
    source: Optional[str]
    target: Optional[str]
    value: Optional[int]
    lineStyle: Any = LineStyle().dict()
    emphasis: Any = SankeylinksEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()


class FunnelEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class FunnelDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class FunnelData(BaseModel):
    name: Optional[str]
    value: Optional[str]
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    emphasis: Any = FunnelDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class GaugeEmphasis(BaseModel):
    itemStyle: Any = ItemStyle().dict()


class GaugeDeatil(BaseModel):
    show: bool = True
    color: str = "#464646"
    fontStyle: Literal["normal", "italic", "oblique"] = "normal"
    fontWeight: Union[Literal["normal", "bold", "bolder", "lighter"], int] = "bold"
    fontFamily: Literal[
        "sans-serif", "serif", "monospace", "Arial", "Courier New"
    ] = "sans-serif"
    fontSize: int = 30
    lineHeight: int = 30
    backgroundColor: str = "transparent"
    borderColor: str = "#ccc"
    borderWidth: int = 0
    borderType: Literal["solid", "dashed", "dotted"] = "solid"
    borderDashOffset: int = 0
    borderRadius: int = 0
    padding: int = 0
    shadowColor: str = "transparent"
    shadowBlur: int = 0
    shadowOffsetX: int = 0
    shadowOffsetY: int = 0
    width: int = 100
    height: int = 40
    textBorderColor: Optional[str]
    textBorderWidth: Optional[int]
    textBorderType: Literal["solid", "dashed", "dotted"] = "solid"
    textBorderDashOffset: int = 0
    textShadowColor: str = "transparent"
    textShadowBlur: int = 0
    textShadowOffsetX: int = 0
    textShadowOffsetY: int = 0
    overflow: Literal["none", "truncate", "break", "breakAll"] = "none"
    ellipsis: str = "..."
    lineOverflow: Literal["none", "truncate"] = "none"
    rich: Optional[dict]
    valueAnimation: bool = True
    offsetCenter: List[Union[int, str]] = [0, "40%"]
    formatter: Optional[dict]


class GaugeData(BaseModel):
    title: Any = Title().dict()
    detail: Any = GaugeDeatil().dict()
    name: Optional[str]
    value: Optional[int]
    itemStyle: Any = ItemStyle().dict()


class PictorialBarEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class PictorialBarDataEmphasis(BaseModel):
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class PictorialBarData(BaseModel):
    name: Optional[str]
    value: Optional[int]
    symbol: Literal[
        "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
    ] = "circle"
    symbolSize: List[Union[int, str]] = ["100%", "100%"]
    symbolPosition: Literal["start", "end", "center"] = "start"
    symbolOffset: List[Union[int, str]] = [0, 0]
    symbolRotate: Optional[int]
    symbolRepeat: Optional[Union[bool, int, str]]
    symbolRepeatDirection: Literal["start", "end"] = "start"
    symbolMargin: Optional[Union[int, str]]
    symbolClip: bool = False
    symbolBoundingData: Optional[int]
    symbolPatternSize: int = 400
    z: Optional[int]
    hoverAnimation: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDurationUpdate: int = 300
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
    animationDelay: int = 0
    animationDelayUpdate: int = 0
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = PictorialBarDataEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    tooltip: Any = ToolTip().dict()


class ThemeRiverEmphasis(BaseModel):
    focus: Literal["none", "self", "series"] = "none"
    blurScope: Literal["coordinateSystem", "series", "global"] = "coordinateSystem"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()


class ThemeRiverData(BaseModel):
    date: Optional[str]
    value: Optional[int]
    name: Optional[str]


class Line(BaseModel):
    type: Literal["line"] = "line"
    id: Optional[str]
    name: Optional[str]
    coordinateSystem: Literal["cartesian2d", "polar"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    polarIndex: int = 0
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "emptyCircle"
    symbolSize: int = 4
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    showSymbol: bool = True
    showAllSymbol: Literal["auto", True, False] = "auto"
    legendHoverLink: bool = True
    stack: Optional[str]
    cursor: Literal["pointer"] = "pointer"
    connectNulls: bool = False
    clip: bool = True
    step: bool = False
    label: Any = Label().dict()
    endLabel: Any = EndLabel().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()
    emphasis: Any = LineEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: Union[bool, Literal["single", "multiple"]] = False
    smooth: Union[bool, float] = False
    smoothMonotone: Optional[Literal["x", "y"]]
    sampling: Optional[Literal["lttb", "average", "max", "min", "sum"]]
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    data: Any = LineData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    ] = "linear"
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Bar(BaseModel):
    type: Literal["bar"] = "bar"
    id: Optional[str]
    name: Optional[str]
    coordinateSystem: Literal["cartesian2d", "polar"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    roundCap: bool = False
    showBackground: bool = False
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    labelLayout: Any = LabelLayout().dict()
    emphasis: Any = BarEmphasis().dict()
    blur: Any = Blur().dict()
    selectedMode: Union[bool, Literal["single", "multiple"]] = False
    stack: Optional[str]
    sampling: Optional[Literal["lttb", "average", "min", "max", "sum"]]
    cursor: Literal["pointer"] = "pointer"
    barWidth: Optional[Union[int, str]]
    barMaxWidth: Optional[Union[int, str]]
    barMinWidth: Optional[Union[int, str]]
    barMinHeight: int = 0
    barMinAngle: int = 0
    barGap: str = "30%"
    barCategoryGap: str = "20%"
    large: bool = False
    largeThreshold: int = 400
    progressive: int = 5000
    progressiveThreshold: int = 3000
    progressiveChunkMode: Literal["mod", "sequential"] = "mod"
    encode: Optional[dict]
    clip: bool = True
    dimensions: Optional[List[str]]
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    data: Any = BarData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    ] = "linear"
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Pie(BaseModel):
    type: Literal["pie"] = "pie"
    id: Optional[str]
    name: Optional[str]
    legendHoverLink: bool = True
    selectedMode: bool = False
    selectedOffset: int = 10
    clockwise: bool = True
    startAngle: int = 90
    minAngle: int = 0
    minShowLabelAngle: int = 0
    roseType: bool = False
    avoidLabelOverlap: bool = True
    stillShowZeroSum: bool = True
    cursor: Literal["pointer"] = "pointer"
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = 0
    top: Union[int, str] = 0
    right: Union[int, str] = 0
    bottom: Union[int, str] = 0
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = PieEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    center: List[Union[int, str]] = ["50%", "50%"]
    radius: List[Union[int, str]] = [0, "75%"]
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    data: Any = PieData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    silent: bool = False
    animationType: Literal["expansion", "scale"] = "expansion"
    animationTypeUpdate: Literal["transition", "expansion"] = "transition"
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Scatter(BaseModel):
    type: Literal["scatter"] = "scatter"
    id: Optional[str]
    name: Optional[str]
    coordinateSystem: Literal["cartesian2d", "polar", "geo"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    polarIndex: int = 0
    geoIndex: int = 0
    calendarIndex: int = 0
    legendHoverLink: bool = True
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "circle"
    symbolSize: int = 10
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    large: bool = False
    largeThreshold: int = 2000
    cursor: Literal["pointer"] = "pointer"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = ScatterEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    progressive: int = 400
    progressiveThreshold: int = 3000
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    data: Any = ScatterData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    clip: bool = True
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class EffectScatter(BaseModel):
    type: Literal["effectScatter"] = "effectScatter"
    id: Optional[str]
    name: Optional[str]
    legendHoverLink: bool = True
    effectType: Literal["ripple"] = "ripple"
    showEffectOn: Literal["render", "emphasis"] = "render"
    rippleEffect: Any = RippleEffect().dict()
    coordinateSystem: Literal["cartesian2d", "polar", "geo"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    polarIndex: int = 0
    geoIndex: int = 0
    calendarIndex: int = 0
    symbol: Literal[
        "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
    ] = "circle"
    symbolSize: int = 10
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    cursor: Literal["pointer"] = "pointer"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = EffectScatterEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    data: Any = EffectScatterData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    clip: bool = True
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Radar(BaseModel):
    type: Literal["radar"] = "radar"
    id: Optional[str]
    name: Optional[str]
    radarIndex: Optional[int]
    symbol: Literal[
        "circle", "rect", "roundRect", "triangle", "diamond", "pin", "arrow", "none"
    ] = "circle"
    symbolSize: int = 4
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    label: Any = Label().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    areaStyle: Any = AreaStyle().dict()
    emphasis: Any = RadarEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    data: Any = RadarData().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Tree(BaseModel):
    type: Literal["tree"] = "tree"
    id: Optional[str]
    name: Optional[str]
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "12%"
    top: Union[int, str] = "12%"
    right: Union[int, str] = "12%"
    bottom: Union[int, str] = "12%"
    width: Optional[Union[int, str]]
    height: Optional[Union[int, str]]
    layout: Literal["orthogonal", "radial"] = "orthogonal"
    orient: Literal["LR", "RL", "TB", "BT"] = "LR"
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "emptyCircle"
    symbolSize: int = 7
    symbolRotate: Optional[int]
    symbolKeepAspect: bool = False
    symbolOffset: List[int] = [0, 0]
    edgeShape: Literal["curve", "polyline"] = "curve"
    edgeForkPosition: str = "50%"
    roam: bool = False
    expandAndCollapse: bool = True
    initialTreeDepth: int = 2
    itemStyle: Any = ItemStyle().dict()
    label: Any = Label().dict()
    labelLayout: Any = LabelLayout().dict()
    lineStyle: Any = LineStyle().dict()
    emphasis: Any = TreeEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    leaves: Any = TreeLeaves().dict()
    data: Any = TreeData().dict()
    tooltip: Any = ToolTip().dict()


class TreeMap(BaseModel):
    type: Literal["treemap"] = "treemap"
    id: Optional[str]
    name: Optional[str]
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "center"
    top: Union[int, str] = "middle"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    width: Union[int, str] = "80%"
    height: Union[int, str] = "80%"
    squareRatio: Optional[int]
    leafDepth: Optional[int]
    drillDownIcon: str = "▶"
    roam: bool = True
    nodeClick: Literal["zoomToNode", "link", False] = "zoomToNode"
    zoomToNodeRatio: float = 0.32 * 0.32
    visualDimension: int = 0
    visualMin: Optional[int]
    visualMax: Optional[int]
    colorAlpha: Optional[List[float]]
    colorSaturation: Optional[List[float]]
    colorMappingBy: Literal["value", "id", "index"] = "index"
    visibleMin: int = 10
    childrenVisibleMin: Optional[int]
    label: Any = Label().dict()
    upperLabel: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = TreeMapEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    breadcrumb: Any = TreeMapBreadcrumb().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    levels: Any = TreeMapLevels().dict()
    data: Any = TreeMapData().dict()
    silent: bool = False
    animationDuration: int = 1500
    animationEasing: Literal[
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
    ] = "quinticInOut"
    animationDelay: int = 0
    tooltip: Any = ToolTip().dict()


class SunBurst(BaseModel):
    type: Literal["sunburst"] = "sunburst"
    id: Optional[str]
    name: Optional[str]
    zlevel: int = 0
    z: int = 2
    center: List[Union[int, str]] = ["50%", "50%"]
    radius: Any = [0, "75%"]
    data: Any = SunBurstData().dict()
    labelLayout: Any = LabelLayout().dict()
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    nodeClick: Literal["rootToNode", False, "link"] = "rootToNode"
    sort: Literal["desc", "asc", "Null"] = "desc"
    renderLabelForZeroData: bool = False
    emphasis: Any = SunBurstEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    levels: Any = SunBurstLevels().dict()
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
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
    animationDelayUpdate: int = 0


class BoxPlot(BaseModel):
    type: Literal["boxplot"] = "boxplot"
    id: Optional[str]
    coordinateSystem: Literal["cartesian2d"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    name: Optional[str]
    legendHoverLink: bool = True
    hoverAnimation: bool = True
    layout: Optional[Literal["horizontal", "vertical"]]
    boxWidth: Any = [7, 50]
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = BoxPlotEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    data: Any = BoxPlotData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animationDuration: int = 800
    animationEasing: Literal[
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
    ] = "elasticOut"
    animationDelay: int = 0
    tooltip: Any = ToolTip().dict()


class CandleStick(BaseModel):
    type: Literal["candlestick"] = "candlestick"
    id: Optional[str]
    coordinateSystem: Literal["cartesian2d"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    name: Optional[str]
    legendHoverLink: bool = True
    hoverAnimation: bool = True
    layout: Optional[Literal["horizontal", "vertical"]]
    barWidth: Optional[int]
    barMinWidth: Optional[Union[int, str]]
    barMaxWidth: Optional[Union[int, str]]
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = CandleSticEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    large: bool = True
    largeThreshold: int = 600
    progressive: int = 3000
    progressiveThreshold: int = 10000
    progressiveChunkMode: Literal["mod", "sequential"] = "mod"
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    data: Any = CandleStickData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    clip: bool = True
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animationDuration: int = 300
    animationEasing: Literal[
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
    ] = "linear"
    animationDelay: int = 0
    tooltip: Any = ToolTip().dict()


class HeatMap(BaseModel):
    type: Literal["heatmap"] = "heatmap"
    id: Optional[str]
    name: Optional[str]
    coordinateSystem: Literal["cartesian2d", "geo"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    geoIndex: int = 0
    calendarIndex: int = 0
    pointSize: int = 20
    blurSize: int = 20
    minOpacity: int = 0
    maxOpacity: int = 1
    progressive: int = 400
    progressiveThreshold: int = 3000
    label: Any = Label().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = HeatMapEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    data: Any = HeatMapData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    tooltip: Any = ToolTip().dict()


class Map(BaseModel):
    type: Literal["map"] = "map"
    id: Optional[str]
    name: Optional[str]
    map: str = ""
    roam: Literal[False, True, "scale", "move"] = False
    center: Optional[List[int]]
    aspectScale: float = 0.75
    boundingCoords: Optional[List[List[int]]]
    zoom: int = 1
    scaleLimit: Optional[dict]
    nameMap: Optional[dict]
    nameProperty: str = "name"
    selectedMode: bool = False
    label: Any = Label().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = MapEmphasis().dict()
    select: Any = Selecte().dict()
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "auto"
    top: Union[int, str] = "auto"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    layoutCenter: Optional[List[str]]
    layoutSize: Optional[int]
    geoIndex: Optional[int]
    mapValueCalculation: Literal["sum", "average", "max", "min"] = "sum"
    showLegendSymbol: Optional[bool]
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    labelLayout: Any = LabelLayout().dict()
    labelLine: Any = LabelLine().dict()
    data: Any = MapData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    silent: bool = False
    tooltip: Any = ToolTip().dict()


class Parallel(BaseModel):
    id: Optional[str]
    coordinateSystem: Literal["parallel"] = "parallel"
    parallelIndex: int = 0
    name: Optional[str]
    lineStyle: Any = LineStyle().dict()
    emphasis: Any = ParallelEmphasis().dict()
    inactiveOpacity: float = 0.05
    activeOpacity: int = 1
    realtime: bool = True
    smooth: bool = False
    progressive: int = 500
    progressiveThreshold: int = 3000
    progressiveChunkMode: Literal["sequential", "mod"] = "sequential"
    data: Any = ParallelData().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    ] = "linear"
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0


class Lines(BaseModel):
    type: Literal["lines"] = "lines"
    id: Optional[str]
    name: Optional[str]
    coordinateSystem: Literal["geo", "cartesian2d"] = "geo"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    geoIndex: int = 0
    polyline: bool = False
    effect: Any = LinesEffect().dict()
    large: bool = True
    largeThreshold: int = 2000
    symbol: Literal[
        "emptyCircle",
        "circle",
        "rect",
        "roundRect",
        "triangle",
        "diamond",
        "pin",
        "arrow",
        "none",
    ] = "none"
    symbolSize: int = 10
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    labelLayout: Any = LabelLayout().dict()
    emphasis: Any = LinesEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    progressive: int = 400
    progressiveThreshold: int = 3000
    data: Any = LinesData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    clip: bool = True
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0


class Graph(BaseModel):
    type: Literal["graph"] = "graph"
    id: Optional[str]
    name: Optional[str]
    legendHoverLink: bool = True
    coordinateSystem: Optional[Literal["none", "cartesian2d", "polar", "geo"]]
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    polarIndex: int = 0
    geoIndex: int = 0
    calendarIndex: int = 0
    center: Optional[List[int]]
    zoom: int = 1
    layout: Literal["none", "circular", "force"] = "none"
    circular: Any = GraphCircular().dict()
    force: Any = GraphForce().dict()
    roam: Literal[False, True, "scale", "move"] = False
    nodeScaleRatio: float = 0.6
    draggable: bool = False
    edgeSymbol: List[str] = ["none", "none"]
    edgeSymbolSize: int = 10
    cursor: Literal["pointer"] = "pointer"
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    label: Any = Label().dict()
    edgeLabel: Any = GraphEdgeLabel().dict()
    labelLayout: Any = LabelLayout().dict()
    emphasis: Any = GraphEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: Literal[False, True, "single", "multiple"] = False
    categories: Any = GraphCategories().dict()
    autoCurveness: Union[bool, int] = False
    data: Any = GraphData().dict()
    nodes: Optional[dict]  # GraphData().dict()
    links: Any = GraphLinks().dict()
    edges: Optional[dict]  # GraphLinks().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "center"
    top: Union[int, str] = "middle"
    right: Union[int, str] = "auto"
    bottom: Union[int, str] = "auto"
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Sankey(BaseModel):
    type: Literal["sankey"] = "sankey"
    id: Optional[str]
    name: Optional[str]
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "5%"
    top: Union[int, str] = "5%"
    right: Union[int, str] = "20%"
    bottom: Union[int, str] = "5%"
    width: Optional[Union[int, str]]
    height: Optional[Union[int, str]]
    nodeWidth: int = 20
    nodeGap: int = 8
    nodeAlign: Literal["justify", "left", "right"] = "justify"
    layoutIterations: int = 32
    orient: Literal["horizontal", "vertical"] = "horizontal"
    draggable: bool = True
    levels: Any = SankeyLevels().dict()
    label: Any = Label().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    lineStyle: Any = LineStyle().dict()
    emphasis: Any = SankeyEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    data: Any = SankeyData().dict()
    nodes: Optional[dict]  # SankeyData().dict()
    links: Any = SankeyLinks().dict()
    edges: Optional[dict]  # SankeyLinks().dict()
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    ] = "linear"
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Funnel(BaseModel):
    type: Literal["funnel"] = "funnel"
    id: Optional[str]
    name: Optional[str]
    min: int = 0
    max: int = 100
    minSize: Union[int, str] = "0%"
    maxSize: Union[int, str] = "100%"
    orient: Literal["vertical", "horizontal"] = "vertical"
    sort: Literal["descending", "ascending", "none"] = "descending"
    gap: int = 0
    legendHoverLink: bool = True
    funnelAlign: Literal["center", "left", "right"] = "center"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    itemStyle: Any = ItemStyle().dict()
    labelLayout: Any = LabelLayout().dict()
    emphasis: Any = FunnelEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = 80
    top: Union[int, str] = 60
    right: Union[int, str] = 80
    bottom: Union[int, str] = 60
    width: Union[int, str] = "auto"
    height: Union[int, str] = "auto"
    seriesLayoutBy: Literal["column", "row"] = "column"
    datasetIndex: int = 0
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    data: Any = FunnelData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class Gauge(BaseModel):
    type: Literal["gauge"] = "gauge"
    id: Optional[str]
    name: Optional[str]
    zlevel: int = 0
    z: int = 2
    center: List[str] = ["50%", "50%"]
    radius: Union[int, str] = "75%"
    legendHoverLink: bool = True
    startAngle: int = 225
    endAngle: int = -45
    clockwise: bool = True
    data: Any = GaugeData().dict()
    min: int = 0
    max: int = 100
    splitNumber: int = 10
    axisLine: Any = AxisLine().dict()
    progress: Any = Progress().dict()
    splitLine: Any = SplitLine().dict()
    axisTick: Any = AxisTick().dict()
    axisLabel: Any = AxisLabel().dict()
    pointer: Any = Pointer().dict()
    anchor: Any = Anchor().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = GaugeEmphasis().dict()
    title: Any = Title().dict()
    detail: Any = GaugeDeatil().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDelay: int = 0
    animationDurationUpdate: int = 300
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
    animationDelayUpdate: int = 0
    tooltip: Any = ToolTip().dict()


class PictorialBar(BaseModel):
    type: Literal["pictorialBar"] = "pictorialBar"
    id: Optional[str]
    name: Optional[str]
    legendHoverLink: bool = True
    coordinateSystem: Literal["cartesian2d"] = "cartesian2d"
    xAxisIndex: int = 0
    yAxisIndex: int = 0
    cursor: Literal["pointer"] = "pointer"
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = PictorialBarEmphasis().dict()
    blur: Any = Blur().dict()
    select: Optional[dict]  # Selecte().dict()
    selectedMode: bool = False
    barWidth: Optional[Union[int, str]]
    barMaxWidth: Optional[Union[int, str]]
    barMinWidth: Optional[Union[int, str]]
    barMinHeight: int = 0
    barMinAngle: int = 0
    barGap: str = "-100%"
    barCategoryGap: str = "20%"
    symbol: str = "circle"
    symbolSize: Any = ["100%", "100%"]
    symbolPosition: Literal["start", "end", "center"] = "start"
    symbolOffset: List[int] = [0, 0]
    symbolRotate: Optional[int]
    symbolRepeat: Optional[int]
    symbolRepeatDirection: Literal["start", "end"] = "start"
    symbolMargin: Optional[Union[int, str]]
    symbolClip: bool = False
    symbolBoundingData: Optional[int]
    symbolPatternSize: int = 400
    hoverAnimation: bool = False
    dimensions: Optional[List[str]]
    encode: Optional[dict]
    data: Any = PictorialBarData().dict()
    markPoint: Any = MarkPoint().dict()
    markLine: Any = MarkLine().dict()
    markArea: Any = MarkArea().dict()
    zlevel: int = 0
    z: int = 2
    silent: bool = False
    animation: bool = True
    animationThreshold: int = 2000
    animationDuration: int = 1000
    animationEasing: Literal[
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
    animationDurationUpdate: int = 300
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
    tooltip: Any = ToolTip().dict()


class ThemeRiver(BaseModel):
    type: Literal["themeRiver"] = "themeRiver"
    id: Optional[str]
    name: Optional[str]
    zlevel: int = 0
    z: int = 2
    left: Union[int, str] = "5%"
    top: Union[int, str] = "5%"
    right: Union[int, str] = "5%"
    bottom: Union[int, str] = "5%"
    width: Optional[Union[int, str]]
    height: Optional[Union[int, str]]
    coordinateSystem: Literal["single"] = "single"
    boundaryGap: Any = ["10%", "10%"]
    singleAxisIndex: int = 0
    label: Any = Label().dict()
    labelLine: Any = LabelLine().dict()
    labelLayout: Any = LabelLayout().dict()
    itemStyle: Any = ItemStyle().dict()
    emphasis: Any = ThemeRiverEmphasis().dict()
    blur: Any = Blur().dict()
    select: Any = Selecte().dict()
    selectedMode: bool = False
    data: Any = ThemeRiverData().dict()
    tooltip: Any = ToolTip().dict()


class Series(BaseModel):
    line: Any = Line().dict()
    bar: Any = Bar().dict()
    pie: Any = Pie().dict()
    scatter: Any = Scatter().dict()
    effectScatter: Any = EffectScatter().dict()
    radar: Any = Radar().dict()
    tree: Any = Tree().dict()
    treemap: Any = TreeMap().dict()
    sunburst: Any = SunBurst().dict()
    boxplot: Any = BoxPlot().dict()
    candlestick: Any = CandleStick().dict()
    heatmap: Any = HeatMap().dict()
    map: Any = Map().dict()
    parallel: Any = Parallel().dict()
    lines: Any = Lines().dict()
    graph: Any = Graph().dict()
    sankey: Any = Sankey().dict()
    funnel: Any = Funnel().dict()
    gauge: Any = Gauge().dict()
    pictorialBar: Any = PictorialBar().dict()
    themeRiver: Any = ThemeRiver().dict()


print(Series().dict().keys())
