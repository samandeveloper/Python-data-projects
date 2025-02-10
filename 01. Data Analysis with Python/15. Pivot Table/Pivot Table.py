#Pivot Charts
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl

##the database that we are using issqlite
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite

conn = sqlite3.connect("m4_survey_data.sqlite") # open a database connection
QUERY = """SELECT * FROM master"""
df = pd.read_sql(QUERY,conn)


#1. Distribution of Respondents by Career Satisfaction and Job Satisfaction
#aggfunc='count': This is the aggregation function to apply. 'count' means it will count the number of respondents for each combination of CareerSat and JobSat.
#fill_value=0: This fills any empty cells (NaN values) in the resulting pivot table with 0.
pivot_table = pd.pivot_table(df, index='CareerSat', columns='JobSat', values='Respondent', aggfunc='count', fill_value=0)
# Plotting heatmap using pivot table
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, cmap='Blues', fmt='g')  #create heatmap using seaborn
plt.title('Career Satisfaction vs. Job Satisfaction')
plt.xlabel('Job Satisfaction')
plt.ylabel('Career Satisfaction')
plt.show()


#2. Comparison of Open Source Adoption Across Operating Systems
pivot_table = pd.pivot_table(df, index='OpSys', columns='OpenSource', values='Respondent', aggfunc='count', fill_value=0)
# Plotting
pivot_table.plot(kind='bar', figsize=(12, 6))
plt.title('Open Source Adoption Across Operating Systems')
plt.xlabel('Operating System')
plt.ylabel('Number of Respondents')
plt.legend(title='Comparison with Closed Source')
plt.xticks(rotation=0)  # displayed legend horizontally
plt.show()



#3. Job Satisfaction and Career Aspirations by Employment Status
pivot_table = pd.pivot_table(df, index='Employment', columns='MgrWant', values='Respondent', aggfunc='count', fill_value=0)
# Plotting
pivot_table.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Career Aspirations by Employment Status')
plt.xlabel('Employment Status')
plt.ylabel('Number of Respondents')
plt.legend(title='Desire to be a Manager')
plt.xticks(rotation=0)
plt.show()


#save the dataframe results in the Excel file
df.to_excel('./data.xlsx', index=False)