#Analyzing a real world data-set with SQL and Python

#Connect to the database
%load_ext sql
import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()

#%sql sqlite:///socioeconomic.db  #The syntax for connecting to magic sql using sqllite is to write sql in python

#Store the dataset in a Table
import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")
%sql SELECT * FROM chicago_socioeconomic_data limit 5; 


#How many rows are in the dataset?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;  #78

#How many community areas in Chicago have a hardship index greater than 50.0?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;  #38

#What is the maximum value of hardship index in this dataset?
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;  #98

#Which community area which has the highest hardship index?
%sql SELECT community_area_name FROM chicago_socioeconomic_data where hardship_index=98.0;  #'Riverdale'

#Which Chicago community areas have per-capita incomes greater than $60,000?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;  # Lake View,Lincoln Park, Near North Side, Loop

#Create a scatter plot using the variables per_capita_income_ and hardship_index.
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())






