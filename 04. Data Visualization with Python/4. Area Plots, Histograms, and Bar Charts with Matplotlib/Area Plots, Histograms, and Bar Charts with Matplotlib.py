# Area Plots, Histograms, and Bar Charts:

#1. import neccessary libraries
import numpy as np  
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

#2. Fetching Data
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')

#3. Prepare data
df_can.set_index('Country', inplace=True) # set the index to 'Country' column

#create a list of years between 1980-2014 and change it to string
years = list(map(str, range(1980, 2014)))

#4. Create Stacked Line Plot or Area plot
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = df_top5[years].transpose()  # transpose the dataframe to have a better plot
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='area',
             alpha=0.25,  # 0 - 1, default value alpha = 0.5 (alpha is the transparancy of the any plot like area, line, histogram,...)
             stacked=False,  #This parameter controls whether the areas are stacked on top of each other (he areas will be displayed side by side, which allows you to see the individual contributions of each category more clearly, but it won’t represent their cumulative total)
             figsize=(20, 10))  # pass a tuple (x, y) size
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()

#5. Use the scripting layer to create a stacked area plot of the 5 countries that contributed the least to immigration to Canada from 1980 to 2013.
df_least5= df_can.tail(5)
df_least5 = df_least5[years].transpose() 
df_least5.index = df_least5.index.map(int)  #change the index values of df_least5 to type integer for plotting
df_least5.plot(kind='area', alpha=0.45, figsize=(20, 10)) #or use .plot.area()
plt.title('Immigration Trend of 5 Countries with Least Contribution to Immigration')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()


#6. Histogram Plot
#Note:By default, the histrogram method breaks up the dataset into 10 bins.
#frequency distribution of the number (population) of new immigrants from the various countries to Canada in 2013
count, bin_edges = np.histogram(df_can['2013'])  #count indicating how many values fall into each bin. and bin_edges indicating the edges of the bins
#answer for count is: [178  11   1   2   0   0   0   0   1   2]
#answer for bin_edges is: [    0.   3412.9  6825.8 10238.7 13651.6 17064.5 20477.4 23890.3 27303.2 30716.1 34129. ]
df_can['2013'].plot(kind='hist', figsize=(8, 5), xticks=bin_edges)  #df_can['2013'].plot.hist(),
plt.title('Histogram of Immigration from 195 countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label
plt.show()

# immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013
df_can.loc[['Denmark', 'Norway', 'Sweden'], years]
df_t = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_t.plot(kind='hist', figsize=(10, 6))
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()

# improve the above histogram by changing the number of bins, alpha and xticks=bin_edges
count, bin_edges = np.histogram(df_t, 15)
# un-stacked histogram
df_t.plot(kind ='hist', 
          figsize=(10, 6),
          bins=15,
          alpha=0.6,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen']
         )
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()


#change the colors of the above histogram plot
#If we do not want the plots to overlap each other, we can stack them using the stacked parameter. 
# Let's also adjust the min and max x-axis labels to remove the extra gap on the edges of the plot. We can pass a tuple (min,max) using the xlim paramater, as show below.
count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes 
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

# stacked Histogram
df_t.plot(kind='hist',
          figsize=(10, 6), 
          bins=15,
          xticks=bin_edges,
          color=['coral', 'darkslateblue', 'mediumseagreen'],
          stacked=True,
          xlim=(xmin, xmax)
         )
plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants') 
plt.show()


#Use the scripting layer to display the immigration distribution for Greece, Albania, and Bulgaria for years 1980 - 2013? Use an overlapping plot with 15 bins and a transparency value of 0.35.
df = df_can.loc[['Greece', 'Albania', 'Bulgaria'], years] #looking for 'Greece', 'Albania', 'Bulgaria' rows (these country names are in df_can.index)
df_cof = df_cof.transpose() # transpose the dataframe
count, bin_edges = np.histogram(df_cof, 15)  # let's get the x-tick values
# Un-stacked Histogram
df_cof.plot(kind ='hist',
            figsize=(10, 6),
            bins=15,  #by default we have 15 bins
            alpha=0.35,  #transparancy 
            xticks=bin_edges, 
            color=['coral', 'darkslateblue', 'mediumseagreen']  #add colors to the histogram
            )
plt.title('Histogram of Immigration from Greece, Albania, and Bulgaria from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')
plt.show()

#7. Bar Charts (kind=bar creates a vertical bar plot and kind=barh creates a horizontal bar plot)
#a. create vertical plot:compare the number of Icelandic immigrants (country = 'Iceland') to Canada from year 1980 to 2013.
df_iceland = df_can.loc['Iceland', years] 
df_iceland.head() 

df_iceland.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year') # add to x-label to the plot
plt.ylabel('Number of immigrants') # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013') # add title to the plot
plt.show()

#add annotations to the above plot
df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)  # rotate the xticks(labelled points on x-axis) by 90 degrees
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
# add Annotate arrow
plt.annotate('',  # s: str. Will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )
plt.show()


#add text to the annotate arrow in the above barplot
df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)
plt.xlabel('Year')
plt.ylabel('Number of Immigrants')
plt.title('Icelandic Immigrants to Canada from 1980 to 2013')
# Annotate arrow
plt.annotate('',  # s: str. will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )
# Annotate Text
plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' algned.
             )
plt.show()


#b. create horizontally barplot
#Using the scripting later and the df_can dataset, create a horizontal bar plot showing the total number of immigrants to Canada from the top 15 countries, for the period 1980 - 2013. Label each country with the total immigrant count.
df_can.sort_values(by='Total', ascending = True, inplace=True)
df_top15 = df_can['Total'].tail(15)
df_top15.plot(kind='barh', figsize=(12, 12), color='steelblue')
plt.xlabel('Number of Immigrants')
plt.title('Top 15 Conuntries Contributing to the Immigration to Canada between 1980 - 2013')
# annotate value labels to each country
for index, value in enumerate(df_top15):   #This iterates over the rows of df_top15, giving you both the index (which corresponds to the country) and the value (the number of immigrants).
    label = format(int(value), ',') # format int with commas (This formats the integer value to include commas for better readability (e.g., 1000 becomes 1,000))
# place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
plt.annotate(label, xy=(value - 47000, index - 0.10), color='white') #this way we are adding the number of immigrants in each contry (label)
#xy=(value - 47000, index - 0.10): This sets the position of the annotation.  
plt.show()


