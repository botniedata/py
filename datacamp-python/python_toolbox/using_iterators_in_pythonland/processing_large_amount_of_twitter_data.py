# Import pandas as pd
import pandas as pd
import os

# Check Current Working Directory
print(os.getcwd())

# Change the cwd to python_toolbox
os.chdir(r"c:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox")

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunck by chunck
for chunk in pd.read_csv("csv/tweets.csv", chunksize = 10):

    # Iterate over the column in Dataframe
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)