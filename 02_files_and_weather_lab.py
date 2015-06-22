

'''
PART 1:
Read in drinks.csv
Store the header in a list called 'header'
Store the data in a list of lists called 'data'
Hint: you've already seen this code!
'''
import csv
with open('/Users/SeanJoseph/GA/SF_DAT_15/data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]

'''
PART 2:
Isolate the beer_servings column in a list of integers called 'beers'
Hint: you can use a list comprehension to do this in one line
Expected output:
    beers == [0, 89, ..., 32, 64]
    len(beers) == 193
'''

beers = [row[1] for row in data]



'''
PART 3:
Create separate lists of NA and EU beer servings: 'NA_beers', 'EU_beers'
Hint: you can use a list comprehension with a condition
Expected output:
    NA_beers == [102, 122, ..., 197, 249]
    len(NA_beers) == 23
    EU_beers == [89, 245, ..., 206, 219]
    len(EU_beers) == 45
'''

NA_beers = [row[1] for row in data if row[5] == 'NA' ]
#len(NA_beers) == 23
EU_beers = [row[1] for row in data if row[5] == 'EU' ]
#len(EU_beers) == 45



'''
PART 4:
Calculate the average NA and EU beer servings to 2 decimals: 'NA_avg', 'EU_avg'
Hint: don't forget about data types!
Expected output:
    NA_avg == 145.43
    EU_avg == 193.78
'''

NA_avg = round(((sum(float(num) for num in NA_beers))/len(NA_beers)),2)
EU_avg = round(((sum(float(num) for num in EU_beers))/len(EU_beers)),2)
NA_avg == 145.43
EU_avg == 193.78


'''
PART 5:
Write a CSV file called 'avg_beer.csv' with two columns and three rows.
The first row is the column headers: 'continent', 'avg_beer'
The second and third rows contain the NA and EU values.
Hint: think about what data structure will make this easy
Expected output (in the actual file):
    continent,avg_beer
    NA,145.43
    EU,193.78
'''
output = [['continent','avg_beer'],['NA',NA_avg],['EU',EU_avg]]
with open('avg_beer.csv', 'wb') as f:
    csv.writer(f).writerows(output)

'''
Part 6:
Use the requests module to pull in weather data for any city
Hint: you can use Istanbul from the other code file but you can search
for cities at http://openweathermap.org/find

Create a dates list that stores the date of each datapoint as well as
temperature and humidity

You've already seen this code!
'''

import requests
api_endpoint = 'http://api.openweathermap.org/data/2.5/forecast/city'
params = {}
params['id'] = '745044'
params['units'] = 'metric'
params['APPID'] = '80575a3090bddc3ce9f363d40cee36c2'
request = requests.get(api_endpoint, params = params)
data = request.json()

from datetime import datetime
dates = [item['dt'] for item in data['list']]
dates = [datetime.fromtimestamp(epoch) for epoch in dates]
temps = [item['main']['temp'] for item in data['list']]
humiditys = [item['main']['humidity'] for item in data['list']]

'''
Part 7
Create a list of the pressure measurements and plot it against dates
'''
pressure = [item['main']['pressure'] for item in data['list']]
import matplotlib.pyplot as plt
plt.xlabel("Date")                         
plt.ylabel("Pressue")         
plt.title("Pressue over Time")
locs, labels = plt.xticks()              
plt.setp(labels, rotation=70) 
plt.plot(dates, pressure)

'''
Part 8
Make a scatter plot plotting pressure against temperature and humidity
'''
plt.scatter(temps,humiditys)
plt.xlabel("Temperature")                         
plt.ylabel("Humidity")        
plt.show()
'''