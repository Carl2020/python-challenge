import os
import csv
# set the total number of votes before the election begins equal to zero
total_votes = 0
# list the names of the candidates up for election
candidate_name = ["Khan", "Correy", "Li", "O'Tooley"]
# set the vote counter and vote percentage for the 4 candidates to zero
candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []
# define the path to the file that contains the results of the election
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# open the file as a csv file
with open(csvpath, 'r', newline='') as csvfile:
    # read the csv file and store the contents in a variable called csvreader
    csv_reader = csv.reader(csvfile, delimiter=',')
    # define the header of the csv file just opened and read and skip it when analysis begins
    csv_header = next(csv_reader)

    # loop through entire file to determine candidate names and add to candidate list

  
     # loop through entire file to count total votes, and votes per candidate
    for row in csv_reader:
        total_votes += 1

        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] += 1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1

    # create a function to calculate the percentage of the total vote for each candidate
    candidate_vote_percent[0] = round(100 * (candidate_vote[0] / total_votes), 4)
    candidate_vote_percent[1] = round(100 * (candidate_vote[1] / total_votes), 4)
    candidate_vote_percent[2] = round(100 * (candidate_vote[2] / total_votes), 4)
    candidate_vote_percent[3] = round(100 * (candidate_vote[3] / total_votes), 4)
    # Determine who the winner is
    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[3]

    # print the report to the terminal screen
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
    print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
    print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
    print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
    print("-----------------------------")
    print(f"Winner: {candidate_winner}")
# create a path to a text file in the Output folder

output_path = os.path.join("..", "Output", "Election_Results.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ' ')

    # write the report into a text file in the Output folder
    csvwriter.writerow('Election Results')
    csvwriter.writerow('-----------------------------')
    csvwriter.writerow(f'Total Votes: {total_votes}')
    csvwriter.writerow('-----------------------------')
    csvwriter.writerow(f'{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})')
    csvwriter.writerow(f'{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})')
    csvwriter.writerow(f'{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})')
    csvwriter.writerow(f'{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})')
    csvwriter.writerow('-----------------------------')
    csvwriter.writerow(f'Winner: {candidate_winner}')
    csvfile.close()



    

 





    