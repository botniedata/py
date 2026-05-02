# Import packages
import os

# Change current director to csv folder
os.chdir(r'c:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox\csv')

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until end of the file
    while True:

        # Read a line form the file data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yeild the line of data
        yield data

# Initialize an empty dictionary: counts_dict
counts_dict = {}        

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterage over the generator from read_large_file:
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else: 
            counts_dict[first_col] = 1

# Print 
print(counts_dict)

