#Ploting visualizations with Matplotlib

#To create a visualization directling with Matplotlib use plt.plot(x,y)
#Step1: Install neccessary libraries
import numpy as np  
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

# Step2: Fetching Data
from js import fetch
import io
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv"
resp = await fetch(URL)
text = io.BytesIO((await resp.arrayBuffer()).to_py())
df_can = pd.read_csv(text)
df_can.head()

# Step3: Data prepration
df_can.set_index('Country', inplace=True)  #set the Country as an index
years = list(map(str, range(1980, 2014)))  #ser a range of 1980-2013 as a list and change it to the string

# Step4: Create line plot>>plt.plot()
df_line=df_can[years]  #creating df with only years columns from 1980 - 2013
total_immigrants=df_line.sum()  #Applying sum to get total immigrants year-wise

#a. Create figure and axes
fig, ax = plt.subplots()
total_immigrants.index = total_immigrants.index.map(int)   #Changing the index type to integer
ax.plot(total_immigrants)
ax.set_title('Immigrants between 1980 to 2013') 
ax.set_xlabel('Years')
ax.set_ylabel('Total Immigrants')
plt.show()

#b.  add style to the above line plot
fig, ax = plt.subplots()
total_immigrants.index = total_immigrants.index.map(int)

# Customizing the appearance of Plot
ax.plot(total_immigrants, 
        marker='s', #Including markers in squares shapes
        markersize=5, #Setting the size of the marker
        color='green', #Changing the color of the line
        linestyle="dotted") #Changing the line style to a Dotted line

ax.set_title('Immigrants between 1980 to 2013') 
ax.set_xlabel('Years')
ax.set_ylabel('Total Immigrants')
ax.legend(['Immigrants'])
plt.show()

#c. add background grid to the above line plot
fig, ax = plt.subplots()
ax.plot(total_immigrants, 
        marker='s', #Including markers in squares shapes
        markersize=5, #Setting the size of the marker
        color='green', #Changing the color of the line
        linestyle="dotted") #Changing the line style to a Dotted line

ax.set_title('Immigrants between 1980 to 2013') 
ax.set_xlabel('Years')
ax.set_ylabel('Total Immigrants')
#limits on x-axis
plt.xlim(1975, 2015)  #or ax.set_xlim()
#Enabling Grid
plt.grid(True)  #or ax.grid()
#Legend
plt.legend(["Immigrants"]) #or ax.legend()
plt.show()


#Step5: create plot a line graph of immigration from Haiti
df_can.reset_index(inplace=True)
haiti=df_can[df_can['Country']=='Haiti']  #create a dataframe just for Haiti

#creating haiti with only years columns from 1980 - 2013 
#and transposing to get the result as a series
haiti=haiti[years].T  #or .transpose()
#converting the index to type integer
haiti.index = haiti.index.map(int)

#Plotting the line plot on the data>>plt.plot()
fig, ax = plt.subplots()
ax.plot(haiti)
ax.set_title('Immigrants from Haiti between 1980 to 2013') 
ax.set_xlabel('Years')
ax.set_ylabel('Number of Immigrants')
#Enabling Grid
#plt.grid(True)  #or ax.grid()
plt.legend(["Immigrants"]) #or ax.legend()  #add legend
plt.show()


#Step6: Create line plot for Haiti
fig, ax = plt.subplots()
ax.plot(haiti)
ax.set_title('Immigrants from Haiti between 1980 to 2013') 
#Setting up the Labels
ax.set_xlabel('Years')
ax.set_ylabel('Number of Immigrants')
#Enabling Grid and ticks
#plt.grid(True)  #or ax.grid()
#ax.set_xticks(list(range(n, m, s)))
plt.legend(["Immigrants"]) #or ax.legend()
ax.annotate('2010 Earthquake',xy=(2000, 6000))   #add annotate to the plot
plt.show()


# Step7: Create scatter plot>> plt.scatter()
fig, ax = plt.subplots(figsize=(8, 4))
total_immigrants.index = total_immigrants.index.map(int)

# Customizing Scatter Plot 
ax.scatter(total_immigrants.index, total_immigrants, 
           marker='o', #setting up the markers
           s = 20, #setting up the size of the markers
           color='darkblue')#the color for the marker

plt.title('Immigrants between 1980 to 2013') 
plt.xlabel('Years')
plt.ylabel('Total Immigrants') 
plt.grid(True)  #including grid
ax.legend(["Immigrants"], loc='upper center')   #Legend at upper center of the figure
plt.show()


#Bar plot>> plt.bar()
#Sorting the dataframe on 'Total' in descending order
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = df_can.head()
df_bar_5=df_top5.reset_index() #resetting the index back to original way
label=list(df_bar_5.Country)  #Creating a list of names of the top 5 countries
label[2]='UK'  #The third name is too lengthy to fit on the x-axis as label so we use alias

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(label,df_bar_5['Total'], label=label)
ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')
plt.show()


#Step8: Create a bar plot of the 5 countries that contributed the least to immigration to Canada from 1980 to 2013
#Sorting the dataframe on 'Total' in descending order
df_can.sort_values(['Total'], ascending=True, axis=0, inplace=True)
df_least5 = df_can.head()
df_least5_bar=df_least5.reset_index()  #resetting the index back to original way
label=list(df_least5_bar.Country)  #Creating alist of names of the top 5 countries
#create the plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(label, df_least5_bar['Total'],label=label)
ax.set_title('Immigration Trend of Top 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')
plt.show()

