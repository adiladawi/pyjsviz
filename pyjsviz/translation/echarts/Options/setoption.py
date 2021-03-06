from calendar import Calendar
from typing import Any
from typing import List
from typing import Literal
from typing import Optional

from angleaxis import AngleAxis
from axispointer import AxisPointer
from brush import Brush
from dataset import Dataset
from datazoom import DataZoom
from geo import Geo
from graphic import Graphic
from grid import Grid
from legend import Legend
from parallel import Parallel
from parallelaxis import ParallelAxis
from polar import Polar
from pydantic import BaseModel
from radar import Radar
from radiusaxis import RadiusAxis
from series import Series
from singleaxis import SingleAxis
from textstyle import TextStyle
from timeline import TimeLine
from title import Title
from toolbox import ToolBox
from tooltip import ToolTip
from visualmap import VisualMap
from xaxis import XAxis
from yaxis import YAxis


class StateAnimation(BaseModel):
    duration: int = 300
    easing: Literal[
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


class SetOption(BaseModel):
    title: Any = Title().dict()
    legend: Any = Legend().dict()
    grid: Any = Grid().dict()
    xAxis: Any = XAxis().dict()
    yAxis: Any = YAxis().dict()
    polar: Any = Polar().dict()
    radiusAxis: Any = RadiusAxis().dict()
    angleAxis: Any = AngleAxis().dict()
    radar: Any = Radar().dict()
    dataZoom: Any = [i for i in DataZoom().dict().values()]
    visualMap: Any = [i for i in VisualMap().dict().values()]
    tooltip: Any = ToolTip().dict()
    axisPointer: Any = AxisPointer().dict()
    toolbox: Any = ToolBox().dict()
    brush: Any = Brush().dict()
    geo: Any = Geo().dict()
    parallel: Any = Parallel().dict()
    parallelAxis: Any = ParallelAxis().dict()
    singleAxis: Any = SingleAxis().dict()
    timeline: Any = TimeLine().dict()
    graphic: Any = Graphic().dict()
    calendar: Any = Calendar().dict()
    dataset: Any = Dataset().dict()
    series: Any = [i for i in Series().dict().values()]
    color: Optional[List[str]]
    backgroundColor: Optional[str]
    textStyle: Any = TextStyle().dict()
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
    stateAnimation: Any = StateAnimation().dict()
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
    hoverLayerThreshold: int = 3000
    useUTC: bool = False


print(SetOption().json())
