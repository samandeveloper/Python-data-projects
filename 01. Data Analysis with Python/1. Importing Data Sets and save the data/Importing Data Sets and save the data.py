# Importing Data Sets and save the dataset- Used Cars Pricing
import pandas as pd
import numpy as np

#read a below dataset
filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(filepath, header=None)
df.head(5)

#Add Headers
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
df.columns = headers  #replace headers

#clean data
df1=df.replace('?',np.NaN) 
df=df1.dropna(subset=["price"], axis=0) #drop missing values in the column "price"

#save the dataset into csv file
df.to_csv("automobile.csv", index=False)