import os
import csv
import pandas as pd
# define and initiate some variables for counting months and financial data
i = 0
month_count = 0
date_list = []
profit_l_list = []
profit_l_list_shift = []
total_p_l = 0
profit_l_difference = float(0)
profit_l_difference_list = []
i = 0

# define the path to the file that contains the results of the election
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# open the file as a csv file
with open(csvpath, 'r', newline='') as csvfile:
# read the csv file and store the contents in a variable called csvreader
    csv_reader = csv.reader(csvfile, delimiter=',')
# define the header of the csv file just opened and read and skip it when analysis begins
    csv_header = next(csv_reader)
# loop through the dataset to count months and add to list of dates and profit/loss values
    for row in csv_reader:
        month_count += 1
        profit_l_list.append(float(row[1]))
        profit_l_list_shift.append(float(row[1]))
        date_list.append(str(row[0]))

# Build profit/loss difference list
for p_l_value in profit_l_list and profit_l_list_shift:
        profit_l_difference = profit_l_list[1] - profit_l_list_shift[0]

        profit_l_difference_list.append(profit_l_difference)
        

# define function to compute average change in profit/loss between months

def average(profit_l_difference_list):
    x = len(profit_l_difference_list)
    total = sum(profit_l_difference_list)
    avg = total / x
    return avg

profit_l_change = average(profit_l_difference_list)
# print report    
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
total_p_l = sum(profit_l_list)
print(f"Total: ${total_p_l}")
print(f"Average Change: ${profit_l_change}")

# to match the dates with the highest and lowest profit/loss values, we zip the lists together
highest_p_l = max(profit_l_list) 
lowest_p_l = min(profit_l_list)

print(f"Greatest Increase in Profits: [date] ({highest_p_l})")

print(f"Greatest Decrease in Profits: [date] ({lowest_p_l})")






   





