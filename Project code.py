# This Project is using data from  https://www.kaggle.com/unsdsn/world-happiness
# A total of 5 .csv files were used.
# World Happiness Report of year 2015, 2016, 2017, 2018, 2019.

# Import libraries for reading data into frame, analysis and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import a CSV file into a Pandas DataFrame
db2015 = pd.read_csv("./DATA/2015.csv")
db2016 = pd.read_csv("./DATA/2016.csv")
db2017 = pd.read_csv("./DATA/2017.csv")
db2018 = pd.read_csv("./DATA/2018.csv")
db2019 = pd.read_csv("./DATA/2019.csv")

# Sorting data by 'GDP per capita' in Descending Order
GDP_2019 = db2019.sort_values(by ='GDP per capita',ascending=False)
Country_GDP_2018 = db2018[['Country or region','GDP per capita']].sort_values(by ='GDP per capita',ascending=False)
Country_GDP_2019 = db2019[['Country or region','GDP per capita']].sort_values(by ='GDP per capita',ascending=False)

# Replacing missing values for db2018 and db2019
db2018.fillna(0)
db2019.fillna(0)

# Slicing Top 5 row of db2019
db2019_top5row = db2019.iloc[[0,1,2,3,4,],:]

# Data of 'Healthy life expectancy' in 2019
db2019_hle = db2019.loc[:,'Healthy life expectancy']

# Merging dataframes
Country_Healthy_2019 = db2019[['Country or region','Healthy life expectancy']]
data_merge_2019 = pd.merge(Country_Healthy_2019, Country_GDP_2019)

# Function
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 0),
                    textcoords="offset points",
                    ha='center', va='bottom',rotation=0)

# Visualization
# Happiness Score vs Economy(GDP per Capita) in 2018, 2019
plt.plot(db2018['Score'],db2018['GDP per capita'])
plt.plot(db2019['Score'],db2019['GDP per capita'])
plt.title('Happiness Score vs Economy(GDP per Capita)')
plt.xlabel('Happiness Score')
plt.ylabel('Economy(GDP per Capita)')
plt.legend(["2018", "2019"])
plt.show()

# Happiness Score vs Healthy life expectancy 2018, 2019
plt.plot(db2018['Score'],db2018['Healthy life expectancy'])
plt.plot(db2019['Score'],db2019['Healthy life expectancy'])
plt.title('Happiness Score vs Healthy life expectancy')
plt.xlabel('Happiness Score')
plt.ylabel('Healthy life expectancy')
plt.legend(["2018", "2019"])
plt.show()

# Top 5 country happiness 2019
top5_2019 = db2019[['Country or region','Overall rank', 'Score']].head()
plt.bar(top5_2019['Country or region'],top5_2019['Score'])
plt.title('Top 5 Countries Happiness 2019')
for index, value in enumerate(top5_2019['Score']):
    plt.text(index-0.25,value, str(round(value,3)))
plt.show()

# Bottom 5 country happiness 2019
bottom5_2019 = db2019[['Country or region','Overall rank', 'Score']].tail()
plt.bar(bottom5_2019['Country or region'],bottom5_2019['Score'])
plt.title('Bottom 5 Countries Happiness 2019')
for index, value in enumerate(bottom5_2019['Score']):
    plt.text(index-0.25,value, str(round(value,3)))
plt.show()

# Happiness Score by Region 2015, 2016
labels = db2015['Region'].unique()
region_2015 = db2015.groupby('Region')['Happiness Score'].mean().round(2)
region_2016 = db2016.groupby('Region')['Happiness Score'].mean().round(2)
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, region_2015, width, label='2015')
rects2 = ax.bar(x + width/2, region_2016, width, label='2016')
ax.set_ylabel('Score')
ax.set_title('Happiness Score by Region')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.xticks(rotation = 60)
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()

