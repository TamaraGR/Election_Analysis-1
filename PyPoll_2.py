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
file_to_save = os.path.join("Analysis_Projects/Election_Analysis/Analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Get candidate from each list.
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load, 'r') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
    # Add to the total vote count
        total_votes = total_votes + 1
    # Print the candidate name for each row
        candidate_name = row[2]

    # Add the candidate name to the candidate options
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
                        
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

        # Save the results to our text file.
        txt_file = open(file_to_save, "w")
        with open(file_to_save, "w") as txt_file:
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(election_results)

            for candidate_name in candidate_votes:
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                txt_file.write(candidate_results)
    print(winning_candidate_summary)
    txt_file.close()

txt_file.close()
#txt_file = open(file_to_save, 'w')
# txt_file.write(candidate_results)


#     txt_file = open(file_to_save, "w")
#     winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")
#     print(winning_candidate_summary)
#     txt_file.write(winning_candidate_summary)
# txt_file.close()



    # Print the total votes, and format it to make it more legible
    # print(f'{total_votes:,d}')
    # Print out the candidates
    # print(candidate_options)
    # Print out the dictionary contain the candidates and their vote totals
    # print(candidate_votes)

election_data.close()


# txt_file = open(file_to_save, "w")
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.
#     # txt_file.write("Hello World")
#     txt_file.write("Counties in Election\n")
#     txt_file.write("-" * 25)
#     txt_file.write("\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# txt_file.close()