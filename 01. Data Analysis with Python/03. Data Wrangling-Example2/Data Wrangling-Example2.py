#Data Wrangling:
import pandas as pd
#read data
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")

#find duplicate rows exist in the dataframe
duplicates = df.duplicated().any()
print(duplicates)  #if true means we have duplicates in the dataframe

#remove duplicate rows
#inside drop_duplicates() we can have kepp = 'first' (default-drop everything except first one),'last' (drop everything except last one), 'False' (drop all duplicates)
remove_duplicates = df.drop_duplicates()

#find missing values:
#we can use isnull() or isna()
missing = df.isnull().any()

# rows are missing in the column 'WorkLoc'
missing_workloc = df['WorkLoc'].isnull().any() 

#Find the value counts for the column WorkLoc.
most_frequent = df['WorkLoc'].value_counts().idxmax()  #answer: Office

#replace all the empty rows in the column WorkLoc with the value that you have identified as majority.
replace_empty = df['WorkLoc'].fillna(most_frequent, inplace=True)


#Normalizing data
#List out the various categories in the column 'CompFreq'
count_compfreq=df['CompFreq'].value_counts()

#Create a new column named 'NormalizedAnnualCompensation'.
# Use the below logic to arrive at the values for the column NormalizedAnnualCompensation.
# If the CompFreq is Yearly then use the exising value in CompTotal
# If the CompFreq is Monthly then multiply the value in CompTotal with 12 (months in an year)
# If the CompFreq is Weekly then multiply the value in CompTotal with 52 (weeks in an year)
def normalize_compensation(row):
    if pd.isna(row['CompFreq']) or pd.isna(row['CompTotal']):
        return None
    elif row['CompFreq'] == 'Yearly':
        return row['CompTotal']
    elif row['CompFreq'] == 'Monthly':
        return row['CompTotal'] * 12
    elif row['CompFreq'] == 'Weekly':
        return row['CompTotal'] * 52
    else:
        return None  

# Create the new column
df['NormalizedAnnualCompensation'] = df.apply(normalize_compensation, axis=1)   #axis=1 apply function on the rows
# Display the first few rows to verify
print(df[['CompFreq', 'CompTotal', 'NormalizedAnnualCompensation']].head())