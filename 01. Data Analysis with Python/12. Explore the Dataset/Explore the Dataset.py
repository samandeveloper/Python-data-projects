#Explore the Dataset

import pandas as pd
dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"
df = pd.read_csv(dataset_url)   #read_csv will automatically generates a new dataframe
df.head()

#Find out the number of rows and columns
num_rows = len(df)
print(num_rows)  #answer:11552

#Print the number of columns in the dataset.
num_columns = len(df.columns)
print(num_columns)   #answer:85

#other way to find out rows and columns
shape_rows = df.shape[0]  #shape[0] shows number of rows
shape_columns = df.shape[1]  #shape[1] shows number of columns
# Get the shape of the DataFrame (show both number of rows and columns)
shape = df.shape


df.info() #check all of the columns datatype

#Print the mean age of the survey participants.
mean_age = df.Age.mean()  #or df['Age'].mean()
print(mean_age)  # 30.77239449133718

#. Print how many unique countries are there in the Country column.
unique_countries= df['Country'].value_counts()  #or use unique_countries= df['Country'].unique() but not counting, it will show a list (array) of unique country names
print(unique_countries)

