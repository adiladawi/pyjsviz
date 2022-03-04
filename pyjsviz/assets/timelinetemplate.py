import pandas as pd
import panel as pn
pn.extension('echarts')


df = pd.read_csv('china_cities_GDP.csv')

def cols_list(df):
    return  df.columns.tolist()[1:]

def uniq_cat_list(df):
    return df.iloc[:,0].to_list()


def optins_builder(df,series_title):
    options = []
    col_list = cols_list(df)
    for col in col_list:
        single_option = {"title" :{"text": f'{col} {series_title}'},
        "series": [
        {"data": df[col].to_list()}
        ]}
        options.append(single_option)
    return options


class BarTimeline():
    def __init__(self) -> None:
        pass
    
    def __new__(cls,df:pd.DataFrame,series_title: str,chart_desc: str,yAxis_desc: str):
        return {
            'baseOption': {
                'timeline': {
                    'axisType': 'category',
                    'autoPlay': True,
                    'playInterval': 1000,
                    'data': cols_list(df)
                },
                'title': {
                    'subtext': chart_desc
                },
                'tooltip': {},
                'legend':{
                    'left': 'right',
                },
                'calculable' : True,
                'grid': {
                    'top': 80,
                    'bottom': 100
                },
                'xAxis': [
                    {
                    'type':'category',
                    'axisLabel':{'interval':0},
                    'data': uniq_cat_list(df),
                    'splitLine': {'show': False}
                    }],
                'yAxis': [
                    {
                    'type': 'value',
                    'name': yAxis_desc,
                    }],
                'series': [
                    {'name' :series_title ,'type': 'bar'}
                    ]
            },
            'options': optins_builder(df,series_title),
        }

print(optins_builder(df,'GDP'))

echart = pn.pane.ECharts(BarTimeline(df,'GDP','this should work','no one cares'),width=1200,height=600,theme='blue')
echart.servable()