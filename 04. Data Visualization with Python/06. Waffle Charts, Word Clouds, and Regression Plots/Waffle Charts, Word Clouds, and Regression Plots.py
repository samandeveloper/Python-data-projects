# Waffle Charts, Word Clouds, and Regression Plots

# Step1: Import and setup matplotlib:
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches  # needed for waffle Charts
import numpy as np  
import pandas as pd 
from PIL import Image  # converting images into arrays
import seaborn as sns
import wordcloud  # for creating wordcloud visualization


# Step2: Fetching Data
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
df_can.head()

# Step3: Data prepration
df_can.set_index('Country', inplace=True)  #set country column as an index

# step4: Create visualizations:

# a. Waffle Charts:
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]  # create a new dataframe using 'Denmark', 'Norway', and 'Sweden'  # : means select all the columns in the dataframe

# create waffle chart
# to cteate a waffle chart we need pywaffle python package
#!pip install pywaffle
from pywaffle import Waffle

#Set up the Waffle chart figure
fig = plt.figure(FigureClass = Waffle,
                 rows = 20, columns = 30, #pass the number of rows and columns for the waffle 
                 values = df_dsn['Total'], #pass the data to be used for display
                 cmap_name = 'tab20', #color scheme
                 legend = {'labels': [f"{k} ({v})" for k, v in zip(df_dsn.index.values,df_dsn.Total)],
                            'loc': 'lower left', 'bbox_to_anchor':(0,-0.1),'ncol': 3}
                 #notice the use of list comprehension for creating labels 
                 #from index and total of the dataset
                )

plt.show()



# create the same waffle chart for China and India
data_CI = df_can.loc[['China', 'India'], :] 
data_CI
fig = plt.figure(FigureClass = Waffle,
    rows = 20,
    columns =30,
    values = data_CI['Total'],
    cmap_name = 'tab20', #color scheme,
    legend={'labels': [f"{k} ({v})" for k, v in zip(df_dsn.index.values,df_dsn.Total)],
                            'loc': 'lower left', 'bbox_to_anchor':(0,-0.1),'ncol': 3}
)
plt.show()


#b. Word Cloud:
from wordcloud import WordCloud, STOPWORDS
import urllib
# open the file and read it into a variable alice_novel
alice_novel = urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt').read().decode("utf-8")

stopwords = set(STOPWORDS)
# instantiate a word cloud object
alice_wc = WordCloud()
# generate the word cloud
alice_wc.generate(alice_novel)   #WordCloud().generate(text address)
#interpolation='bilinear': method used when resizing or rendering the image. Bilinear interpolation smooths the image by averaging the colors of the four nearest pixels. This can help create a visually pleasing effect when scaling the image.
plt.imshow(alice_wc, interpolation='bilinear')  #This function displays an image
plt.axis('off')  #This line removes the axis from the plot
plt.show()


#Make the above wordcloud more beautiful:
fig = plt.figure(figsize=(14, 18))
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()


# in the above wordcloud 'said' isn't really an informative word. So let's add it to our stopwords and re-generate the cloud
stopwords.add('said') # add the words said to stopwords (we can add a word even though it's already added)
# re-generate the word cloud
alice_wc.generate(alice_novel)
# display the cloud
fig = plt.figure(figsize=(14, 18))
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()


