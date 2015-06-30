'''
Class 3 Lab

'''
# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# read in the CSV file from a URL
drinks = pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/SF_DAT_15/master/data/drinks.csv', na_filter=False)


# 1. Show the first 17 rows of drinks
drinks[0:17]

# 2. create a variable called beer_servings and use it to store the beer_servings column
beer_servings = drinks['beer_servings']


# 3. Display a dataframe where the only rows are those with continent North America
drinks[drinks['continent']=='NA'] 



# 4. Create a new dataframe called north_america that holds your answer in 1.
# drinks (the dataframe) should remain unchanged

north_america = drinks[drinks['continent']=='NA'] 



# 5. What is the average wine consumption per person per year in Africa?

drinks[drinks['continent']=='AF']['wine_servings'].mean()


# 6. Create a scatter plot between spirit servings and wine servings of all countries
drinks.plot(x='spirit_servings', y='wine_servings', kind='scatter', alpha=0.3)


# 7. Show a list of the top 10 spirit drinking countries 
# (show only country names and spirit servings)
drinks[['country', 'spirit_servings']].sort_index(by='spirit_servings', ascending = 0)[0:10]


# 8. Plot 6 histograms of wine servings by continent, 
# remember to share x and share y axis scales!
drinks.wine_servings.hist(by=drinks.continent, sharex=True, sharey=True)

# 9. What is the average wine consumption in South America?
drinks[drinks.continent == 'SA'].wine_servings.mean()

# 10. Which continent has the highest on average wine consumption?
drinks.groupby('continent').wine_servings.mean()

