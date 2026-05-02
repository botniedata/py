# Import the pandas package
import pandas as pd
import os

# Change directory to target the csv file
os.chdir(r'C:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox\csv')

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize= 10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))