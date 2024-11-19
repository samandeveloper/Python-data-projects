#Exploratory Data Analysis
import pandas as pd
import numpy as np
import piplite
await piplite.install('seaborn')

filepath='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(filepath, header=None)

#Analyzing Individual Feature Patterns Using Visualization
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline 

#1. Find the correlation between the following columns: bore, stroke, compression-ratio, and horsepower.
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

#1. Continuous Numerical Variables:

#Positive Linear Relationship
# Engine size as potential predictor variable of price
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)
df[["engine-size", "price"]].corr()
sns.regplot(x="highway-mpg", y="price", data=df)
df[['highway-mpg', 'price']].corr()

#Weak Linear Relationship
sns.regplot(x="peak-rpm", y="price", data=df)
df[['peak-rpm','price']].corr()

#Find the correlation between x="stroke" and y="price"
df[["stroke","price"]].corr()

#Given the correlation results between "price" and "stroke"
sns.regplot(x="stroke", y="price", data=df)

#2. Categorical Variables
# relationship between "body-style" and "price"
sns.boxplot(x="body-style", y="price", data=df)    #"body-style" and "price"
sns.boxplot(x="engine-location", y="price", data=df)  # "engine-location" and "price"
sns.boxplot(x="drive-wheels", y="price", data=df)  # "drive-wheels" and "price"

#3. Descriptive Statistical Analysis
#Value Counts: the method "value_counts" only works on pandas series, not pandas dataframes. 
# As a result, we only include one bracket df['drive-wheels'], not two brackets df[['drive-wheels']]
df['drive-wheels'].value_counts()
#now we can convert series to dataframe
df['drive-wheels'].value_counts().to_frame()

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.reset_index(inplace=True)
drive_wheels_counts=drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'})
drive_wheels_counts

# rename the index to 'drive-wheels'
drive_wheels_counts.index.name = 'drive-wheels'


#4. Basics of Grouping
df['drive-wheels'].unique()
df_group_one = df[['drive-wheels','body-style','price']]
# grouping results
df_grouped = df_group_one.groupby(['drive-wheels'], as_index=False).agg({'price': 'mean'})


# grouping results (groupby is a dataframe method)
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()

grouped_pivot = grouped_test1.pivot(index='drive-wheels',columns='body-style')

grouped_pivot = grouped_pivot.fillna(0) #fill missing values with 0

#Use the "groupby" function to find the average "price" of each car based on "body-style"
df_gptest2 = df[['body-style','price']]
grouped_test_bodystyle = df_gptest2.groupby(['body-style'],as_index= False).mean()


#create a heat map to visualize the relationship between Body Style vs Price.
import matplotlib.pyplot as plt
%matplotlib inline 
#use the grouped results
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


#to create more details plot
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()

#way1: calculate pearson coefficient using df.corr()
#Correlation and Causation
#Pearson Correlation is the default method of the function "corr" (we are just working with dataframe and p-value is not important to us)
#near -1 strong negative corrolation. near +1 is the strong positive corrolation. near 0 is the weak corrolation.
df.corr()  #corr() is th emethod on dataframe in pandas and gives us just coefficient

#P-value: The P-value is the probability value that the correlation between these two variables is statistically significant.
#P-value<  0.001: we say there is strong evidence that the correlation is significant.
# P-value:< 0.05: there is moderate evidence that the correlation is significant.
#P-value:< 0.1: there is weak evidence that the correlation is significant.
#P-value:>  0.1: there is no evidence that the correlation is significant.

#way2: calculate coefficient and p_value in pearson corrolation using scipy library (stats.pearsonr(df[column1],df[column2],...)) 
#We can obtain this information using "stats" module in the "scipy" library.
#now we want to work on both series and dataframe
from scipy import stats
# calculate the Pearson Correlation Coefficient and P-value of 'wheel-base' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)  # p-value is 0.001, the correlation between wheel-base and price is statistically significant, although the linear relationship isn't extremely strong (~0.585).

#calculate the Pearson Correlation Coefficient and P-value of 'horsepower' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  #p-value is 0.001, the correlation between horsepower and price is statistically significant, and the linear relationship is quite strong (~0.809, close to 1).

#calculate the Pearson Correlation Coefficient and P-value of 'length' and 'price'.
pearson_coef, p_value = stats.pearsonr(df['length'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value)  #the p-value is 0.001, the correlation between length and price is statistically significant, and the linear relationship is moderately strong (~0.691).



