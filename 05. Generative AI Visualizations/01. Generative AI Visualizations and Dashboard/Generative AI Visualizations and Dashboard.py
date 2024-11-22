import pandas as pd
import numpy as np
import plotly.express as px
import plotly.offline as pyo

URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-AI0272EN-SkillsNetwork/labs/dataset/2016.csv"
df = pd.read_csv(URL, header=0)  # means this table has heading (optional no difference)
df.head()
df.info()

#convert the wrong data types in the dataframe to the correct one
df['Upper Confidence Interval'] = pd.to_numeric(df['Upper Confidence Interval'], errors='coerce')  #object to float # or df['Upper Confidence Interval']=df['Upper Confidence Interval'].astype(float)
df['Economy (GDP per Capita)']= pd.to_numeric(df['Economy (GDP per Capita)'], errors='coerce') #object to float
df['Health (Life Expectancy)']= pd.to_numeric(df['Health (Life Expectancy)'], errors='coerce') #object to float
df['Freedom']= pd.to_numeric(df['Freedom'], errors='coerce') #object to float
df['Region']= df['Region'].str.strip() #remove the white spaces before and after in this column (not between)
df['Country']= df['Country'].str.strip() #remove the white spaces before and after in this column (not between)

#replace the NAN columns with empty in all the columns in the dataframe
df.replace('', np.nan, inplace=True)# this is a old method : df['Country'].replace('', np.nan, inplace=True)

#find the columns with missing values then fill the missing values with mean of that column
columns_with_missing = df.columns[df.isnull().any()].tolist()  #find the columns that has missing values
print("Columns with missing values:", columns_with_missing)   #answer: ['Lower Confidence Interval','Upper Confidence Interval', 'Economy (GDP per Capita)', 'Health (Life Expectancy)', 'Freedom']

mean_value_Lower_Confidence_Interval = df['Lower Confidence Interval'] = df['Lower Confidence Interval'].mean() #replace missing values in the above columns with the mean
df.fillna(mean_value_Lower_Confidence_Interval, inplace=True)  # to add inplace=true   #old method:df['Lower Confidence Interval'].fillna(mean_value1, inplace=True) 

mean_value_Upper_Confidence_Interval = df['Upper Confidence Interval'] = df['Upper Confidence Interval'].mean()
df.fillna(mean_value_Upper_Confidence_Interval, inplace=True)  #old method: df['Upper Confidence Interval'].fillna(mean_value2, inplace=True)

mean_value_Upper_Confidence_Interval = df['Upper Confidence Interval'] = df['Upper Confidence Interval'].mean()
df.fillna(mean_value_Upper_Confidence_Interval, inplace=True)  #old method: df['Upper Confidence Interval'].fillna(mean_value2, inplace=True)

mean_value_Economy = df['Economy (GDP per Capita)'] = df['Economy (GDP per Capita)'].mean()
df.fillna(mean_value_Economy, inplace=True)

mean_value_Health = df['Health (Life Expectancy)'] = df['Health (Life Expectancy)'].mean()
df.fillna(mean_value_Health, inplace=True)

mean_value_Freedom = df['Freedom'] = df['Freedom'].mean()
df.fillna(mean_value_Freedom, inplace=True)


#Generate SQL query to Count the number of rows for each country
count_each_country = df['Country'] = df['Country'].value_counts() 
print(count_each_country)

#Section2: create visulizations:

#Question: Write a python code that identifies the GDP per capita and Healthy Life Expectancy of the top 10 countries and create a bar chart named fig1 to show the GDP per capita and Healthy Life Expectancy of these top 10 countries using plotly.
top_10_GDP_countries = df.sort_values('Economy (GDP per Capita)', ascending=False).head(10)   #or top_10_countries = df.nlargest(10, ['Economy (GDP per Capita)', 'Health (Life Expectancy)'])
print(top_10_GDP_countries)

fig1 = px.bar(top_10_GDP_countries, x='Country', y=['Economy (GDP per Capita)', 'Health (Life Expectancy)'],   #we have 2 y axias
              title='Top 10 Countries: GDP per Capita and Healthy Life Expectancy',
              labels={'value': 'Value', 'variable': 'Indicator', 'Country': 'Country'},
              barmode='group')

fig1.show()

