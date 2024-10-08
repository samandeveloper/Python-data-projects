#House Sales in King County, USA 

#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
%matplotlib inline

#Module 1: Importing Data Sets
import piplite
await piplite.install('seaborn')

filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
df = pd.read_csv(filepath, header=None)
df.head()

#Display the data types of each column using the function dtypes
df.dtypes

#step1:Display the data types of each column using the function dtypes. 
df.dtypes

#step2:Data Wrangling
df.drop(columns=['id', 'Unnamed: 0'], inplace=True)
df.head()

#step3:Exploratory Data Analysis
#Use the method value_counts to count the number of houses with unique floor values, use the method .to_frame() to convert it to a data frame. 

#value_counts() can be used on both DataFrame columns and Series, but it returns a Series, not a DataFrame.
df['floors'].value_counts().to_frame()
df

#step4: Use the function boxplot in the seaborn library to determine whether houses with a waterfront view or without a waterfront view have more price outliers.
#waterfront column can be 0 or 1
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x="waterfront", y="price", data=df)
plt.title("House Prices: Waterfront vs Non-Waterfront Properties")
plt.xlabel("Waterfront")
plt.ylabel("Price")
plt.show()

#step5: Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price. 
import seaborn as sns
import matplotlib.pyplot as plt

sns.regplot(x="sqft_above", y="price", data=df)
plt.title("Relationship between sqft_above and Price")
plt.xlabel("Square Feet Above Ground")
plt.ylabel("Price")
plt.show()


#step6: Model Development
#We can Fit a linear regression model using the longitude feature 'long' and caculate the R^2.
from sklearn.linear_model import LinearRegression
X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)  #0.00046769430149007363

#Fit a linear regression model to predict the 'price' using the feature 'sqft_living' then calculate the R^2.
#Enter Your Code, Execute and take the Screenshot
import pandas as pd
from sklearn.linear_model import LinearRegression
x = df[['sqft_living']]  # Feature
y = df['price']          # Target variable
lm =LinearRegression()
lm.fit(x,y)  #fit the model to the data
r_squared = lm.score(X, Y)  #calculate R^2
print(r_squared)  #answer:0.4928532179037931

#step7: Fit a linear regression model to predict the 'price' using the list of features
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]     
import pandas as pd
from sklearn.linear_model import LinearRegression

x= df[features]
y= df['price']

lm = LinearRegression()
# Fit the model to the data
lm.fit(x, y)

# Calculate the R² score
r_squared = lm.score(x, y)
print(r_squared)  #answer: 0.6576890354915759


#step8: Use the list to create a pipeline object to predict the 'price', fit the object using the features in the list features, and calculate the R^2. 
# Create a list of tuples, the first element in the tuple contains the name of the estimator:

# 'scale'

# 'polynomial'

# 'model'

# The second element in the tuple contains the model constructor

# StandardScaler()

# PolynomialFeatures(include_bias=False)

# LinearRegression()

Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression

input_estimators = [  #input_estimators which are steps in the pipeline is a list
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]

# Create a pipeline object
pipeline = Pipeline(steps=input_estimators)

pipeline.fit(x,y)
r_squared = pipeline.score(x, y)
print(r_squared)  #answer:0.7512051345272872



#Model Evaluation and Refinement
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

#step9: We will split the data into training and testing sets:
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

print("number of test samples:", x_test.shape[0])  #number of test samples: 3242
print("number of training samples:",x_train.shape[0])  # number of training samples: 18371

#step9: Ridge regression model: 
# Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data. 
#we usually use ridge regression to prevent overfitting in the model since it will give us higher R^2 
#Ridge regression can be applied to both simple linear regression and polynomial regression, as well as other regression forms. Its primary purpose is to manage the model complexity and prevent overfitting
# we also can use cross validation to find the most suitable alpha in the Ridge regression (min 0)
from sklearn.linear_model import Ridge
ridge_model = Ridge(alpha=0.1)  # Set regularization parameter to 0.1
ridge_model.fit(x_train, y_train)

r_squared = ridge_model.score(x_test, y_test)  #calculate R^2
print(r_squared)  #answer:0.647875916393907



#Step10: 
#Perform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided.
poly = PolynomialFeatures(degree=2, include_bias=False)
x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test) #usually .fit_transform is for train data and .transform is for test data
ridge = Ridge(alpha=0.1)
ridge.fit(x_train_poly, y_train)
r_squared = ridge.score(x_test_poly, y_test)
print(r_squared)  #answer:0.700274425803224




