# Import the pandas package
import pandas as pd
import os

# Change directory to target the csv file
os.chdir(r'C:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox\csv')

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize= 1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interests: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pop_list
pop_list = list(pops)

# Print pop_list
print(pop_list)