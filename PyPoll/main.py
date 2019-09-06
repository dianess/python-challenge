import os
import csv

poll_data_csv = os.path.join("/Users/dianeshomefolder/Documents/Code/UA Bootcamp Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

# Open and read csv
with open(poll_data_csv, newline="") as file_object:
    poll_voting_data = csv.reader(file_object, delimiter = ',')

    # Read the header row first
    poll_voting_header = next(poll_voting_data)
    # print(f"Poll Voting Header: {poll_voting_header}") #- used to check code

    # Read through each "Voter ID", "County" and "Candidate" row after the header
    id_s = []
    #first_candidate = 'Khan'
    Khan_vote_count = 0
    Correy_vote_count = 0
    Li_vote_count = 0
    O_Tooley_vote_count = 0

    for voter_id, county, candidate in poll_voting_data:
        id_s.append(voter_id)  # use this to count the total number of votes (1 per voter id)

        if candidate == 'Khan':
            Khan_vote_count += 1

        if candidate == 'Correy':
            Correy_vote_count += 1

        if candidate == 'Li':
            Li_vote_count += 1

        if candidate == "O'Tooley":
            O_Tooley_vote_count += 1
        
    total_votes = len(id_s)
    percent_Khan = Khan_vote_count/total_votes*100
    percent_Correy = Correy_vote_count/total_votes*100
    percent_Li = Li_vote_count/total_votes*100
    percent_O_Tooley = O_Tooley_vote_count/total_votes*100

    #Testing code
    if Khan_vote_count > Correy_vote_count and Khan_vote_count > Li_vote_count and Khan_vote_count > O_Tooley_vote_count:
        winner = 'Khan'
    elif Correy_vote_count > Khan_vote_count and Correy_vote_count > Li_vote_count and Correy_vote_count > O_Tooley_vote_count:
        winner = 'Correy'
    print(winner)


#Print data to terminal
print("Election Results")
print("-------------------------------")
print("Total Votes: ", total_votes)
print("-------------------------------")
print("Khan: ", "{:.3f}".format(percent_Khan),"% (", Khan_vote_count, ")")
print("Correy: ", "{:.3f}".format(percent_Correy),"% (", Correy_vote_count, ")")
print("Li: ", "{:.3f}".format(percent_Li),"% (", Li_vote_count, ")")
print("O'Tooley: ", "{:.3f}".format(percent_O_Tooley),"% (", O_Tooley_vote_count, ")")