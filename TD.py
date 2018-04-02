# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import datetime as dt

# Reading the data (sample)
data_s = pd.read_csv('train_sample.csv').fillna('')#, parse_dates = ['attributed_time'])



pd.datetime(data_s.click_time)

data_s.click_time = pd.to_datetime(data_s.click_time, errors = 'ignore')
data_s.attributed_time = pd.to_datetime(data_s.attributed_time, errors = 'ignore')
data_s[data_s.attributed_time == 'NaT']
.fillna('')

data_s['click_time'] - ['data_s.attributed_time']
pd.datetime.now() - data_s.attributed_time

np.where(data.attributed_time.isnull()==False, data_s['click_time'] - ['data_s.attributed_time'], 0)
data_s.head()
data_s.shape
data_s.click_time
pd.datetime(data_s.click_time)
# Checking for NANs
for col in data_s.columns:
    print(len(data_s[data_s[col].isnull()]))

## attributed_time has 97K NAN 
data_s[data_s.attributed_time.isnull()]

## Coded those as 0
data_s.attributed_time = np.where(data_s.attributed_time != 1,0,1)


for col in data_s.columns:
    print(len(data_s[data_s[col] != '']))

data_s.dtypes

data[data.attributed_time.isnull()==False]


data
data.ip.isnull()
data.isnull().values


data[data.isnull().any(1)]