#Collecting Job Data Using APIs
#Collect Jobs Data using GitHub Jobs API (Write a function to get the number of jobs for the Python technology.)
#The keys in the json are: Job Title, Job Experience Required, Key Skills, Role Category, Location, Functional Area, Industry, 
# Role
import pandas as pd
import json
import requests

api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
    
#your code goes here
response = requests.get(api_url)
print(response)
if response.status_code == 200:
    data = response.json()
   # print(data)
else: 
    print("no data")


def get_number_of_jobs_T(technology):
    
    #your code goes here
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
    #print(data)
    number_of_jobs = sum(1 for i in data if technology.lower() in i['Key Skills'].lower())  #if the name of "technology" is in the key skills
    return technology,number_of_jobs
#call the function
get_number_of_jobs_T("Python")  #('Python', 1173)


#Write a function to find number of jobs in US for a location of your choice
def get_number_of_jobs_L(location):
    #your coe goes here
    number_of_jobs = sum(1 for i in data if i['Location'].lower)
    return location,number_of_jobs
#call the function in Los Angeles
get_number_of_jobs_L('Los Angeles')  #answer:('Los Angeles', 27005)


#find the languages
languages=[ "C", "C#", "C++", "Java", "JavaScript", "Python", "Scala",
    "Oracle", "SQL Server", "MySQL", "PostgreSQL", "MongoDB"]
def count_jobs(languages):
    count = 0
    for job in data:
        if 'Key Skills' in job:
            skills = job['Key Skills'].lower()
            for language in languages:
                if language.lower() in skills:
                    count += 1
                    break  # Count the job only once even if multiple languages match
    return count


total_jobs = count_jobs(languages)
print(f"Total job postings with any of the specified languages: {total_jobs}")
