# Localytics Data Viz Challenge

## Background:
>BootLoader is a fictional mobile app that helps people crowdfund their creative projects. Dennis Ridesalot, a BootLoader user, has a new concept for a 3-speed bicycle made from recycled parts with a $20 price point. The BootLoader team wants to send a push notification to their users, prompting them to fund the project. Create a visualization that helps the team determine what kinds of users would be interested in the bicycle project?
## Analysis:
##### Methodology:
  - Define the problem 
  - Explore and prepare data
  - Build and evaluate models 
  - Visualize results
##### Define the problem:
What groups of members that are likely to fund Ridesalot's bike project? 

##### Explore and prepare data:
The data provide by Localytics comes in the form of a JSON with two possible event types: 'View Project' and 'Fund Project'. Events have the  following information:
* `session_id`: unique identifier for each user
* `age range`: one of ['18-24', '25-34', '35-44', '45-54', '55+']
* `gender`: one of ['M', 'F', 'U']
* `location`:
 * `city`: a city in the United States
 * `state`: a state in the United States
 * `latitude`
 * `longitude`
* `marital_status`: one of ['single', 'married']
* `device`: one of ['iOS', 'android']
* `amount`: for 'Fund Project' events only

Inital invesigations of the data revealed the following:
1.  There is a 7:10 ratio between 'Fund Project' and 'View Project' events
2.  Each unique user only has 1 device
3.  35% of users are on an Android device
4.  Events are distributed evenly across the five categories

##### Build and evaluate models:
Possible approaches to be evaluated:
1. Unsupervised Learning using KNN
2. Building classification model
##### Visualize results:

