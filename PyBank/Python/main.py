import os
import csv
# define the path to the file that contains the results of the election
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# open the file as a csv file
with open(csvpath, 'r', newline='') as csvfile:
    # read the csv file and store the contents in a variable called csvreader
    csv_reader = csv.reader(csvfile, delimiter=',')
    # define the header of the csv file just opened and read and skip it when analysis begins
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
    # loop through entire file to count total votes, and votes per candidate


   





