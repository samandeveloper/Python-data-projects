#Model Development >>calculate R^2 and MSE in different models like linear regression, multi linear regression and polynomial regression

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
lm1.fit(df[['engine-size']], df[['price']])  #in the fit we will use dataframes
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
plt.ylim(0,)   #We can see from this plot that price is negatively correlated to highway-mpg since the regression slope is negative.

#Let's compare this plot to the regression plot of "peak-rpm".
plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

#Given the regression plots above, is "peak-rpm" or "highway-mpg" more strongly correlated with "price"? Use the method ".corr()" to verify your answer.
df[["peak-rpm","highway-mpg","price"]].corr()


#Residual Plot : means observed value - predicted value
width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(x=df['highway-mpg'], y=df['price'])
plt.show()

#Multiple Linear Regression
Y_hat = lm.predict(Z)

plt.figure(figsize=(width, height))
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Y_hat, hist=False, color="b", label="Fitted Values" , ax=ax1)
plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')
plt.show()
plt.close()

#3. Polynomial Regression and Pipelines
#Polynomial regression is a particular case of the general linear regression model or multiple linear regression models
def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']

f = np.polyfit(x, y, 3)
p = np.poly1d(f)
print(p)

PlotPolly(p, x, y, 'highway-mpg')

np.polyfit(x, y, 3)   #array([-1.55663829e+00,  2.04754306e+02, -8.96543312e+03,  1.37923594e+05])


#Create 11 order polynomial model with the variables x and y from above:use np.polyfit()
f1 = np.polyfit(x, y, 11)
p1 = np.poly1d(f1)
print(p1)
PlotPolly(p1,x,y, 'Highway MPG')


#The analytical expression for Multivariate Polynomial function gets complicated. For example, the expression for a second-order (degree=2) polynomial with two variables is given by:
#Yhat = a+b1X1+b2X2+b3X1X2+b4X1^2+B5X2^2
from sklearn.preprocessing import PolynomialFeatures  #use olynomialFeatures library
pr=PolynomialFeatures(degree=2)
pr

Z_pr=pr.fit_transform(Z)
Z.shape  #(201, 4)
Z_pr.shape  #(201, 15)


#Pipeline
#Data Pipelines simplify the steps of processing the data. We use the module Pipeline to create a pipeline. We also use StandardScaler as a step in our pipeline.
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

#We create the pipeline by creating a list of tuples including the name of the model or estimator and its corresponding constructor.
Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())]

pipe=Pipeline(Input)

ypipe=pipe.predict(Z)
ypipe[0:4]   #array([13102.74784201, 13102.74784201, 18225.54572197, 10390.29636555])

#Create a pipeline that standardizes the data, then produce a prediction using a linear regression model using the features Z and target y.
Input=[('scale',StandardScaler()),('model',LinearRegression())]
pipe=Pipeline(Input)
pipe.fit(Z,y)
ypipe=pipe.predict(Z)
ypipe[0:10]


#Measures for In-Sample Evaluation
#Two very important measures that are often used in Statistics to determine the accuracy of a model are:
#both R-squared (R2) and Mean Squared Error (MSE) can be used for both linear and polynomial regression models.
##R^2 / R-squared (coefficient)>>lm.score() 
##Mean Squared Error (MSE):>> lm.predict() .The Mean Squared Error measures the average of the squares of errors. That is, the difference between actual value (y) and the estimated value (ŷ).


#Model 1: Simple Linear Regression >> lm.score() and mean_squared_error(df[],lm.predict(x)) calculates the MSE 
#calculate R-square
lm.fit(X, Y)  #highway_mpg_fit
print('The R-square is: ', lm.score(X, Y))  #The R-square is:  0.4965911884339176

Yhat=lm.predict(X)  # lm.predict() generates prediction
print('The output of the first four predicted value is: ', Yhat[0:4])  #The output of the first four predicted value is:  [16236.50464347 16236.50464347 17058.23802179 13771.3045085 ]

#Let's import the function mean_squared_error from the module metrics:
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df['price'], Yhat)  #The mean square error of price and predicted value is:  31635042.944639888
print('The mean square error of price and predicted value is: ', mse)


#Model 2: Multiple Linear Regression>> lm.score() and mean_squared_error(df[],lm.predict(Z)) calculates the MSE 
#calculate R^2
# fit the model 
lm.fit(Z, df['price'])
# Find the R^2
print('The R-square is: ', lm.score(Z, df['price']))  #The R-square is:  0.8093562806577457
Y_predict_multifit = lm.predict(Z)
print('The mean square error of price and predicted value using multifit is: ', \
      mean_squared_error(df['price'], Y_predict_multifit)) #The mean square error of price and predicted value using multifit is:  11980366.87072649


#Model 3: Polynomial Fit>>use r2_score() to calculate R^2 and mean_squared_error() to calculate MSE
#Let’s import the function r2_score from the module metrics as we are using a different function.
from sklearn.metrics import r2_score
#R^2
r_squared = r2_score(y, p(x))
print('The R-square value is: ', r_squared)
#MSE
mean_squared_error(df['price'], p(x))


#5. Prediction and Decision Making
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline 
#Create a new input:
new_input=np.arange(1, 100, 1).reshape(-1, 1)

#Fit the model:
lm.fit(X, Y)
lm

yhat=lm.predict(new_input)
yhat[0:5]   #array([37601.57247984, 36779.83910151, 35958.10572319, 35136.37234487,34314.63896655])

plt.plot(new_input, yhat)
plt.show()


# Decision Making: Determining a Good Model Fit
# Simple Linear Regression Model (SLR) vs Multiple Linear Regression Model (MLR)
# Usually, the more variables you have, the better your model is at predicting, but this is not always true. Sometimes you may not have enough data, you may run into numerical problems, or many of the variables may not be useful and even act as noise. As a result, you should always check the MSE and R^2.

# In order to compare the results of the MLR vs SLR models, we look at a combination of both the R-squared and MSE to make the best conclusion about the fit of the model.

# MSE: The MSE of SLR is 3.16x10^7 while MLR has an MSE of 1.2 x10^7. The MSE of MLR is much smaller.
# R-squared: In this case, we can also see that there is a big difference between the R-squared of the SLR and the R-squared of the MLR. The R-squared for the SLR (~0.497) is very small compared to the R-squared for the MLR (~0.809).
# This R-squared in combination with the MSE show that MLR seems like the better model fit in this case compared to SLR.

# Simple Linear Model (SLR) vs. Polynomial Fit
# MSE: We can see that Polynomial Fit brought down the MSE, since this MSE is smaller than the one from the SLR.
# R-squared: The R-squared for the Polynomial Fit is larger than the R-squared for the SLR, so the Polynomial Fit also brought up the R-squared quite a bit.
# Since the Polynomial Fit resulted in a lower MSE and a higher R-squared, we can conclude that this was a better fit model than the simple linear regression for predicting "price" with "highway-mpg" as a predictor variable.

# Multiple Linear Regression (MLR) vs. Polynomial Fit
# MSE: The MSE for the MLR is smaller than the MSE for the Polynomial Fit.
# R-squared: The R-squared for the MLR is also much larger than for the Polynomial Fit.
    
# Conclusion
# Comparing these three models, we conclude that the MLR model is the best model to be able to predict price from our dataset. This result makes sense since we have 27 variables in total and we know that more than one of those variables are potential predictors of the final car price.
















