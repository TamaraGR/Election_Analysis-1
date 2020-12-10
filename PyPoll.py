# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os


# Assign a variable to load the file from a path.
file_to_load = os.path.join("Analysis_Projects/Election_Analysis/Resources", "election_results.csv")

# Assign a variable to save the file from a path.
file_to_save = "Analysis_Projects/Election_Analysis/Analysis/election_results.txt"

with open(file_to_load, 'r') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row[0])

    # Print the file object
    print(election_data)

election_data.close()


#outfile = open(file_to_save, "w")
with open(file_to_save, "w") as outfile:
    # Write some data to the file.
    # outfile.write("Hello World")
    outfile.write("Counties in Election\n")
    outfile.write("-" * 25)
    outfile.write("\n")
    outfile.write("Arapahoe\nDenver\nJefferson")

outfile.close()