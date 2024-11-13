#Model Development

#install neccessary libraries:
#! mamba install pandas==1.3.3-y
#! mamba install numpy=1.21.2-y
#! mamba install sklearn=0.20.1-y

import piplite
await piplite.install('seaborn')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv"
df = pd.read_csv(filepath, header=None)

#1. Linear Regression and Multiple Linear Regression (Yhat = a+bX)
#Simple Linear Regression is a method to help us understand the relationship between two variables:
##The predictor/independent variable (X)
##The response/dependent variable (that we want to predict)(Y)
#The result of Linear Regression is a linear function that predicts the response (dependent) variable as a function of the predictor (independent) variable.

#load the modules for linear regression
from sklearn.linear_model import LinearRegression

#Create the linear regression object
lm = LinearRegression()
lm

#How could "highway-mpg" help us predict car price?
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X,Y)

Yhat=lm.predict(X)
Yhat[0:5]

#What is the value of the intercept (a)?
lm.intercept_

#What is the value of the slope (b)?
lm.coef_

#Q1:Create a linear regression object called "lm1".
lm1 = LinearRegression()
lm1

#Q2:Train the model using "engine-size" as the independent variable and "price" as the dependent variable?
lm1.fit(df[['engine-size']], df[['price']])
lm1

#Q3:Find the slope and intercept of the model.
# Slope 
lm1.coef_     #answer b: array([[166.86001569]])
# Intercept
lm1.intercept_    #answer a: array([-7963.33890628])


#Q4:What is the equation of the predicted line? You can use x and yhat or "engine-size" or "price".
# using X and Y  
Yhat=-7963.34 + 166.86*X
Price=-7963.34 + 166.86*df['engine-size']


#2. Multiple Linear Regression: Yhat = a+b1X1+b2X2+b3X3+b4X4
#a is intercept and b is coefficient

#From the previous section we know that other good predictors of price could be:
#Horsepower
#Curb-weight
#Engine-size
#Highway-mpg

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
#Fit the linear model using the four above-mentioned variables.
lm.fit(Z, df['price'])

#What is the value of the intercept(a)?
lm.intercept_   #-15806.62462632922
#What are the values of the coefficients (b1, b2, b3, b4)?
lm.coef_   #array([53.49574423,  4.70770099, 81.53026382, 36.05748882])


#Create and train a Multiple Linear Regression model "lm2" where the response variable is "price", and the predictor variable is "normalized-losses" and "highway-mpg".
lm2 = LinearRegression()
lm2.fit(df[['normalized-losses' , 'highway-mpg']],df['price'])

#Find the coefficient of the model.
lm2.coef_  #array([   1.49789586, -820.45434016])

# 3. Model Evaluation Using Visualization
#Import the visualization package, seaborn:
import seaborn as sns
%matplotlib inline

#Regression Plot
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)



