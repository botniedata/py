# Import pandas as pd
import pandas as pd
import os

# Check Current Working Directory
print(os.getcwd())

# Change the cwd to python_toolbox
os.chdir(r"c:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox\csv")

# Change csv file to a dataframe
df = pd.read_csv('tweets.csv')

# Extract the created_at column in df
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)
