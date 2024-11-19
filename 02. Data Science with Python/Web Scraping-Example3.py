#Extracting Stock Data Using a Web Scraping

#import necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#way1: Extracting data using requests.get()
#Step 1: Send an HTTP request to the web page
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
data  = requests.get(url).text  #get html using .text

#Step 2: Parse the HTML content
soup = BeautifulSoup(data, 'html.parser')

#Step 3: Identify the HTML tags
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])  #add column names

#Step 4: Use a BeautifulSoup method for extracting data
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)    

#Step 5: Print the extracted data
netflix_data.head()

#way2: Extracting data using pandas library
read_html_pandas_data = pd.read_html(url)
netflix_dataframe = read_html_pandas_data[0]  #there is only one table in this url so we use index0 to find this table

#content of the title attribute
title = soup.find_all("title")
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])  #column names

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    print(col[0])

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = pd.concat([amazon_data, pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

    
