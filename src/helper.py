# skimming function
import pandas as pd

def skim(data:pd.DataFrame, name:str):
    summary = pd.DataFrame({
                'dataset' : name,
                'column': data.columns.values,
                'data_type': data.dtypes.values,
                'unique': data.nunique().values,
                'null': data.isna().sum().reset_index()[0],
                'null_pct': round(data.isna().sum().reset_index()[0]/len(data)*100, 2),
                'zero_value' : [True if (data[col] == 0).any() else False for col in data.columns],
                'neg_value' : [True if (data[col].dtype == int or data[col].dtype == float) and (data[col] < 0).any() else False for col in data.columns],
                'min': data.dropna().min().values,
                'max': data.dropna().max().values,
                'sample_unique': [data[col].unique() for col in data.columns.values]
                })
    return summary