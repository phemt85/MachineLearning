import pandas as pd

#read a csv file
washers = pd.read_csv("washers.csv")

#print the info of Dataframe
washers.info()

#get the first five records of Dataframe
print(washers.head())

#return a statistical summary for each of the columns of the DataFrame
print(washers.describe())

#return a statistical summary for a columns of the DataFrame
print(washers[['BrandName']].describe())

#return the count value from specific column
print(washers[['BrandName']].value_counts())

#return the percentage distribution from values inside specific column
print(washers[['BrandName']].value_counts(normalize = True))

#return a group level aggregations
print(washers.groupby('BrandName')[['Volume']].mean())

#return a group level aggregations with sorting
print(washers.groupby('BrandName')[['Volume']].mean().sort_values(by='Volume', ascending=False))

#return a multiple group level aggregations
print(washers.groupby('BrandName')[['Volume']].agg(['min', 'max', 'mean']))
