from pandas import DataFrame
from ..translation import SetOption


def convert_df_to_dataset(df: DataFrame)-> dict: 
    dimensions = df.columns.values.tolist()
    source = df.columns.values.tolist()
    return dict(dimensions= dimensions, source = source)

setOptionDict = SetOption().dict()
print(setOptionDict)