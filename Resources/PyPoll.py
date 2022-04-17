# creating a path
import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")

# create a filename variaable to a drict or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

# read the file object with the reader function
    file_reader = csv.reader(election_data)

# print the header row
    headers = next(file_reader)
    print(headers)


# use the open statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

#write some data to the file
        txt_file.write("Arapahoe\nDenver\nJefferson")



# Import the datetime class for the dateime module
        import datetime as dt
# Use the now90 attribute on the datetime class to get the present time
        now = dt.datetime.now()
# Print the present time
        print("The time right now is", now)


# the data we need to retrieve
# A complete list of candidates who received votes
# the % of votes each candidate won
# the total number of votes each candidate won
# the winner of the election based on popular vote

