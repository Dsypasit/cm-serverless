import pandas as pd

data = pd.read_csv('data/hs.csv')
section = pd.read_csv('data/sections.csv')
def handler_get_hscode(event, context):
    data = pd.read_csv('data/hs.csv')
    return data.to_json(orient='records')
# print(data.head())
# print(section.head())
# print(data[data['section'] == 'I'].tail())