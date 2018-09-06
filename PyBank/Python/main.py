import os
import csv
import pandas as pd
# define and initiate some variables for counting months and financial data
i = 0
month_count = 0
monthly_p_l_list = []
monthly_p_l_list_shift = [0]
total_p_l = 0
p_l_difference = float(0)
p_l_difference_sum = float(0)
p_l_difference_list = []

# define the path to the file that contains the results of the election
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# open the file as a csv file
with open(csvpath, 'r', newline='') as csvfile:
# read the csv file and store the contents in a variable called csvreader
    csv_reader = csv.reader(csvfile, delimiter=',')
# define the header of the csv file just opened and read and skip it when analysis begins
    csv_header = next(csv_reader)
# loop through the dataset to create list of p_l values
    for row in csv_reader:
        month_count += 1
        monthly_p_l_list.append(float(row[1]))
        
        # monthly_difference = monthly_income(i+1) - monthly_income(i)
        # monthly_difference_list.append(monthly_difference[i])
        # i += 1
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
total_p_l = sum(monthly_p_l_list)
print(f"Total: ${total_p_l}")
highest_p_l = max(monthly_p_l_list)
print(f"Greatest Increase in Profits: [date] ({highest_p_l})")
lowest_p_l = min(monthly_p_l_list)
print(f"Greatest Decrease in Profits: [date] ({lowest_p_l})")



# make a list of differences between monthly p/l values

# for p_l in monthly_p_l_list:
   # p_l_difference = p_l[i + 1] - p_l[i]
  #  p_l_difference_list.append(p_l_difference)
# print(p_l_difference_list)



   





