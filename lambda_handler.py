import pandas as pd
import json

data = pd.read_csv('data/hs.csv')
section = pd.read_csv('data/sections.csv')
def handler(event, context):

    try:
        handler_function_name = json.loads(event['body'])['handler']
        
        # Dynamically invoke the corresponding handler function
        if handler_function_name == 'get_hs_code':
            return handler_get_hscode(event, context)
        else:
            return {
                'statusCode': 400,
                'body': 'Invalid or missing handler name in payload'
            }

    except:
        return {
            'statusCode': 400,
            'body': 'Invalid or missing handler name in payload'
        }

def handler_get_hscode(event, context):
    data = pd.read_csv('data/hs.csv')
    return {
        'body': data.to_json(orient='records'),
        'statusCode': 200
    }
# print(data.head())
# print(section.head())
# print(data[data['section'] == 'I'].tail())