# Import pandas
import os
import pandas as pd

# Print the current wording directory
print("Current Directory:", os.getcwd())

# Print the change directory to target the csv file
os.chdir("intermediate_to_python/python_ecosystem")

# Read in sales.csv
sales_df = pd.read_csv("csv/sales.csv")

# Display the DataFrame info
print("---Data Frame Info---")
print(sales_df.info())