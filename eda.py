# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:36:37 2019

@author: Ryan
"""

import pandas as pd
from pathlib import Path

base_folder = Path('C:/Users/Ryan/dota2-classification')

df = pd.read_csv(base_folder / 'matches.csv')