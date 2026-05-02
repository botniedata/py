# Import os
import os
import pandas as pd

# Change directory to get the csv file
os.chdir(r'c:\Users\Joseph Antonio\Desktop\datacamp-python\python_toolbox\csv')

# Call the csv file as dataFrame
df = pd.read_csv('tweets.csv')

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)