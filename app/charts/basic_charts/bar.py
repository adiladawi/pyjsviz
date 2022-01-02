from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class _Bar(RectChart):
    """
    <<< Bar Chart >>>

    Bar chart presents categorical data with rectangular bars
    with heights or lengths proportional to the values that they represent.
    """

    def __init__(self,vars = types.Dict(
                type: ChartType.BAR,
                name: str,
                data: types.Sequence[types.Union[types.Numeric, opts.BarItem, dict]], *,
                xAxisIndex: types.Optional[types.Numeric] = None,
                yAxisIndex: types.Optional[types.Numeric] = None,
                legendHoverLink: is_legend_hover_link,
                is_selected: bool = True,
                is_legend_hover_link: bool = True,
                color: types.Optional[str] = None,
                self._append_legend(series_name, is_selected)
                showBackground: bool = False,
                backgroundStyle: types.Union[types.BarBackground, dict, None] = None,
                stack: types.Optional[str] = None,
                barWidth: types.Union[types.Numeric, str] = None,
                barMaxWidth: types.Union[types.Numeric, str] = None,
                barMinWidth: types.Union[types.Numeric, str] = None,
                barMinHeight: types.Numeric = 0,
                barCategoryGap: types.Union[types.Numeric, str] = "20%",
                barGap: types.Optional[str] = "30%",
                large: bool = False,
                largeThreshold: types.Numeric = 400,
                dimensions: types.Union[types.Sequence, None] = None,
                seriesLayoutBy: str = "column",
                datasetIndex: types.Numeric = 0,
                clip: bool = True,
                zlevel: types.Numeric = 0,
                z: types.Numeric = 2,
                label: types.Label = opts.LabelOpts(),
                markPoint: types.MarkPoint = None,
                markLine: types.MarkLine = None,
                tooltip: types.Tooltip = None,
                itemStyle: types.ItemStyle = None,
                encode: types.Union[types.JSFunc, dict, None] = None
        ))
        used = {'color','series_name','is_selected'}
        self._append_color(vars['color'])
        self._append_legend(vars['series_name'], vars['is_selected'])
        self.options.get("series").append({key:value for key,value  in vars.items() if key not in used})
        return self


class Bar(_Bar):
    """
    <<< Bar Chart >>>

    Bar chart presents categorical data with rectangular bars
    with heights or lengths proportional to the values that they represent.
    """

    def __init__(self,df = DF, x= SR, y= SR)
        return self
