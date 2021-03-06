import os
import csv

# Path to collect data from the Resources folder
wrestling.csv = os.path.join("Resources", "WWE-Data-2016.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def percentages(wrestlerData)

# Find the total number of matches wrestled
total_number = wins + losses + ties
# Find the percentage of matches won
percentage_won = (wins / total_number) * 100
# Find the percentage of matches lost
percentage_lost = (losses / total_number) * 100˛
# Find the percentage of matches drawn
percentage_tied = (ties / total_number) * 100
# Print out the wrestler's name and their percentage stats

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
