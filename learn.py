# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:48:59 2019

@author: Ryan
"""

from pathlib import Path
from sklearn import metrics
from sklearn import tree
import pandas as pd


base_folder = Path('C:/Users/Ryan/dota2-classification')
dataset = pd.read_csv(base_folder / 'dataset.csv')

data = dataset[['kills', 'assists', 'deaths']]
target = dataset['hero_name']

model = tree.DecisionTreeClassifier()

model = model.fit(data, target)

predicted = model.predict(dataset[['kills', 'assists', 'deaths']])

print(metrics.classification_report(target, predicted))