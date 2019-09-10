# PyPoll main.py calculates the votes and percentage of votes for 4 different candidates and shows the winner.

import os
import csv
import pandas as pd

poll_data_csv = os.path.join("/Users/dianeshomefolder/Documents/Code/UA Bootcamp Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

# Open and read csv for use with pandas to determine number and names of unique candidates
poll_data = pd.read_csv(poll_data_csv) 
poll_data["Candidate"].unique()

'''
These 2 print lines were used to determine the number and names of candidates who were competing in the election.
print(poll_data["Candidate"].unique())
print(len(poll_data["Candidate"].unique()))
Those 2 lines printed:
['Khan' 'Correy' 'Li' "O'Tooley"]
4
'''

# Open and read csv
with open(poll_data_csv, newline="") as file_object:
    poll_voting_data = csv.reader(file_object, delimiter = ',')

    # Read the header row first and move past it
    poll_voting_header = next(poll_voting_data)

    '''
    The following print line was used to confirm column names in the database:
    print(f"Poll Voting Header: {poll_voting_header}") 
    It printed:
    Poll Voting Header: ['Voter ID', 'County', 'Candidate']
    '''

    # Read through each "Voter ID", "County" and "Candidate" row after the header
    id_s = [] # list for adding up the total number of voters
    
    # set each candidate's vote count to zero before beginning for loop below
    Khan_vote_count = 0
    Correy_vote_count = 0
    Li_vote_count = 0
    O_Tooley_vote_count = 0

    # Use "for" loop to add up the votes for each candidate
    for voter_id, county, candidate in poll_voting_data:
        id_s.append(voter_id)  # use this to count the total number of votes (1 per voter id), appended to list created above

        if candidate == 'Khan':
            Khan_vote_count += 1

        if candidate == 'Correy':
            Correy_vote_count += 1

        if candidate == 'Li':
            Li_vote_count += 1

        if candidate == "O'Tooley":
            O_Tooley_vote_count += 1
        
    # Find total votes and percentage of votes that each candidate earned
    total_votes = len(id_s)
    percent_Khan = Khan_vote_count/total_votes*100
    percent_Correy = Correy_vote_count/total_votes*100
    percent_Li = Li_vote_count/total_votes*100
    percent_O_Tooley = O_Tooley_vote_count/total_votes*100

    #Determine the winner
    if Khan_vote_count > Correy_vote_count and Khan_vote_count > Li_vote_count and Khan_vote_count > O_Tooley_vote_count:
        winner = 'Khan'
    elif Correy_vote_count > Khan_vote_count and Correy_vote_count > Li_vote_count and Correy_vote_count > O_Tooley_vote_count:
        winner = 'Correy'
    elif Li_vote_count > Khan_vote_count and Li_vote_count > Correy_vote_count and Li_vote_count > O_Tooley_vote_count:
        winner = 'Li'
    else:
        winner = "O'Tooley"

#Print data to terminal
print("Election Results")
print("-------------------------------")
print("Total Votes: ", total_votes)
print("-------------------------------")
print("Khan: ", "{:.3f}".format(percent_Khan) +"% (" + str(Khan_vote_count) + ")")
print("Correy: ", "{:.3f}".format(percent_Correy) +"% (" + str(Correy_vote_count) + ")")
print("Li: ", "{:.3f}".format(percent_Li) +"% (" + str(Li_vote_count) + ")")
print("O'Tooley: ", "{:.3f}".format(percent_O_Tooley) +"% (" + str(O_Tooley_vote_count) + ")")
print("-------------------------------")
print("Winner: ", winner)
print("-------------------------------")

#Print data to file
with open('PyPoll_output.txt', 'w') as file:
    print("Election Results", file=file)
    print("-------------------------------", file=file)
    print("Total Votes: ", total_votes, file=file)
    print("-------------------------------", file=file)
    print("Khan: ", "{:.3f}".format(percent_Khan) +"% (" + str(Khan_vote_count) + ")", file=file)
    print("Correy: ", "{:.3f}".format(percent_Correy) +"% (" + str(Correy_vote_count) + ")", file=file)
    print("Li: ", "{:.3f}".format(percent_Li) +"% (" + str(Li_vote_count) + ")", file=file)
    print("O'Tooley: ", "{:.3f}".format(percent_O_Tooley) +"% (" + str(O_Tooley_vote_count) + ")", file=file)
    print("-------------------------------", file=file)
    print("Winner: ", winner, file=file)
    print("-------------------------------", file=file)   