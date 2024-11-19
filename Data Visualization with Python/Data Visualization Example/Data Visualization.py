# Data Visualization
#since we are working with sqlite database we will use sqlite3
##SQLite3 is not typically used to connect to remote databases or APIs. SQLite3 is a lightweight, file-based database engine that is embedded directly into applications. 

import pandas as pd
#Download database file.
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite

import sqlite3
conn = sqlite3.connect("m4_survey_data.sqlite") # open a database connection

#in this database file we have different tables (in the query below we check list of all tables)
QUERY = """
SELECT name as Table_Name FROM
sqlite_master WHERE
type = 'table'
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
pd.read_sql_query(QUERY,conn)


# count everything in the master table
QUERY = """
SELECT COUNT(*)
FROM master
"""
import sqlite3
conn = sqlite3.connect('m4_survey_data.sqlite')
cur = conn.cursor()
cur.execute(QUERY)
result = cur.fetchone()
print(result[0])
df_count = pd.read_sql_query(QUERY,conn)



#create a new dataframe for counting each Age
QUERY = """
SELECT Age,COUNT(*) as count
FROM master
group by age
order by age
"""
df_age = pd.read_sql_query(QUERY,conn)


#check datatypes of all columns in the master table
QUERY = """
SELECT sql FROM sqlite_master
WHERE name= '{}'
""".format(table_name)

df = pd.read_sql_query(QUERY,conn)
print(df.iat[0,0]) 


#1. Plot a histogram of ConvertedComp column in the master table
import matplotlib.pyplot as plt
import seaborn as sns
# Query to select ConvertedComp column
query = "SELECT ConvertedComp FROM master"  #table name is master
# Read the query result into a pandas DataFrame
df = pd.read_sql_query(query, conn)
# Create the histogram using seaborn
plt.figure(figsize=(12, 6))
plt.hist(df['ConvertedComp'], bins=50, edgecolor='black')
plt.title('Histogram plot')
plt.xlabel('ConvertedComp')
plt.show()

#2. create distribution plot
sns.distplot(df['ConvertedComp'].dropna().astype(int)) 
plt.show()


#3. box plot for Age column in master table
query = "SELECT Age FROM master"  #table name is master
# Read the query result into a pandas DataFrame
df = pd.read_sql_query(query, conn)
plt.figure(figsize=(12, 6))
plt.boxplot(df['Age'].dropna().astype(int))  # we need to drop the na values and change the typr of age from object to integer
plt.title('Box Plot for Age')
plt.ylabel('Age')
plt.show()


#4. Create a bubble plot of WorkWeekHrs and CodeRevHrs, use Age column as bubble size.
Query = '''
select age,workweekhrs,CodeRevHrs from master
'''
#conn = sqlite3.connect('m4_survey_data.sqlite')
df = pd.read_sql_query(Query,conn)
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='WorkWeekHrs', y='CodeRevHrs', size='Age', sizes=(20, 500), legend='brief')
plt.show()


#5. Pie plot
Query ='''select * from  DatabaseDesireNextYear'''  #DatabaseDesireNextYear table has two columns(Respondent,DatabaseDesireNextYear)
df = pd.read_sql_query(Query,conn)
Query ='''SELECT DatabaseDesireNextYear, COUNT(*) as Count
FROM DatabaseDesireNextYear
GROUP BY DatabaseDesireNextYear  
ORDER BY Count DESC
LIMIT 5
'''  #DatabaseDesireNextYear table has two columns(Respondent,DatabaseDesireNextYear)
df = pd.read_sql_query(Query,conn)


#6. Stacked chart:Create a stacked chart of median WorkWeekHrs and CodeRevHrs for the age group 30 to 35.:
Query ='''select 
Age,
    WorkWeekHrs,
    CodeRevHrs
from  master
WHERE Age BETWEEN 30 AND 35
group by age
order by age
'''  
df = pd.read_sql_query(Query,conn)
#median_data = df.groupby('Age')['WorkWeekHrs'].median().reset_index()
median_data = df.groupby('Age').agg(
    MedianWorkWeekHrs=('WorkWeekHrs', 'median'),
    MedianCodeRevHrs=('CodeRevHrs', 'median')
).reset_index()
median_data.head()


# 7. Create the bars for Median Work Week Hours
plt.bar(median_data['Age'], median_data['MedianWorkWeekHrs'], 
        label='Median Work Week Hours', color='skyblue', width=0.4, align='center')

plt.bar(median_data['Age'] + 0.4, median_data['MedianCodeRevHrs'], 
        label='Median Code Review Hours', color='lightgreen', width=0.4, align='center')
plt.title('Stacked chart of median WorkWeekHrs and CodeRevHrs for the age group 30 to 35')
plt.show()


#8. Plot the median ConvertedComp for all ages from 45 to 60
Query = '''
select Age, ConvertedComp from master WHERE Age BETWEEN 45 AND 60  
'''
df = pd.read_sql_query(Query,conn)
median_data = df.groupby('Age')['ConvertedComp'].median().reset_index()

# Sort the data by Age to ensure proper line plot
plt.figure(figsize=(12, 6))
median_data = median_data.sort_values('Age')
#print(median_data)
plt.plot(median_data['Age'], median_data['ConvertedComp'], marker='o')

# Customize the plot
plt.title('Median ConvertedComp by Age (45-60)', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Median ConvertedComp', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


#9. Create a horizontal bar chart using column MainBranch.
Query = '''
select MainBranch, Count(*) as Count from master
group by
MainBranch
ORDER BY Count DESC
'''
df =pd.read_sql_query(Query,conn)
# Create the horizontal bar chart (plt.barh)
plt.figure(figsize=(12, 8))
bars = plt.barh(df['MainBranch'], df['Count'])
plt.title('Horizontal bar chart using column MainBranch')
plt.show()







