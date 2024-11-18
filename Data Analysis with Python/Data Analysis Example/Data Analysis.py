#Data Analysis

#1. The column ConvertedComp contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
#This assumes 12 working months and 50 working weeks.
#Plot the distribution curve for the column ConvertedComp

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#way1: use histplot
plt.figure(figsize=(12, 6))
sns.histplot(df['ConvertedComp'].dropna(), kde=True)
plt.title('Distribution of Annual Salaries (USD)')
plt.xlabel('Converted Compensation (USD)')
plt.ylabel('Frequency')
plt.show()

#way2: use distplot: distplot is is a deprecated function
plt.figure(figsize=(12, 6))
sns.distplot(df['ConvertedComp'].dropna(), kde=True, bins=50)
plt.title('Distribution of Annual Salaries (USD)')
plt.xlabel('Converted Compensation (USD)')
plt.ylabel('Density')
plt.show()

#2. Plot the histogram for the column ConvertedComp
plt.figure(figsize=(12, 6))
plt.hist(df['ConvertedComp'].dropna(), bins=50, edgecolor='black')
plt.title('Histogram of Annual Salaries (USD)')
plt.xlabel('Converted Compensation (USD)')
plt.ylabel('Frequency')
plt.show()

#3.Give the five number summary for the column Age
plt.figure(figsize=(12, 6))
plt.hist(df['Age'].dropna(), bins=50, edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#4.Find out if outliers exist in the column ConvertedComp using a box plot
plt.figure(figsize=(12, 6))
plt.boxplot(df['ConvertedComp'].dropna())
plt.title('Box Plot of Annual Salaries (USD)')
plt.ylabel('Converted Compensation (USD)')
plt.show()

#Find out the Inter Quartile Range for the column ConvertedComp
Q1 = df['ConvertedComp'].dropna().quantile(0.25)
Q3 = df['ConvertedComp'].dropna().quantile(0.75)
IQR = Q3-Q1
#Find out the upper and lower bounds.
min_value = Q1 - 1.5 * IQR
max_value = Q3 + 1.5 * IQR
print(min_value, max_value)


#5. Identify how many outliers are there in the ConvertedComp column
converted_comp = df['ConvertedComp'].dropna()
outliers = converted_comp[(converted_comp < min_value) | (converted_comp > max_value)]
# Count the number of outliers
num_outliers = len(outliers)
print(num_outliers)

#6. Create a new dataframe by removing the outliers from the ConvertedComp column
def remove_outliers(df, column):
    return df[(df[column] >= min_value) & (df[column] <= max_value)]  #keep the data between min and max
# Create a new dataframe without outliers
df_no_outliers = remove_outliers(df, 'ConvertedComp')
print(df_no_outliers)


#7. corrolation
#Find the correlation between Age and all other numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])
# Calculate correlation with Age
age_correlations = numeric_df.corr()['Age'].sort_values(ascending=False)
# if we want to remove Age's correlation with itself
age_correlations = age_correlations.drop('Age')
print(age_correlations)


