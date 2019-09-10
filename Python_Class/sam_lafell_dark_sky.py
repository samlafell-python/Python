#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import numpy as np

os.chdir('/Users/samlafell/Desktop/MSA/Python/Healy_Class')
print(os.getcwd())

from forecastiopy import *

api_key = 'c14295d6060f09271a3d29d107f614b2'

loc = [["Anchorage, Alaska", 61.2181, -149.9003],
       ["Buenos Aires, Argentina", -34.6037, -58.3816],
       ["Sao Jose dos Campos, Brazil", -23.2237, -45.9009],
       ['San Jose, Costa Rica', 9.9281, -84.0907],
       ['Nanaimo, Canada', 49.1659, -123.9401],
       ['Ningbo, China', 29.8683, 121.5440],
       ['Giza, Egypt', 30.0131, 31.2089],
       ['Mannheim, Germany', 49.4875, 8.4660],
       ['Hyderabad, India', 17.3850, 78.4867],
       ['Tehran, Iran', 35.6892, 51.3890],
       ['Bishkek, Kyrgyzstan', 42.8746, 74.5698],
       ['Riga, Latvia', 56.9496, 24.1052],
       ['Quetta, Pakistan', 30.1798, 66.9750],
       ['Warsaw, Poland', 52.2297, 21.0122],
       ['Dhahran, Saudi Arabia', 26.2361, 50.0393],
       ["Madrid, Spain", 40.4168, -3.7038],
       ["Oldham, United Kingdom", 53.5409, -2.1114]]

whole_list = []
new_list = []
for i in loc:
    max = []
    min = []
    city = i[0]
    latitude = i[1]
    longitude = i[2]
    weather = ForecastIO.ForecastIO(api_key, latitude=latitude, longitude=longitude, units=ForecastIO.ForecastIO.UNITS_SI)
    daily = FIODaily.FIODaily(weather)
    for day in range(2, 7):
        val = daily.get(day)
        min.append(val['temperatureMin'])
        max.append(val['temperatureMax'])
    max_mean = round((sum(max) / 5), 2)
    min_mean = round((sum(min) / 5), 2)
    max.append(max_mean)
    min.append(min_mean)
    whole_list = [city, min[0], max[0], min[1], max[1], min[2], max[2], min[3], max[3], min[4], max[4], min[5], max[5]]
    new_list.append(whole_list)

dark_sky_api = pd.DataFrame(new_list, columns=['City', 'Min 1', 'Max 1', 'Min 2', 'Max 2',
                                          'Min 3', 'Max 3', 'Min 4', 'Max 4', 'Min 5', 'Max 5', 'Min Avg', 'Max Avg'])

dark_sky_api.set_index('City', inplace=True)

dark_sky_api.to_csv('lafell_dark_sky_api.csv')

