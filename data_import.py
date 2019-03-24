# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:20:45 2019

@author: Ryan
"""

import pandas as pd
import requests
from pandas.io.json import json_normalize
from pathlib import Path


api_key = 'b8d9dc97-b4fd-44ec-8993-8e3f9f2cd901'
payload = {'api_key':api_key}
account_id = '45576964'
base_folder = Path('C:/Users/Ryan/dota2-classification')

p = requests.get('https://api.opendota.com/api/players/' + account_id, params = payload)
profile_df = json_normalize(p.json())

r = requests.get('https://api.opendota.com/api/players/' + account_id + '/matches', params = payload)
matches_df = json_normalize(r.json())

h = requests.get('https://api.opendota.com/api/heroes', params = payload)
heroes_df = json_normalize(h.json())
hero_id_dict = pd.Series(heroes_df['localized_name'].values, index = heroes_df['id']).to_dict()

matches_df['hero_name'] = matches_df['hero_id'].map(hero_id_dict)
matches_df['start_datetime'] = pd.to_datetime(matches_df['start_time'], unit = 's')
matches_df = matches_df[matches_df['start_datetime'] <= pd.to_datetime('2019-01-01')]

profile_df.to_csv(base_folder / 'profile.csv', index = False)
matches_df.to_csv(base_folder  / 'matches.csv', index = False)

