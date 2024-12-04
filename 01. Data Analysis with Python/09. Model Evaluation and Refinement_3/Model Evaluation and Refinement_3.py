#Model Evaluation and Refinement2

import piplite
await piplite.install('seaborn')
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures

filepath = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv'
df = pd.read_csv(filepath, header=None)
df.head()

#Task 1 : Using Cross validation to improve the model
#Divide the dataset into x_data and y_data parameters. Here y_data is the "Price" attribute, and x_data has all other attributes in the data set.
y_data = df['Price']
x_data = df.drop('Price',axis=1) #drop the price column (axis=1 is the column)

#Split the data set into training and testing subests such that you reserve 10% of the data set for testing purposes.
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1) #every time the data split can be changed
print("number of test samples :", x_test.shape[0])  #number of test samples : 24
print("number of training samples:",x_train.shape[0])   #number of training samples: 214

#Create a single variable linear regression model using "CPU_frequency" parameter. Print the R^2 value of this model for the training and testing subsets.
lre = LinearRegression()
lre.fit(x_train[['CPU_frequency']], y_train)
print(lre.score(x_test[['CPU_frequency']], y_test))  #-0.06599437350393766
print(lre.score(x_train[['CPU_frequency']], y_train))  #0.14829792099817962

#Run a 4-fold cross validation on the model and print the mean value of R^2 score along with its standard deviation.
Rcross = cross_val_score(lre, x_data[['CPU_frequency']], y_data, cv=4)
print("The mean of the folds are", Rcross.mean(), "and the standard deviation is" , Rcross.std())  #The mean of the folds are -0.1610923238859522 and the standard deviation is 0.38495797866647274

#Task 2: Overfitting
#Split the data set into training and testing components again, this time reserving 50% of the data set for testing.
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.5, random_state=0)

#To identify the point of overfitting the model on the parameter "CPU_frequency", you'll need to create polynomial features using the single attribute. You need to evaluate the R^2 scores of the model created using different degrees of polynomial features, ranging from 1 to 5. Save this set of values of R^2 score as a list.
#Fitting: When you call fit_transform, it learns the necessary parameters (like the degree of the polynomial) based on the input data. In the case of polynomial features, it determines how to create the new feature set based on the specified degree.
lre = LinearRegression()
Rsqu_test = []  #This list will store the R² (coefficient of determination) scores for each polynomial degree evaluated later.
order =[1,2,3,4,5]  #Defines a list order containing the polynomial degrees to be tested.
for n in order: #Begins a for loop that iterates over each value in the order
    pr = PolynomialFeatures(degree=n)
    x_train_pr = pr.fit_transform(x_train[['CPU_frequency']])  # (fi_transform method usually happen in the polynomial model on the train not the test data) Fits the PolynomialFeatures transformer to the CPU_frequency column from the x_train DataFrame and transforms it into polynomial features.
    x_test_pr = pr.fit_transform(x_test[['CPU_frequency']])
    lre.fit(x_train_pr, y_train)
    Rsqu_test.append(lre.score(x_test_pr, y_test)) #append to the empty array

#Plot the values of R^2 scores against the order. Note the point where the score drops.
plt.plot(order, Rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 Using Test Data')

#Task 3 : Ridge Regression
#Now consider that you have multiple features, i.e. 'CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core','OS','GPU' and 'Category'. Create a polynomial feature model that uses all these parameters with degree=2. Also create the training and testing attribute sets.
pr=PolynomialFeatures(degree=2)
x_train_pr=pr.fit_transform(x_train[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS', 'GPU', 'Category']])
x_test_pr=pr.fit_transform(x_test[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS', 'GPU', 'Category']])

#Create a Ridge Regression model and evaluate it using values of the hyperparameter alpha ranging from 0.001 to 1 with increments of 0.001. Create a list of all Ridge Regression R^2 scores for training and testing data.
Rsqu_test = []
Rsqu_train = []
Alpha = np.arange(0.001,1,0.001)  #Creates a NumPy array Alpha containing values from 0.001 to just below 1 (inclusive) in increments of 0.001. 
pbar = tqdm(Alpha)  #this line is nort neccessary but it will help

for alpha in pbar:
    RigeModel = Ridge(alpha=alpha) 
    RigeModel.fit(x_train_pr, y_train)
    test_score, train_score = RigeModel.score(x_test_pr, y_test), RigeModel.score(x_train_pr, y_train)
    pbar.set_postfix({"Test Score": test_score, "Train Score": train_score})
    Rsqu_test.append(test_score)
    Rsqu_train.append(train_score)

#Plot the R^2 values for training and testing sets with respect to the value of alpha
plt.figure(figsize=(10, 6))  
plt.plot(Alpha, Rsqu_test, label='validation data')
plt.plot(Alpha, Rsqu_train, 'r', label='training Data')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.ylim(0, 1)
plt.legend()

#Task 4: Grid Search
#Using the raw data and the same set of features as used above, use GridSearchCV to identify the value of alpha for which the model performs best. Assume the set of alpha values to be used as {0.0001, 0.001, 0.01, 0.1, 1, 10}
parameters1= [{'alpha': [0.0001,0.001,0.01, 0.1, 1, 10]}]  #should be inside the list
#Create a Ridge instance and run Grid Search using a 4 fold cross validation.
RR=Ridge()
Grid1 = GridSearchCV(RR, parameters1,cv=4)
Grid1.fit(x_train[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS', 'GPU', 'Category']], y_train)

#Print the R^2 score for the test data using the estimator that uses the derived optimum value of alpha.
BestRR=Grid1.best_estimator_
print(BestRR.score(x_test[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core','OS','GPU','Category']], y_test))  #0.3009905048691819

BestRR=Grid1.best_estimator_
print(BestRR.score(x_test[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core','OS','GPU','Category']], y_test))









