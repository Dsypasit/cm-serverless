import pandas as pd
import json

data = pd.read_csv('data/hs.csv')
section = pd.read_csv('data/sections.csv')
def handler(event, context):
    # Parse the event payload
    payload = event['body']
    
    # Check if the 'handler' key is present in the payload
    if 'handler' in payload:
        # Extract the handler function name from the payload
        handler_function_name = payload['handler']
        
        # Dynamically invoke the corresponding handler function
        if handler_function_name == 'get_hs_code':
            return handler_get_hscode(payload, context)
    
    # Default behavior if 'handler' key is not present or unknown handler name
    return {
        'statusCode': 400,
        'body': 'Invalid or missing handler name in payload'
    }

def handler_get_hscode(event, context):
    data = pd.read_csv('data/hs.csv')
    return data.to_dict(orient='records')
# print(data.head())
# print(section.head())
# print(data[data['section'] == 'I'].tail())