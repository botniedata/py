# Import packages
import os

# Change current director to csv folder
os.chdir(r'c:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox\csv')

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    count_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in count_dict.keys():
            count_dict[first_col] +=1

        # Else, add to the dict and set value to 1
        else:
            count_dict[first_col] = 1

# Print the resulting dictionary
print(count_dict)