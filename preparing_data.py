import pandas as pd

#read a csv file
students = pd.read_excel("students.xlsx")

#get true o false result if 'State' value is null
#mask = students['State'].isnull()

#get only the student with 'State' is null
#studentStateNull = students[mask]

#remove missing values
#students.dropna()

#remove missing values with filter on specified column
#students.dropna(subset=['State', 'Zip'], how='all')

#drop column with missing values
#students.dropna(axis=1)

#drop column with nore than 10% missing values
#students.dropna(axis=1, thresh=10)

#replace missing values in a column with a specific value
#students = students.fillna({'Gender':'Female'})

#replace missing values with the median value of the column
#students = students.fillna({'Age': students['Age'].median()})

#replace value of a specific column of a specific record
mask = (students['Finance'] == 'Accountancy') & (students['State'] == 'IN') 
students.loc[mask, 'Zip'] = 49120

print(students)