# Step9: create histogram plot>> plt.hist()
df_country = df_can.groupby(['Country'])['2013'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 4))
count = ax.hist(df_country['2013'])
#you can check the arrays in count with indexing count[0] for count, count[1] for bins
ax.set_title('New Immigrants in 2013') 
ax.set_xlabel('Number of Immigrants')
ax.set_ylabel('Number of Countries')
ax.set_xticks(list(map(int,count[1])))
ax.legend(['Immigrants'])
plt.show()


# Step10: immigration distribution for Denmark, Norway, and Sweden for years 1980 - 2013 (use histogram)
df=df_can.groupby(['Country'])[years].sum()
df_dns=df.loc[['Denmark', 'Norway', 'Sweden'], years]
df_dns=df_dns.T  #or .transpose()
df_dns
#create histogram plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df_dns)
ax.set_title('Immigration from Denmark, Norway, and Sweden from 1980 - 2013') 
ax.set_xlabel('Number of Immigrants')
ax.set_ylabel('Number of Years')
ax.legend(['Denmark', 'Norway', 'Sweden'])
plt.show()


# Step11:immigration distribution for China and India for years 2000 to 2013
df=df_can.groupby(['Country'])[years].sum()
y=list(map(str,range(2000, 2014)))
df_ci=df.loc[['China', 'India'], y]
df_ci=df_ci.T  #or .transpose()
#create plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df_ci)
ax.set_title('Immigration from Denmark, Norway, and Sweden from 1980 - 2013') 
ax.set_xlabel('Number of Immigrants')
ax.set_ylabel('Number of Years')
ax.legend(['China', 'India'])
plt.show()


# Step12: Pie Chart>>plt.pie()
fig,ax=plt.subplots()
#Pie on immigrants
ax.pie(total_immigrants[0:5], labels=years[0:5], 
       colors = ['gold','blue','lightgreen','coral','cyan'],
       autopct='%1.1f%%',explode = [0,0,0,0,0.1]) #using explode to highlight the lowest 
ax.set_aspect('equal')  # Ensure pie is drawn as a circle
plt.title('Distribution of Immigrants from 1980 to 1985')
#plt.legend(years[0:5]), include legend, if you donot want to pass the labels
plt.show()


# Step13:Create a pie chart representing the total immigrants proportion for each continent>>plt.pie()
df_con=df_can.groupby('Continent')['Total'].sum().reset_index()
label=list(df_con.Continent)
label[3] = 'LAC'  #set the alias name
label[4] = 'NA'   #set the alias name
df_con

fig,ax=plt.subplots(figsize=(10, 4))
ax.pie(df_con['Total'], colors = ['gold','blue','lightgreen','coral','cyan','red'],
        autopct='%1.1f%%', pctdistance=1.25)
ax.set_aspect('equal')  # Ensure pie is drawn as a circle
plt.title('Continent-wise distribution of immigrants')
ax.legend(label,bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()

# Step14: Sub plotting>>plt.subplots(rows, columns)
# a. Create a figure with two axes in a row>>use plt.subplots()
fig, axs = plt.subplots(1, 2, sharey=True)  # one row and two columns
#Plotting in first axes - the left one
axs[0].plot(total_immigrants)  #line plot
axs[0].set_title("Line plot on immigrants")
#Plotting in second axes - the right one
axs[1].scatter(total_immigrants.index, total_immigrants)  #scatter plot
axs[1].set_title("Scatter plot on immigrants")
axs[0].set_ylabel("Number of Immigrants")
#Adding a Title for the Overall Figure
fig.suptitle('Subplotting Example', fontsize=15)
fig.tight_layout()
plt.show()

# b. use plt.add_subplots(rows, columns, plot number) to create sub plotting
# Create a figure with two axes in a row
fig = plt.figure(figsize=(8,4))
# Add the first subplot (top-left)
axs1 = fig.add_subplot(1, 2, 1)
#Plotting in first axes - the left one
axs1.plot(total_immigrants)
axs1.set_title("Line plot on immigrants")

# Add the second subplot (top-right)
axs2 = fig.add_subplot(1, 2, 2)
#Plotting in second axes - the right one
axs2.barh(total_immigrants.index, total_immigrants) #Notice the use of 'barh' for creating horizontal bar plot
axs2.set_title("Bar plot on immigrants")
            
#Adding a Title for the Overall Figure
fig.suptitle('Subplotting Example', fontsize=15)
# Adjust spacing between subplots
fig.tight_layout()
plt.show()


# Step15: Choose four plots from above plots, which you have developed in this lab, with subplotting display them in a 2x2 display
fig = plt.figure(figsize=(10, 10))

# Add the first subplot (top-left)
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(total_immigrants)
ax1.set_title('Plot 1 - Line Plot')

# Add the second subplot (top-right)
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(total_immigrants.index, total_immigrants)
ax2.set_title('Plot 2 - Scatter plot')

# Add the third subplot (bottom-left)
ax3 = fig.add_subplot(2, 2, 3)
ax3.hist(df_dns)
ax3.set_title('Plot3 - Histogram') 
ax3.set_xlabel('Number of Immigrants')
ax3.set_ylabel('Number of Years')

# Add the fourth subplot (bottom-right)
ax4 = fig.add_subplot(2, 2, 4)
ax4.pie(total_immigrants[0:5], labels=years[0:5], 
        colors = ['gold','blue','lightgreen','coral','cyan'],
        autopct='%1.1f%%')
ax4.set_aspect('equal')  
ax4.set_title('Plot 5 - Pie Chart')

#Adding a Title for the Overall Figure
fig.suptitle('Four Plots in a Figure Example', fontsize=15)

# Adjust spacing between subplots
fig.tight_layout()
plt.show()