from typing import List, Literal
from pydantic import BaseModel
from pandas import DataFrame
from typing import Union

class Chart(BaseModel):
    """
    A Chart is an abstract baseclass for elements representing one or
    more independent and dependent variables. The independent variables or key
    dimensions map onto the x-axis while the dependent variables are
    usually mapped to the location, height or spread along the
    y-axis. Any number of additional value dimensions may be
    associated with a Chart
    """

    def __init__(self, data: DataFrame, kdims:Union[str,List[str]], vdims:Union[str,List[str]],title: str = None, color: str = None, size: str= None, groupby: str = None):
        self.dataset = data
        self.dimensions = self.dataset.columns.values.tolist()
        self.source = self.dataset.values.tolist()
        self.x = kdims
        self.y = vdims
        self.title = title
        self.color = color
        self.size = size
        self.groupby = groupby
        self.theme = 'light'
        self.palette = ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc']
        self.background = None
        self.heigth: int = 600
        self.width: int = 800
        self.xAxis: Union[dict,List[dict]]
        self.yAxis: Union[dict,List[dict]]
        self.charttype: Union[Literal['line', 'bar', 'pie', 'scatter', 'effectScatter', 'radar', 'tree', 'treemap', 'sunburst', 'boxplot', 'candlestick', 'heatmap', 'map', 'parallel', 'lines', 'graph', 'sankey', 'funnel', 'gauge', 'pictorialBar', 'themeRiver'],None]= None
        self.legend: Union[dict,None] = None
        self.grid: Union[dict,None] = None
        self.tooltip: Union[dict,None] = None
        self.toolbox: Union[dict,None] = None
        self.dataZoom: Union[dict,None] = None
        self.visualMap: Union[dict,None] = None
        self.text: Union[dict,None] = None
        self.markline: Union[dict,None] = None
        self.markpoint: Union[dict,None] = None
        self.markarea: Union[dict,None] = None

    def opts(self, title=None, legend=None, grid=None, tooltip=None, toolbox=None, visualMap=None, xAxis=None, yAxis=None, data=None, theme=None, palette=None, background=None, text=None, markline=None, markpoint=None, markarea=None):
        self.title = title
        self.legend = legend
        self.grid = grid
        self.tooltip = tooltip
        self.toolbox = toolbox
        self.dataZoom = toolbox
        self.visualMap = visualMap
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.dataset = data
        self.theme = theme
        self.palette = palette
        self.background = background
        self.text = text
        self.markline = markline
        self.markpoint = markpoint
        self.markarea = markarea



class Line(Chart): #Curve
    """
    Curve is a Chart element representing a line in a 1D coordinate
    system where the key dimension maps on the line x-coordinate and
    the first value dimension represents the height of the line along
    the y-axis.
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'line'



class Bar(Chart):
    """
    Bar is a Chart element representing categorical observations
    using the height of rectangular bars. The key dimensions represent
    the categorical groupings of the data, but may also be used to
    stack the bars, while the first value dimension represents the
    height of each bar.
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'bar'


class Pie(Chart):
    """
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'pie'

class Scatter(Chart):
    """
    Scatter is a Chart element representing a set of points in a 1D
    coordinate system where the key dimension maps to the points
    location along the x-axis while the first value dimension
    represents the location of the point along the y-axis.
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'scatter'


class EffectScatter(Chart):
    """
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'effectScatter'

class Parallel(Chart): 
    """
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'parallel'


class Candlestick(Chart):
    """
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'candlestick'


class Map(Chart):
    """
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'map'


class Funnel(Chart):
    """
    """
    def __init__(self, data: DataFrame, kdims: Union[str, List[str]], vdims: Union[str, List[str]], color: str, size: str, groupby: str):
        super().__init__(data, kdims, vdims, color=color, size=size, groupby=groupby)
        self.charttype = 'funnel'

