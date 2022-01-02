from time import sleep
import pandas as pd
import panel as pn
pn.extension('echarts')


df = pd.read_json('life-expectancy-table.json')
col_names = ['Income','Life Expectancy','Population','Country','Year']
df.columns = col_names
df = df[['Year','Country','Income','Life Expectancy','Population']]
df_original = df.drop([0],axis=0)

def filtered_df(df,col, filteritem):
        df = df[df[col] == filteritem]
        return  df

def convert_to_dataset(df):
        cols = df.columns.tolist()
        values = df.values.tolist()
        return [cols] + values

def uniq_year_list(df):
        return df.iloc[:,0].unique().tolist()

def dataset_builder(df):
        Years = uniq_year_list(df)
        return [{
                'source': convert_to_dataset(filtered_df(df,'Year',year))}
                for year in Years]

option = {
    'title': {},
    'legend': {},
    'grid': {
        'left':150},
    'tooltip': {},
    'toolbox': {},
    #'dataZoom': {},
    #'visualMap': {},
    'xAxis': {
        'max': 'dataMax',
    },
    'yAxis': {
        'type': 'category',
        'inverse': True,
        'axisLabel': {
            'show': True,
            'textStyle': {
                'fontSize': 14
            },
        },
    },
    'series': [{
        'realtimeSort': True,
        'name': 'X',
        'type': 'bar',
        'encode': {
                'x': 2,
                'y': 1,
            },
        'label': {
            'show': True,
            'position': 'right',
            'valueAnimation': True
        }
    }],
    'dataset': dataset_builder(df_original)[0],
    'animationDuration': 0,
    'animationDurationUpdate': 2000,
    'animationEasing': 'linear',
    'animationEasingUpdate': 'linear'
}

echart = pn.pane.ECharts(option,width=800,height=600)
layout = pn.Column(echart)
layout.servable()

#print(dataset_builder(df_original))
for index, year in enumerate(uniq_year_list(df)):
    if index == 0:
        continue
    option['dataset'] = dataset_builder(df_original)[index]
    echart.object = option
    sleep(0.1)