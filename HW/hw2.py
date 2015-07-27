##### Part 1 #####

# 1. read in the yelp dataset
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

import statsmodels.formula.api as smf

data = pd.read_csv('/Users/SeanJoseph/GA/SF_DAT_15/hw/optional/yelp.csv')
data.head(20)

# 2. Perform a linear regression using 
# "stars" as your response and 
# "cool", "useful", and "funny" as predictors
x = data[['cool','useful','funny']]
y = data['stars']

linreg = LinearRegression()
linreg.fit(x, y)

# 3. Show your MAE, R_Squared and RMSE
y_pred = linreg.predict(x)
print metrics.mean_absolute_error(y, y_pred)
print metrics.r2_score(y, y_pred)
print np.sqrt(metrics.mean_squared_error(y, y_pred))

# 4. Use statsmodels to show your pvalues
# for each of the three predictors
# Using a .05 confidence level, 
# Should we eliminate any of the three?
lm = smf.ols(formula='stars ~ cool + useful + funny', data=data).fit()
print lm.pvalues

# 5. Create a new column called "good_rating"
# this could column should be True iff stars is 4 or 5
# and False iff stars is below 4
data['good_rating'] = (data['stars'] >= 4)
data[['good_rating','stars']].sort_index(by='stars')

# 6. Perform a Logistic Regression using 
# "good_rating" as your response and the same
# three predictors
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
x2 = data[['cool','useful','funny']]
y2 = data['good_rating']
features_train, features_test, response_train, response_test = \
    train_test_split(x2, y2, random_state=1)
    
logreg.fit(features_train, response_train)
response_pred = logreg.predict(features_test)

# 7. Show your Accuracy, Sensitivity, Specificity
# and Confusion Matrix

#Sensitivity, Specificity, Accuracy
def logreg_metrics(cmat):
    return [cmat[1][1] / float(cmat[1][0] + cmat[1][1])\
    , cmat[0][0] / float(cmat[0][0] + cmat[0][1])\
    , (cmat[0][0] + cmat[1][1]) / float((cmat.sum()))]

cm2 = metrics.confusion_matrix(response_test, response_pred)
logreg_metrics(cm2)

from sklearn import cross_validation
scores2 = cross_validation.cross_val_score(logreg,x2,y2)

# 8. Perform one NEW operation of your 
# choosing to try to boost your metrics!

#beg= 0,end=len(i))
data['isBest'] = data.apply(lambda row:\
                    (row['text'].lower().find('best') >= 0)\
                    , axis=1)
                    
from textblob import TextBlob      
data['sentiment'] = [TextBlob(unicode(txt, errors='ignore')).sentiment.polarity for txt in data['text']]             

x3 = data[['cool','useful','funny','sentiment']]
y3 = data['good_rating']
features_train, features_test, response_train, response_test = \
    train_test_split(x3, y3, random_state=1)
    
logreg.fit(features_train, response_train)
response_pred = logreg.predict(features_test)

cm3 = metrics.confusion_matrix(response_test, response_pred)
logreg_metrics(cm3)

##### Part 2 ######

# 1. Read in the titanic data set.
titanic = pd.read_csv('/Users/SeanJoseph/GA/SF_DAT_15/data/titanic.csv')

# 4. Create a new column called "wife" that is True
# if the name of the person contains Mrs.
# AND their SibSp is at least 1
titanic['wife'] = titanic.apply(lambda row:\
                    (row['Name'].lower().find('mrs.') >= 0) &\
                    row['SibSp'] >= 1, axis=1)
                    
# 5. What is the average age of a male and
# the average age of a female on board?
male_avg_age = titanic[titanic['Sex']=='male']['Age'].mean()
female_avg_age = titanic[titanic['Sex']=='female']['Age'].mean()

# 5. Fill in missing MALE age values with the
# average age of the remaining MALE ages

def conditional_nan(row):
    if pd.isnull(row['Age']):
        if row['Sex'] == 'male':
            return male_avg_age
        else:
            return female_avg_age
    else:
        return row['Age']

titanic['Age'] = titanic.apply(lambda row: conditional_nan(row), axis=1)

# 6. Fill in missing FEMALE age values with the
# average age of the remaining FEMALE ages

'''See the above code'''

# 7. Perform a Logistic Regression using
# Survived as your response and age, wife
# as predictors

titanic.head()
x4 = titanic[['Age','wife']]
y4 = titanic['Survived']
features_train, features_test, response_train, response_test = \
    train_test_split(x4, y4, random_state=1)
    
logreg.fit(features_train, response_train)
response_pred = logreg.predict(features_test)
zip(['Age','wife'],logreg.coef_[0])

# 8. Show Accuracy, Sensitivity, Specificity and 
# Confusion matrix
cm4 = metrics.confusion_matrix(response_test, response_pred)
logreg_metrics(cm4)

# 9. now use ANY of your variables as predictors
# Still using survived as a response to boost metrics!
titanic['isMale'] = [sex == 'male' for sex in titanic['Sex']]
train, test = train_test_split(titanic, test_size = 0.3)

x5 = titanic[['Age','isMale','wife']]
y5 = titanic['Survived']
features_train, features_test, response_train, response_test = \
    train_test_split(x5, y5, random_state=1)
    
logreg.fit(features_train, response_train)
response_pred = logreg.predict(features_test)

# 10. Show Accuracy, Sensitivity, Specificity
cm5 = metrics.confusion_matrix(response_test, response_pred)
logreg_metrics(cm5)

# REMEMBER TO USE
# TRAIN TEST SPLIT AND CROSS VALIDATION
# FOR ALL METRIC EVALUATION!!!!

