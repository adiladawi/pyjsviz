from turtle import width
import pandas as pd
import panel as pn
pn.extension('echarts')
dftest = pd.read_csv('china_cities_GDP.csv')

option = {
    'title': {...},
    'legend': {...},
    'grid': {...},
    'tooltip': {...},
    'toolbox': {...},
    'dataZoom': {...},
    'visualMap': {...},
    'xAxis': [
        {'type': 'category',},
        {'type': 'category',},
        {'type': 'value',}
    ],
    'yAxis': [{...}, {...}],
    'series': [
        {'type': 'line', 'data': [['AA', 332], ['CC', 124], ['FF', 412], ... ]},
        {'type': 'line', 'data': [2231, 1234, 552, ... ]},
        {'type': 'line', 'data': [[4, 51], [8, 12], ... ]}
    ]
}
