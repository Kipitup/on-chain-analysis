# import json
import pandas as pd
import pprint as pp
import requests
from configparser import ConfigParser

def glassnode_api_key():
    # Grab the config file values
    config = ConfigParser()
    config.read('config_file.ini')

    # insert your API key here
    API_KEY = config.get('main', 'API_KEY')

    # List of available endpoints and supported options
    print("="*80)
    print("List of available endpoints and supported options")
    print("-"*80)
    res = requests.get('https://api.glassnode.com/v2/metrics/endpoints',
        params={'api_key': API_KEY})
    df_list_endpoint = pd.read_json(res.text)
    pp.pprint(df_list_endpoint)

    print("="*80)
    # make API request
    res = requests.get('https://api.glassnode.com/v1/metrics/indicators/sopr',
        params={'a': 'BTC', 'api_key': API_KEY})

    # convert to pandas dataframe
    df = pd.read_json(res.text, convert_dates=['t'])

    pp.pprint(df)