# Question:Find the correlation between the Economy (GDP per Capita), Family, Health (Life Expectancy), Freedom, Trust (Government Corruption), Generosity and Happiness score. You may like to represent the correlation as a heatmap of a readable, visually appealing size.
# 1. Create a sub-dataset including Economy (GDP per Capita), Family, Health (Life Expectancy), Freedom, Trust (Government Corruption), Generosity, and Happiness Score attributes from the dataframe (df).
attributes = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 'Freedom', 'Trust (Government Corruption)', 'Generosity', 'Happiness Score']
sub_dataset = df[attributes]
print(sub_dataset)
sub_dataset.info()

#conver data type to the suitable datatype in sub_dataset dataframe
sub_dataset['Freedom'] = sub_dataset['Freedom'].str.strip()
sub_dataset['Freedom']= pd.to_numeric(sub_dataset['Freedom'], errors='coerce') #object to float

sub_dataset['Health (Life Expectancy)'] = sub_dataset['Health (Life Expectancy)'].str.strip()
sub_dataset['Health (Life Expectancy)']= pd.to_numeric(sub_dataset['Health (Life Expectancy)'], errors='coerce') #object to float

sub_dataset['Economy (GDP per Capita)'] = sub_dataset['Economy (GDP per Capita)'].str.strip()
sub_dataset['Economy (GDP per Capita)']= pd.to_numeric(sub_dataset['Economy (GDP per Capita)'], errors='coerce') #object to float

# Calculate the correlation matrix (to plot the heatmap using plotly express we need to first define the corrolation between sub_dataset dataframe)
correlation_matrix = sub_dataset.corr()

# Create a heatmap using Plotly
fig2 = px.imshow(correlation_matrix, title='Correlation Heatmap of Subdataset', width=800, height=600)

fig2.show()

#Question: go back to the main df: Create a scatter plot to identify the effect of GDP per Capita on Happiness Score in various Regions. Use plotly for creating the plot.
#Write a code that creates a scatter plot named fig3 between Happiness Score and GDP per Capita attributes of a dataframe using Plotly. Use Region to color the data points on the scatter plot.
fig3 = px.scatter(df, x='Economy (GDP per Capita)', y='Health (Life Expectancy)', color='Region', title='Scatter Plot of Happiness Score vs GDP per Capita by Region')  #note: color='Region'
fig3.show()


#Question:Write a Plotly code that creates a pie chart named fig4 to present Happiness Score by Region attributes of dataframe df.
fig4 = px.pie(df, values='Health (Life Expectancy)', names='Region',  title='Pie Chart of Happiness Score by Region')  #values and names (not value and name) 
fig4.show()


#Question:#Write a Plotly code that creates a map named fig5 to display GDP per capita of countries and include Healthy Life Expectancy to be shown as a tooltip.
fig5 = px.choropleth(df, locations="Country", locationmode="country names", color="Economy (GDP per Capita)",  #locationmode="country names"This mode is used when you want to map data to specific countries based on their names. 
                     hover_name="Country", hover_data={"Economy (GDP per Capita)": True, "Health (Life Expectancy)": True},
                     title='Map of GDP per Capita with Healthy Life Expectancy Tooltip')
fig5.show()


#Section3: Dashboarding and story telling:

#Question: Write Python code to write any four of the Plotly figures (fig1, fig2, fig3, fig4, fig5) to a single HTML file named “dashboard.html”?
import plotly.offline as pyo

# Assume fig1, fig2, fig3, and fig4 are the Plotly figures you want to include in the dashboard

fig1.update_layout(title_text="Figure 1")
fig2.update_layout(title_text="Figure 2")
fig3.update_layout(title_text="Figure 3")
fig4.update_layout(title_text="Figure 4")

# Create a list of the figures you want to include in the dashboard
figures = [fig1, fig2, fig3, fig4]

# Write the figures to an HTML file
pyo.plot(figures, filename='dashboard.html')

# Create a new HTML file and add some of our visualizations like a dashboard in it
with open('dashboard.html', 'w') as f:
    # Write each figure to the HTML file
    f.write('<html><head><title>World Happiness Dashboard</title></head><body><h1>Test</h1></body></html>')
    f.write(pyo.plot(fig1, include_plotlyjs='cdn', output_type='div'))
    f.write(pyo.plot(fig2, include_plotlyjs='cdn', output_type='div'))
    f.write(pyo.plot(fig3, include_plotlyjs='cdn', output_type='div'))
    f.write(pyo.plot(fig4, include_plotlyjs='cdn', output_type='div'))
    f.write('</body></html>')  #optional
fig1.show()
fig2.show()
fig3.show()
fig4.show()
