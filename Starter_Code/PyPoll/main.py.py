import os
import csv
csvpath=os.path.join('Resources','election_data.csv')

# Set variables
Total_number_of_votes = 0
Candidate_votes = {}
votes = 0
winning_candidate = ""
Winning_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)    #pull out header row
    
    for row in csvreader:

    # Count the total number of votes
        Total_number_of_votes += 1
        candidate_name = row[2]

    #Loops through the rows and find the vote count for each candidate
        if candidate_name in Candidate_votes:
            Candidate_votes[candidate_name] +=1
        else:
            Candidate_votes[candidate_name] =1

# Print header
print("Election votes: ")
# Print Total number of votes
print("Total votes:", Total_number_of_votes)
# Print complete list of candidates
print ("Candidate votes:", Candidate_votes)

# Open a text file for writing the results
with open("election_results.txt", "w") as file:
    file.write(f"Election Results\n\n")
    file.write(f"---------------------------\n\n")
# Write the total number of votes cast to the file
# Print complete list of candidates
    file.write(f"Total Votes: {Total_number_of_votes}\n\n")
    file.write(f"---------------------------\n\n")

# Calculate percentage of votes for each candidate
    for candidate_name, votes in Candidate_votes.items():
        percentage = (votes/Total_number_of_votes) *100 
        print(f"{candidate_name}: {percentage:.2f}% ({votes})")
# Write the list of candidates, percentage and number of votes to the file
        file.write(f"{candidate_name}: {percentage:.2f}% ({votes})\n\n")
        file.write(f"---------------------------\n\n")

# Calculate the winner of the election based on popular vote
        if votes > Winning_count:
            Winning_count = votes
            winning_candidate = candidate_name

    print("Winner:", winning_candidate)
    #Write winner
    file.write(f"Winner: {winning_candidate}\n\n")
    file.write(f"---------------------------\n\n")