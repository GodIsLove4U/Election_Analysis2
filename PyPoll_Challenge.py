# 1. Calculate the total number of votes cast
# 2. Get a complete list of candidates who received votes
# 3. Calculate the total number of votes each candidate received
# 4. Calculate the percentage of votes each candidate won
# 5. Determine the winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# CHALLENGE - Add Counties
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ''
winning_count = 0
winning_percentage = 0
# CHALLENGE - Add largest county turnout
largest_turnout_county = ''

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]
        # CHALLENGE - get county name
        county_name = row[1]

        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # CHALLENGE - If county does not match any existing county, add
        # CHALLENGE - the county list
        if county_name not in county_options:
            # CHALLENGE - Add county name to the county list
            county_options.append(county_name)
            # CHALLENGE - Track county voter count
            county_votes[county_name] = 0
        # CHALLENGE - Add vote to county count
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        # CHALLENGE - print county votes
        f"County Votes:\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # CHALLENGE county calc
    for county in county_votes:
        
        # Retrieve vote count and percentage.
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) or (county == ''):
            winning_count = votes
            largest_turnout_county = county

    # Print the county results to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest county turnout: {largest_turnout_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_county_summary)

    # CHALLENGE - winning totals
    winning_count = 0

    # CHALLENGE - candidate count and percentages
    for candidate in candidate_votes:
        # CHALLENGE - retrieve counts and percentages
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # CHALLENGE - print candidate's count and percentage
        print(candidate_results)

        # CHALLENGE - save results to text file
        txt_file.write(candidate_results)

        # CHALLENGE - determine winning count, percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # CHALLENGE - print winning candidate results to terminal
    winning_candidate_summary = (
        f"------------------------\n"
        f"WINNER: {winning_candidate}\n"
        f"WINNING VOTE COUNT: {winning_count:,}\n"
        f"WINNING %: {winning_percentage:.1f}%\n"
        f"------------------------\n")
        
    # CHALLENGE - print winner summary
    print(winning_candidate_summary)

    # CHALLENGE - Save winning candidate's results to text file
    txt_file.write(winning_candidate_summary)