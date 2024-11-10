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
