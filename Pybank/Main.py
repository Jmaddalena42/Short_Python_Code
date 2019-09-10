import os
import pandas as pd
import numpy as np
import locale
import csv
#set locale for easy currency conversion
locale.setlocale( locale.LC_ALL, '' )
'English_United States.1252'

df = pd.read_csv('C:\\Users\\JMadd\\Desktop\\03-Python_Homework\\Instructions\\PyBank\\Resources\\budget_data.csv')

print('Financial Analysis')
print('------------------')

#total months
total_months = len(df.index)
print('Total Months: ' + str(total_months))

#Total Profits/Losses
Profit = locale.currency(df['Profit/Losses'].sum())
print('Total: ' + str(Profit))
        
#Average Change
Change = locale.currency(df['Profit/Losses'].mean())
print('Average Change: ' + str(Change))

#Greatest increase/ idxmax() gets the maximum value in column, df.iloc grabs that entire row, .values only grabs the values and leaves the column names out
print('Greatest Increase in Profits: ' + str(df.iloc[df['Profit/Losses'].idxmax()].values))

#Greatest Decrease/ idxmin() gets the minimum value in column, df.iloc grabs that entire row, .values only grabs the values and leaves the column names out
print('Greatest Decrease in Profits: ' + str(df.iloc[df['Profit/Losses'].idxmin()].values))

print('---')

#write outputs to Output.txt
import sys
file = open('output.txt', 'w+')
sys.stdout = file

print('Financial Analysis')
print('------------------')
print('Total Months: ' + str(total_months) )
print('Total: ' + str(Profit))
print('Average Change: ' + str(Change))
print('Greatest Increase in Profits: ' + str(df.iloc[df['Profit/Losses'].idxmax()].values))
print('Greatest Decrease in Profits: ' + str(df.iloc[df['Profit/Losses'].idxmin()].values))
print('---')

file.close()

