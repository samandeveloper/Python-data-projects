#Exploratory Data Analysis - Laptops Pricing dataset

#install seaborn library and then import it
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#%matplotlib inline   #if you are using Jupyter Notebook uncomment this line

filepath="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(filepath, header=None)

#Step1: Visualize individual feature patterns

#1. CPU_frequency plot
sns.regplot(x="CPU_frequency", y="Price", data=df)
plt.ylim(0,)

#2. Screen_Size_inch plot
sns.regplot(x="Screen_Size_inch", y="Price", data=df)
plt.ylim(0,)

#3. Weight_pounds plot
sns.regplot(x="Weight_pounds", y="Price", data=df)
plt.ylim(0,)

#4. Correlation values of the three attributes above with Price
for param in ["CPU_frequency", "Screen_Size_inch","Weight_pounds"]:  #loop in the array
    print(f"Correlation of Price and {param} is ", df[[param,"Price"]].corr())  #df[[param, "Price"]].corr()


#Step2: Categorical features

#1. Generate Box plots for the different feature that hold categorical values. These features would be "Category", "GPU", "OS", "CPU_core", "RAM_GB", "Storage_GB_SSD"
sns.boxplot(x="Category", y="Price", data=df)

#2. GPU Box plot
sns.boxplot(x="GPU", y="Price", data=df)

#3. OS Box plot
sns.boxplot(x="OS", y="Price", data=df)

#4. CPU_core Box plot
sns.boxplot(x="CPU_core", y="Price", data=df)

#5. RAM_GB Box plot
sns.boxplot(x="RAM_GB", y="Price", data=df)

#6. Storage_GB_SSD Box plot
sns.boxplot(x="Storage_GB_SSD", y="Price", data=df)


#Step3: Descriptive Statistical Analysis
print(df.describe())
print(df.describe(include=['object']))

#Step4: GroupBy and Pivot Tables
#Group the parameters "GPU", "CPU_core" and "Price" to make a pivot table and visualize this connection using the pcolor plot.
df_gptest = df[['GPU','CPU_core','Price']]  #insert 'GPU','CPU_core','Price' in a dataframe
grouped_test1 = df_gptest.groupby(['GPU','CPU_core'],as_index=False).mean()   #groupby 'GPU','CPU_core' and get a mean()

# Create the Pivot table
grouped_pivot = grouped_test1.pivot(index='GPU',columns='CPU_core')   


# Create the Plot
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

fig.colorbar(im)


#Step5: Pearson Correlation and p-values (coefficient and p_values)
#Use the scipy.stats.pearsonr() function to evaluate the Pearson Coefficient and the p-values for each parameter tested above.
from scipy import stats
for param in ['RAM_GB','CPU_frequency','Storage_GB_SSD','Screen_Size_inch','Weight_pounds','CPU_core','OS','GPU','Category']:
    pearson_coef, p_value = stats.pearsonr(df[param], df['Price'])
    print(param)
    print("The Pearson Correlation Coefficient for ",param," is", pearson_coef, " with a P-value of P =", p_value)







