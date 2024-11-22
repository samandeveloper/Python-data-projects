#Create & Access SQLite database using Python

#1. Create database using SQLite
#!pip install sqlite3   #first install the sqlite3
import sqlite3
conn = sqlite3.connect('INSTRUCTOR.db') #connect to the INSTRUCTOR.db
cursor_obj = conn.cursor()


#2. Create a table in the database
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")  #Drop the table if already exist
# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
cursor_obj.execute(table)
print("Table is Ready")


#3. Insert data into the table 
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


#4. Query data in the table
#In this step we will retrieve data we inserted into the INSTRUCTOR table.
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)

### Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)


# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)


#write and execute an update statement that changes the Rav's CITY to MOOSETOWN
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)


#5. Retrieve data into Pandas
import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)
#print the dataframe
df
#print just the LNAME for first row in the pandas data frame
df.LNAME[0]

#6. Close the Connection
conn.close()
