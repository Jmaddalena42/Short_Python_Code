import os
import pandas as pd
import numpy as np
import csv

df = pd.read_csv("Resources\election_data.csv")

print('Election Results')
print('-----------------------')
#Total Votes
total_votes = len(df.index)
print('Total Votes: ' + str(total_votes))
print('-----------------------')

#Find Candidate Counts
count = df.Candidate.value_counts()

#Change Display Format to %
pd.options.display.float_format = '{:.2f}%'.format

#Calculate Percentage of Total Votes
percentage = (df.Candidate.value_counts()/len(df.index))*100

#Make second Dataframe with columns for percent, count and rows of values
df2 = pd.DataFrame({'Percent': percentage, 'Count': count})
#Print Dataframe #2
print(df2.to_string(header=None))
print('-----------------------')

#Find Winner
winner = df.Candidate.mode().values
print('Winner: ' + str(winner))
print('-----------------------')

#write outputs to output.txt file
import sys
file = open('output.txt', 'w+')
sys.stdout = file

print('Election Results')
print('-----------------------')
print('Total Votes: ' + str(total_votes))
print('-----------------------')
print(df2.to_string(header=None))
print('-----------------------')
print('Winner: ' + str(winner))
print('-----------------------')

file.close()
