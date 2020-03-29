# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is,", now)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: perform analysis
    print(election_data)

# To do: perform analysis.

# Close the file.
election_data.close()

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
# with open(file_to_load) as election_data:

    # Print the file object
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a file variable to a direct or indirect path to the file.
with open (file_to_load) as election_data:

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    # txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")

    # To do: read and analyze the data here.

    # Read the file object with the reader funcition.
    file_reader = csv.reader(election_data)

    # Print header row.
    headers = next(file_reader)
    print(headers)

# Close the file
csv.reader.close()