# pre-processing a dataset using Pandas
# Dataset we use here is "Immigration to Canada from 1980 to 2013"

#import neccessary library
import numpy as np  
import pandas as pd 

#read the excel file
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

df_can.head() #show the top 5 rows
df_can.tail() #show the last 5 rows
df_can.info(verbose=False)  #show the summary of dataframe
df_can.columns # show the list of column header
df_can.index  #get the list of indices we use the .index instance variables
df_can.columns.tolist()  #to see the column names as a list
df_can.shape #show the dimensions of the dataframe

#use .drop() method to remove some unnecessary columns
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)  #axis=1 means column
df_can.head(2)  #show the first two rows of the dataframe

#change the name of some headings in the columns (use .rename() method)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)  #example:OdName of the heading column become Country
df_can.columns

#summing up all the values in each row 
df_can['Total'] = df_can.sum(axis=1)  #axis=1 means summing up all the values horizontally (eachrow)
df_can['Total']

#show how many null objects
df_can.isnull().sum()  

#summary of each column
df_can.describe()

#Indexing and Selection (slicing)

#Filter Columns:
#way1. df.column_name 
#way2. df['column']   # returns series  or  df[['column 1', 'column 2']]  # returns dataframe

df_can.Country  #returns a list of Countries

#list of countryies and the data for years: 1980 - 1985
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]

#Filter Rows:
#way1. df.loc[label]   # filters by the labels of the index/column
#way2. df.iloc[index]  # filters by the positions of the index/column

# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.set_index('Country', inplace=True)
df_can.head(3)

#to remove the name of the index
df_can.index.name = None

#to see the Japan row
df_can[df_can.index == 'Japan']

#value of the Japan in 2013
df_can.loc['Japan', 2013]  #or df_can.iloc[87, 36]

#values for Japan in 1980, 1981, 1982, 1983, 1984, and 1984]
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]   #or  df_can.iloc[87, [3, 4, 5, 6, 7, 8]]  Japan is in row 87 and column 3 is 1980 and column 4 is 1981,...

# converting the names of all the columns in the DataFrame df_can to strings.
df_can.columns = list(map(str, df_can.columns))

#Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years
years = list(map(str, range(1980, 2014)))
years

#show the data on Asian countries
condition = df_can['Continent'] == 'Asia'
print(condition)
df_can[condition]  #show it in the dataframe

# filter for AreaNAme = Asia and RegName = Southern Asia
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]


#Sorting Values of a Dataframe or Series
#You can use the sort_values() function is used to sort a DataFrame or a Series based on one or more columns.
#syntax: df.sort_values(col_name, axis=0, ascending=True, inplace=False, ignore_index=False)
#s sort out dataframe df_can on 'Total' column, in descending order to find out the top 5 countries that contributed the most to immigration to Canada
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)  #it means sorting the rows based on the values in the 'Total' column
top_5 = df_can.head(5)
top_5


#Find out top 3 countries that contributes the most to immigration to Canda in the year 2010.
df_can.sort_values(by='2010', ascending=False, axis=0, inplace=True)
top3_2010 = df_can['2010'].head(3)
top3_2010


















