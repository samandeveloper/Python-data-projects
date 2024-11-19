#Matplotlib and Line Plots

import pandas as pd 

df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
df_can.head()
df_can.set_index('Country', inplace=True) #set the 'Country' column as an index
years = list(map(str, range(1980, 2014)))  #convert the years column to string  #years = list(range(1980, 2014)) doesn't convert to string

#Visualizing Data using Matplotlib
#if you want to use matplotlib in Jupyternotebook use %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

#create line plot
#Plot a line graph of immigration from Haiti using df.plot() >> df.plot() and df.plot(kind='line') both create line plot
#1. extract the data series for Haiti.

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column (years is string)
haiti.head()

haiti.plot(kind='line')  #or use .plot.line()
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show() 

#now add text inside the line plot
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
# annotate the 2010 Earthquake. 
plt.text(2000, 6000, '2010 Earthquake') # # syntax: plt.text(x location, y location, label)
plt.show() 

#2. compare the number of immigrants from India and China from 1980 to 2013.
#Get the data set for China and India, and display the dataframe.
df_CI =df_can.loc[['India','China'], years]  #years are column from 1980 - 2013
df_CI
#now create a line plot for df_CI
df_CI.plot(kind='line')
#to make the plot more readable we need to pivot it
df_CI = df_CI.transpose() #change the column and row of the df_CI
df_CI.head()

#3. Compare the trend of top 5 countries that contributed the most to immigration to Canada.
df_can.sort_values(by='Total', ascending= False, axis=0, inplace=True)
df_top5 = df_can.head()
#df_top5
df_top5 = df_top5[years].transpose()
print(df_top5)
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()


