# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:36:37 2019

@author: Ryan
"""

import pandas as pd
from pathlib import Path
import numpy as np

base_folder = Path('C:/Users/Ryan/dota2-classification')

df = pd.read_csv(base_folder / 'matches.csv')

df.head()

#top10 = df.groupby('hero_name').size().nlargest(10).index.values.tolist()
#
#rdf = df[df['hero_name'].isin(top10)]
#
#rdf.groupby('hero_name').agg({'kills':np.mean, 'assists':np.mean, 'deaths':np.mean})


top3 = df.groupby('hero_name').size().nlargest(3).index.values.tolist()

rdf = df[df['hero_name'].isin(top3)]

rdf.groupby('hero_name').agg({'kills':np.mean, 'assists':np.mean, 'deaths':np.mean})

rdf = rdf[['hero_name', 'kills', 'assists', 'deaths']]

rdf.to_csv(base_folder  / 'dataset.csv', index = False)