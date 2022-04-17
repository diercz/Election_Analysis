# creating a path
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")

# create a filename variaable to a drict or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Set accumulator that will increment by 1 as it reads each row in the loop
total_votes = 0

# candidate options
candidate_options = []

# declare the empy dictionary
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:

# read the file object with the reader function
    file_reader = csv.reader(election_data)

# print the header row
    headers = next(file_reader)

# pring each row in the CSV File
    for row in file_reader:

# 2. Add to the total vot count
        total_votes += 1

# A complete list of candidates who received votes
        candidate_name = row[2]

# if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        
        # Add the candidate name to the candidate list
                candidate_options.append(candidate_name)
        
        # begin tracking that candidates vote count
                candidate_votes[candidate_name] = 0

        # counting candidate votes
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
#1. iterage through the candidate list
for candidate_name in candidate_votes:
        #2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. calculate the percentage of votes
        vote_percentage = (votes) / (total_votes) * 100
        #4. print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:,.2f}% of the vote")

# Winning Candidate and Winning Count tracker


#determine winning vote count and candidate
#1. detemine if the vote are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
#2. if truen then sett winning_count = votes and winning_percentate =
        # vote_percentage
                winning_candidate = votes
                winning_percentage = vote_percentage
        #3. set the wining candidate equal to the candidates name
                winning_candidate = candidate_name


#print out the winning candidate vote count and percentat to 
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# terminal
# print the candidate vote dictionary
#print(candidate_votes)
# print the list of candidates
#print(candidate_options)



# use the open statement to open the file as a text file
#with open(file_to_save, "w") as txt_file:

#write some data to the file
        #txt_file.write("Arapahoe\nDenver\nJefferson")



# Import the datetime class for the dateime module
        #import datetime as dt
# Use the now90 attribute on the datetime class to get the present time
        #now = dt.datetime.now()
# Print the present time
        #print("The time right now is", now)


# the data we need to retrieve

# the % of votes each candidate won
# the total number of votes each candidate won
# the winner of the election based on popular vote

