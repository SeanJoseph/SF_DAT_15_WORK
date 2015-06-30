'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('../hw/data/police-killings.csv')
killings.head(1)

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
killings.rename(columns={'lawenforcementagency':'agency'
                    ,'raceethnicity':'race'}
                    , inplace = True)
killings.columns 

# 2. Show the count of missing values in each column
for col in killings:
    print col + ' ' + str(killings[col].isnull().sum())

# 3. replace each null value in the dataframe with the string "Unknown"
for col in killings:
    killings[col].fillna(value='Unknown',inplace=True)

# 4. How many killings were there so far in 2015?
killings[killings['year']==2015].count()
 
# 5. Of all killings, how many were male and how many female?
killings['gender'].value_counts()

# 6. How many killings were of unarmed people?
killings[killings['armed']=='No'].shape[0]

# 7. What percentage of all killings were unarmed?
float(killings[killings['armed']=='No'].shape[0]) / killings['armed'].count()

# 8. What are the 5 states with the most killings?
killings.groupby('state').city.count().order(ascending = 0).head(5)

# 9. Show a value counts of deaths for each race
killings['race'].value_counts()

# 10. Display a histogram of ages of all killings
killings.age.hist()

# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings['race'])

# 12. What is the average age of death by race?
killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month
month_map = {'January':0,'February':1,'March':2,'April':3,'May':4,'June':5}
killings['num_month']=killings['month'].map(month_map)
killings.groupby(['num_month','month']).city.count().plot(kind='bar')

###################
### Less Morbid ###
###################

majors = pd.read_csv('../hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
del majors['Employed_full_time_year_round']
del majors['Major_code']

# 2. Show the cout of missing values in each column
for col in majors:
    print col + ' ' + str(majors[col].isnull().sum())

# 3. What are the top 10 highest paying majors?
majors[['Major','Median']].sort_index(by='Median', ascending = 0).head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
majors[['Major','Median']].sort_index(by='Median', ascending = 0)[:10].plot(\
     x = 'Major'\
    , y = 'Median'\
    , kind = 'bar'\
    , title = 'Median Salary by Major'\
    )




# 5. What is the average median salary for each major category?
majors.groupby('Major_category').Median.mean()

# 6. Show only the top 5 paying major categories
cats = majors.groupby('Major_category').Median.max()
cats.sort(ascending = 0)
cats.head(10)

# 7. Plot a histogram of the distribution of median salaries
majors['Median'].hist()

# 8. Plot a histogram of the distribution of median salaries by major category
majors.groupby('Major_category')['Median'].mean().plot(kind='bar')

# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?
majors[['Major','Unemployment_rate']].sort_index(by='Unemployment_rate',\
    ascending = 0).head(10)

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?
majors.groupby('Major_category')[['Unemployment_rate']].mean().\
    sort_index(by='Unemployment_rate', ascending = 0).head(10)

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

majors['sample_employment_rate'] = majors['Employed']/majors['Total']*1.0


# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
majors['sample_unemployment_rate']=1-majors['sample_employment_rate'] 
