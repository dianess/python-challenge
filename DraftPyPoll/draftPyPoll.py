import os
import csv
import pandas as pd

#poll_data_csv = os.path.join("/Users/dianeshomefolder/Documents/Code/UA Bootcamp Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

# Open and read csv
poll_data = pd.read_csv("/Users/dianeshomefolder/Documents/Code/UA Bootcamp Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv") 

candidate_list = []

# Find total votes and candidate votes
total_votes = len(poll_data["Voter ID"])
poll_data["Candidate"].unique()
candidate_list = poll_data["Candidate"].unique()

num_candidates = len(poll_data["Candidate"].unique())

num_votes_candidate = poll_data["Candidate"].value_counts()

# calculate percentage by candidate
percentage_by_candidate = (poll_data.groupby("Candidate").size()/poll_data["Candidate"].count())*100

# Create dataframe with requested data
printed_dataframe = pd.DataFrame({'Percentage': percentage_by_candidate, 'Total Votes': num_votes_candidate})

# Change display format to %
pd.options.display.float_format = '{:.2f}%'.format

# Find winner 
winner = poll_data.Candidate.mode().values

#Print data to terminal

print("Election Results")
print("-------------------------------")
print("Total Votes: ", total_votes)
print("-------------------------------")
print(printed_dataframe.to_string(header=None))
print("-------------------------------")
print("Winner: ", winner)
print("-------------------------------")