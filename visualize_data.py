import pandas as pd
import matplotlib.pyplot as plt

#read a csv file
vehicles = pd.read_csv("vehicles.csv")

#print(vehicles.head())

#Relationship visualization 
#vehicles.plot(kind='scatter', x='drive', y='co2emissions', c='DarkBlue')
#plt.show()

#Distribution visualization 
#vehicles['co2emissions'].plot(kind='hist')
#plt.show()

#Comparison visualization 
#pvt = vehicles.pivot(columns='drive', values='co2emissions')
#pvt.plot(kind='box', figsize=(10, 6))
#plt.show()

#Composition visualization 
#vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(10,6))
#plt.show()

#Composition visualization with filtered data
rsltDf = vehicles[vehicles['drive'] == '2-Wheel Drive']
rsltDf.groupby('year')['drive'].value_counts().unstack().plot(kind='bar', stacked=True, figsize=(10,6))
plt.show()
