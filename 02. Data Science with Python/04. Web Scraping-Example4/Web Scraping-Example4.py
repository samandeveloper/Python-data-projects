#Web Scraping 2

import requests
from bs4 import BeautifulSoup
#your code goes here
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
data = requests.get(url).text  #must specify we are collecting text here
soup = BeautifulSoup(data,"html.parser")

table = soup.find('table')  #we only have one table here so we use find method instead of find_all
#print(table)
td = table.find_all('td')
#print(td)
tr = table.find_all('tr')
#print(tr)

for rows in tr:  
    cols = rows.find_all('td')
    #print(cols)
    languages = cols[1].getText()
    average_annual_salary = cols[3].getText()
    print(average_annual_salary)
#answer:
# Average Annual Salary
# $114,383
# $101,013
# $92,037
# $110,981
# $130,801
# $113,865
# $88,726
# $84,727
# $84,793
# $94,082

#Save the scrapped data into a file named popular-languages.csv
#way1
import csv
# Open a new CSV file to write the data
with open('language_salaries.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)  #csv.writer(filename)
    # Write the header row
    csvwriter.writerow(['Language', 'Average Annual Salary'])  #previous variable name.writerow(['column1 name', 'column 2 name'])
    # Write the data to the CSV file
    csvwriter.writerow([languages, average_annual_salary])   #previous variable name.writerow([column1, column2])



#way2: 
# Create empty lists to store the data
languages_list = []
salaries_list = []

for rows in tr:  # or for row in find_all('tr')
    cols = rows.find_all('td')
    languages = cols[1].getText()
    average_annual_salary = cols[3].getText()   
    # Append data to lists
    languages_list.append(languages)
    salaries_list.append(average_annual_salary)

# Create a DataFrame
df = pd.DataFrame({
    'Language': languages_list,
    'Average Annual Salary': salaries_list
})

# Write the DataFrame to a CSV file
df.to_csv('language_salaries.csv', index=False)

print("Data has been written to language_salaries.csv")