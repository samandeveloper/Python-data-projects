#Extracting and Visualizing Stock Data

#install necessary packages:
#!pip install yfinance
#!pip install bs4
#!pip install nbformat

#import necessary packages
import yfinance as yf  #yahoo finance
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#below function 
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

#1. Use yfinance to Extract Stock Data
#Use yfinance to Extract Stock Data
tesla = yf.Ticker('TSLA')

#Use function 'history' to extract information from tesla
tesla_data = tesla.history(period="max")

#Reset the index using the reset_index(inplace=True) function on the tesla_data DataFrame (add index from 0)
tesla_data.reset_index(inplace=True)
tesla_data.head()


#2. Use Webscraping to Extract Tesla Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

# Initialize an empty list to collect data
data = []
# Assuming 'soup' is already defined as the BeautifulSoup object containing your HTML
for table in soup.find_all('table'):  # Find all the tables in the soup
    if table.find('th').getText().startswith("Tesla Quarterly Revenue"):  # Check for specific table
        for row in table.find("tbody").find_all("tr"):  # Find all rows in the tbody
            col = row.find_all("td")  # Find all columns in the row
            
            if len(col) < 2:  # Skip if there are not enough columns
                continue
            
            Date = col[0].text.strip()
            Revenue = col[1].text.replace("$", "").replace(",", "").strip()
            
            # Append a dictionary of the row to the data list
            data.append({"Date": Date, "Revenue": Revenue})

# Convert the list of dictionaries to a DataFrame
tesla_revenue = pd.DataFrame(data)

print(tesla_revenue)

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"", regex=True)
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


#3. Use yfinance to Extract Stock Data
gme = yf.Ticker('GME')
gme_data = gme.history(period = "max")
gme_data.reset_index(inplace=True)
gme_data.head()


#4. Use Webscraping to Extract GME Revenue Data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url).text  #.text method to see the html of the url

soup = BeautifulSoup(html_data_2, 'html.parser')  #use html.parser or html5lib

gme_revenue = pd.DataFrame(columns = ["Date","Revenue"])
data = []
for table in soup.find_all('table'):
    for row in table.find("tbody").find_all("tr"):
        col = row.find_all("td")
        # Check if the row has enough columns
        if len(col) < 2:
            continue  # Skip this row if it doesn't have at least 2 columns
            
        Date = col[0].text.strip()
        Revenue = col[1].text.replace("$", "").replace(",", "").strip()
               
        data.append({"Date": Date, "Revenue": Revenue})

gme_revenue = pd.DataFrame(data)

print(gme_revenue)



