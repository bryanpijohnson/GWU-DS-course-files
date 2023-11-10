import os
import csv

# This is the path of the CSV file relative to this file
election_csv = os.path.join("Resources", "election_data.csv")

# Opening CSV file to read
with open(election_csv) as csvfile:

    # Reading in the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Saving the header row in case for later and to skip the header row for analysis
    csv_header = next(csvreader)
    
    # Initializing variables for each candidate and total votes
    # This will be used to enter in the unique candidate names
    candidates = []
    # This will be used to track each candidates number of votes
    cand_votes = []

    # This will iterate through the csv.reader file once and will add the candidate name to the 
    # candidates list if it's not there already. When a new candidate is found, it will append 1 vote
    # to the cand_votes list and then each time that candidate is found after, it will add one more vote
    # to the cand_votes total for that candidate.
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            cand_votes.append(1)
        else:
            cand_votes[candidates.index(row[2])] += 1

# This calculates the total number of votes
n_votes = sum(cand_votes)

# This is a list I created to be able to print to the terminal and the file at the same time.
# The first 2 items are the header text and separator in the text file. The next 2 are the 
# total number of votes and the separator before the individual candidate stats.
# The next 3 items are the individual candidate names, number of votes, and percent of vote.
# The next item is the separator before announcing the winner. The next item announces the
# winner, and the last item is the separator.
output_file = ["Election Results", "-------------------------", \
    f"Total Votes: {n_votes}", "-------------------------", \
    f"{candidates[0]}: {round(100 * cand_votes[0] / n_votes, 3)}% ({cand_votes[0]})", \
    f"{candidates[1]}: {round(100 * cand_votes[1] / n_votes, 3)}% ({cand_votes[1]})", \
    f"{candidates[2]}: {round(100 * cand_votes[2] / n_votes, 3)}% ({cand_votes[2]})", \
    "-------------------------", \
    f"Winner: {candidates[cand_votes.index(max(cand_votes))]}", \
    "-------------------------"]

output_path = os.path.join("Analysis", "pypoll.txt")

with open(output_path, "w") as pypath:
    for item in output_file:
        print(item)
        pypath.write(item)
        pypath.write('\n')