#show an image (mask) using wordcloud
#save mask to alice_mask
alice_mask = np.array(Image.open(urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/images/alice_mask.png')))

fig = plt.figure(figsize=(14, 18))
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()


#Shaping the word cloud according to the mask is straightforward using word_cloud package. For simplicity, we will continue using the first 2000 words in the novel.
alice_wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask, stopwords=stopwords)  #make the image background white
# generate the word cloud
alice_wc.generate(alice_novel)
# display the word cloud
fig = plt.figure(figsize=(14, 18))
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()


#calculate total immigration from 1980 to 2013 (set maximum words to 90)
total_immigration = df_can['Total'].sum()
max_words = 90  #maximum number of word
word_string = ''
for country in df_can.index.values:
     # check if country's name is a single-word name
    if country.count(" ") == 0:
        repeat_num_times = int(df_can.loc[country, 'Total'] / total_immigration * max_words)
        word_string = word_string + ((country + ' ') * repeat_num_times)
word_string  # display the generated text
#answer:'China China China China China China China China China Colombia Egypt France Guyana Haiti India India India India India India India India India Jamaica Lebanon Morocco Pakistan Pakistan Pakistan Philippines Philippines Philippines Philippines Philippines Philippines Philippines Poland Portugal Romania '

# create the word cloud
wordcloud = WordCloud(background_color='white').generate(word_string)

plt.figure(figsize=(14, 18))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# Step5: Plotting with Seaborn 

#a. counplot with seaborn>>sns.countplot(x, data=df)
#first find the unique names of the continent
df_can['Continent'].unique()

#A count plot can be thought of as a histogram across a categorical, instead of quantitative, variable
#seaborn.countplot is a function in the Seaborn library used to create a count plot, which displays the count of observations in each categorical bin. 
# unlike histogram that work on continous data the countplot funstion is used for categorical data. It displays the count of observations for each category (e.g., counts of different classes of items).
sns.countplot(x='Continent', data=df_can)  
#relace the long names with aliases
df_can1 = df_can.replace('Latin America and the Caribbean', 'L-America')
df_can1 = df_can1.replace('Northern America', 'N-America')
plt.figure(figsize=(15, 10))
sns.countplot(x='Continent', data=df_can1)


#b. Barplot with Seaborn>>sns.barplot(x,y,data=df)
plt.figure(figsize=(15, 10))
sns.barplot(x='Continent', y='Total', data=df_can1)
df_Can2=df_can1.groupby('Continent')['Total'].mean()


#c. Regression plot with Seaborn>>sns.regplot(x,y,data=df)
years = list(map(str, range(1980, 2014)))
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum(axis=0))
# change the years to type float (useful for regression later on)
df_tot.index = map(float, df_tot.index)
# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace=True)
df_tot.columns = ['year', 'total']  # rename columns
df_tot.head()
#create regression plot
plt.figure(figsize=(15, 10))
sns.set(font_scale=1.5)  #increase the font size of the tickmark labels, the title, and the x- and y-labels
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')  #or use plt.xlabel() and plt.ylabel()
ax.set_title('Total Immigration to Canada from 1980 - 2013')  # or use plt.title()
plt.show()


#in the above regression plot change the background color from purple to white
plt.figure(figsize=(15, 10))
sns.set(font_scale=1.5)
sns.set_style('ticks')  # change background to white background (this line is added)  #sns.set_style('whitegrid') gives us white background with grid
ax = sns.regplot(x='year', y='total', data=df_tot, color='green', marker='+', scatter_kws={'s': 200})  #scatter_kws={'s': 200}: customize the appearance of the scatter points
ax.set(xlabel='Year', ylabel='Total Immigration')
ax.set_title('Total Immigration to Canada from 1980 - 2013')
plt.show()

#Use seaborn to create a scatter plot with a regression line to visualize the total immigration from Denmark, Sweden, and Norway to Canada from 1980 to 201
df_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].T  #or use .transpose()
df_total = pd.DataFrame(df_countries.sum(axis=1))
df_total.reset_index(inplace=True)  #add index to this dataframe
df_total.columns = ['year', 'total']  #rename columns
df_total['year'] = df_total['year'].astype(int)  #change column 'year' from string into integer
plt.figure(figsize=(15, 10))  #define figuare size
sns.set(font_scale=1.5)  #set font size of the plot in Seaborn
sns.set_style('whitegrid')  #set background style of the plot in Seaborn

ax = sns.regplot(x='year', y='total', data=df_total, color='green', marker='+', scatter_kws={'s': 200})
ax.set(xlabel='Year', ylabel='Total Immigration')  #or use plt.xlabel() and plt.ylabel()
ax.set_title('Total Immigrationn from Denmark, Sweden, and Norway to Canada from 1980 - 2013')  # or use plt.title()






