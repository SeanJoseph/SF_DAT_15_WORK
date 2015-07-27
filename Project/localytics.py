# -*- coding: utf-8 -*-
"""
Localytics Data Visualization Challenge
http://data-viz-challenge.localytics.com/
"""

import pandas as pd

#reading in raw json for the Localytics Data Viz Challenge
data = pd.read_json('https://raw.githubusercontent.com/localytics/data-viz-challenge/master/data.json')

#getting an understanding of the data's structure
data.head(5)
data.shape

#The raw JSON data is a series of dictionaries describing individual events
#Converting into a pandas data frame
df = pd.DataFrame([dic for dic in data['data']])
df.head()

#Location is still stores as a dictionary
#Converting location from a dictionary to individual series
loc_keys = [keys for keys in df['location'][0]]
for key in loc_keys:
    df[key] = [row[key] for row in df['location']]
df.head()

#confirming that each unqiue user only has one device type
df[['device','session_id']].groupby("session_id")\
    .agg({"device": pd.Series.nunique}).sort_index(by='device', ascending = 0).head(5)

'''
What is the question?
    Who is likely to fund a 'Sports' and/or 'Environment' project with a $20 price point
    
What are metrics or kpis to help identify our target audiance?
    ViewRate = (Users w/ View) / (Total Users)
    FundRate = (Users w/ Fund) / (Total Users)
    Fund20Rate = (Users w/ $20+ Fund) / (Total Users)
    *all metrics based on sports and environment category

What are the dimensions we can use to cluster members?
    Age, Gender, Marital Status, Device, City, State, 
    Lat/Long, Zip, Categories Viewed, Categories Funded
'''
categories = df['category'].unique() 

df.groupby(by='event_name').session_id.count()
df.groupby(by='device').session_id.count().plot(kind='bar')
df.groupby(by='category').session_id.count().plot(kind='bar')