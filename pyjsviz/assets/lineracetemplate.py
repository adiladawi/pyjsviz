import pandas as pd
import panel as pn
pn.extension('echarts')
import json


df = pd.read_json('life-expectancy-table.json')
col_names = ['Income','Life Expectancy','Population','Country','Year']
df.columns = col_names
df = df[['Year','Country','Income','Life Expectancy','Population']]
df_original = df.drop([0],axis=0)
countries = ['Finland', 'France', 'Germany', 'Iceland', 'Norway', 'Poland', 'Russia', 'United Kingdom']
df = df_original[df_original.Country.isin(countries)]

def filtered_df(df,col, filteritem):
        df = df[df[col] == filteritem]
        return  df


def convert_to_dataset(df):
        cols = df.columns.tolist()
        values = df.values.tolist()
        return [cols] + values
    

def uniq_con_list(df):
        return df.iloc[:,1].unique().tolist()

def dataset_builder(df):
        countries = uniq_con_list(df)
        return [{'id': f'dataset_{country}',
                'source': convert_to_dataset(filtered_df(df,'Country',country))}
                for country in countries]

def series_builder(df):
        series = []
        countries = uniq_con_list(df)
        for country in countries:
            single_series = {
                'type': 'line',
                'datasetId': f'dataset_{country}',
                'showSymbol': False,
                'name': country,
                'labelLayout': {
                    'moveOverlap': 'shiftY'
                },
                'emphasis': {
                    'focus': 'series'
                },
                'encode': {
                'x': 'Year',
                'y': 'Income',
                'label': ['Country', 'Income'],
                'itemName': 'Year',
                'tooltip': ['Income'],
            },
            }
            series.append(single_series)
        return series

#print(dataset_builder(df))

class BarTimeline():
    def __init__(self) -> None:
        pass
    
    def __new__(cls,df,title: str,yAxis_desc: str):
        return  {
        'animationDuration': 10000,
        'dataset': dataset_builder(df),
        'title': {
            'text': title
        },
        'tooltip': {
            'order': 'valueDesc',
            'trigger': 'axis'
        },
        'xAxis': {
            'type': 'category',
            'nameLocation': 'middle'
        },
        'yAxis': {
            'name': yAxis_desc
        },
        'grid': {
            'right': 140
        },
        'series': series_builder(df)
    }

#print(BarTimeline(df,'this should work','no one cares'))

echart = pn.pane.ECharts(BarTimeline(df,'this should work','no one cares'),width=800,height=600)
echart.servable()