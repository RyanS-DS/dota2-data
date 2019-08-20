# dota2-data

This is a brief data exploration and modeling based around data from my own DOTA 2 matches, pulled via OpenDota API.

**Note: to use this yourself you will need to create a config.py file containing an OpenDota API key.**

### See *data_import.py* for instructions on how the data was imported and some brief cleaning
### See _DOTA 2 Data Exploration.ipynb_ for an exploration of the data and generation of ideas for models
### See _DOTA 2 Model Building.ipynb_ for a model build of a logistic regression, then a random forest

There is much more that can be done with the OpenDota API, as it contains the data for every DOTA match ever played in painstaking detail.

Some ideas to work on in future:

1. Extract data on pro matches and build a profit-making predictor model.
2. Build dashboards showing averages and items for each hero, to assist with strategy whilst in-game.
