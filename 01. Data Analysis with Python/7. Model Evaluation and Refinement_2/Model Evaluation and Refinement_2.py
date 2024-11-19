#Model Evaluation and Refinement (train and test)>>we can use it in every model like linear regression, multi linear regression and polynomial regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
df = pd.read_csv(filepath, header=None)
df.head()
#just get numeric data:
df=df._get_numeric_data()
df.head()

#remove the columns 'Unnamed:0.1' and 'Unnamed:0' since they do not provide any value to the models.
df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1, inplace=True)

#import libraries for plotting:
from ipywidgets import interact, interactive, fixed, interact_manual

#Functions for Plotting
def DistributionPlot(RedFunction, BlueFunction, RedName, BlueName, Title):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    
    ax1 = sns.kdeplot(RedFunction, color="r", label=RedName)
    ax2 = sns.kdeplot(BlueFunction, color="b", label=BlueName, ax=ax1)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')
    plt.show()
    plt.close()


def PollyPlot(xtrain, xtest, y_train, y_test, lr,poly_transform):
    width = 12
    height = 10
    plt.figure(figsize=(width, height))
    
    
    #training data 
    #testing data 
    # lr:  linear regression object 
    #poly_transform:  polynomial transformation object 
 
    xmax=max([xtrain.values.max(), xtest.values.max()])

    xmin=min([xtrain.values.min(), xtest.values.min()])

    x=np.arange(xmin, xmax, 0.1)


    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, y_test, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1, 1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()


#Part 1: Training and Testing
y_data = df['price']
x_data=df.drop('price',axis=1)  #Drop price data in dataframe x_data
# we randomly split our data into training and testing data using the function train_test_split.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)  #use train_test_split(x_dara, y_data)
print("number of test samples :", x_test.shape[0])  # number of test samples : 21
print("number of training samples:",x_train.shape[0])  #number of training samples: 180


#Step1: Use the function "train_test_split" to split up the dataset such that 40% of the data samples will be utilized for testing. 
# Set the parameter "random_state" equal to zero. The output of the function should be the following: "x_train1" , "x_test1", "y_train1" and "y_test1".
x_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0) 
print("number of test samples :", x_test1.shape[0])  #number of test samples : 81
print("number of training samples:",x_train1.shape[0])  #number of training samples: 120

#import LinearRegression from the module linear_model.
from sklearn.linear_model import LinearRegression

lre=LinearRegression() #create a Linear Regression object:
lre.fit(x_train[['horsepower']], y_train)  #fit the model using the feature "horsepower"
lre.score(x_test[['horsepower']], y_test)  #calculate the R^2 on the test data (answer:0.3635875575078824)
lre.score(x_train[['horsepower']], y_train) #answer:0.6619724197515103

#Step2:Find the R^2 on the test data using 40% of the dataset for testing.
x_train1, x_test1, y_train1, y_test1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
lre.fit(x_train1[['horsepower']],y_train1)
lre.score(x_test1[['horsepower']],y_test1)  #use .score() to calculate R^2


#Cross-Validation Score
from sklearn.model_selection import cross_val_score

#We input the object, the feature ("horsepower"), and the target data (y_data). The parameter 'cv' determines the number of folds. In this case, it is 4.
Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv=4)  #use cross_val_score function

#The default scoring is R^2. Each element in the array has the average R^2 value for the fold
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
print("number of test samples :", x_test.shape[0])  #number of test samples : 21
print("number of training samples:",x_train.shape[0])  #number of training samples: 180

Rcross  #array([0.7746232 , 0.51716687, 0.74785353, 0.04839605])
#We can calculate the average and standard deviation of our estimate:
print("The mean of the folds are", Rcross.mean(), "and the standard deviation is" , Rcross.std())  #The mean of the folds are 0.5220099150421197 and the standard deviation is 0.29118394447560203
#We can use negative squared error as a score by setting the parameter 'scoring' metric to 'neg_mean_squared_error'.
-1 * cross_val_score(lre,x_data[['horsepower']], y_data,cv=4,scoring='neg_mean_squared_error')   #array([20254142.84026702, 43745493.26505171, 12539630.34014929,17561927.72247586])



#Step3: Calculate the average R^2 using two folds, then find the average R^2 for the second fold utilizing the "horsepower" feature
Rc=cross_val_score(lre,x_data[['horsepower']], y_data,cv=2)
Rc.mean()  #answer:0.5166761697127429

from sklearn.model_selection import cross_val_predict
#We input the object, the feature "horsepower", and the target data y_data. The parameter 'cv' determines the number of folds. In this case, it is 4. 
yhat = cross_val_predict(lre,x_data[['horsepower']], y_data,cv=4)
yhat[0:5]  #array([14141.63807508, 14141.63807508, 20814.29423473, 12745.03562306,14762.35027598])

#Overfitting, Underfitting and Model Selection
#Let's create Multiple Linear Regression objects and train the model using 'horsepower', 'curb-weight', 'engine-size' and 'highway-mpg' as features.
lr = LinearRegression()
lr.fit(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']], y_train)

#Prediction using training data:
yhat_train = lr.predict(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_train[0:5]  #array([ 7426.6731551 , 28323.75090803, 14213.38819709,  4052.34146983,34500.19124244])

#Prediction using test data:
yhat_test = lr.predict(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']])
yhat_test[0:5]  #array([11349.35089149,  5884.11059106, 11208.6928275 ,  6641.07786278,15565.79920282])

#import neccessary libraries
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

