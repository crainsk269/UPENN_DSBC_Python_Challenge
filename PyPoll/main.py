import csv

# Create Variables
title = "Election Results"
line_separator = "----------------------------------"
total_votes = 0
candidates = []
number_votes = []
percent_votes = []

# Set Variable for file path
election_path = "Resources/election_data.csv"

# Open CSV file
with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes [index] += 1

# Calculate Percentages
for votes in number_votes:
   percentage = (votes/total_votes)*100
   percentage = "%.3f%%" % percentage
   percent_votes.append(percentage)

# Calculate Winner
winner = max(number_votes)
index = number_votes.index(winner)
winner_cdt = candidates[index]

# Print Results
print(title)
print(line_separator)
print(f'Total Votes:{str(total_votes)}')
print(line_separator)
for x in range(len(candidates)):
    print(f"{candidates[x]}: {str(percent_votes[x])} ({str(number_votes[x])})")
print(line_separator)
print(f"Winner: {winner_cdt}")
print(line_separator)


# Print to text file
PyPoll_text = "Analysis/PyPoll_Results.txt"

with open(PyPoll_text, 'w') as textfile:
    line1 = title + "\n"
    line2 = line_separator + "\n"
    line3 = "Total Votes: " + str(total_votes) + "\n"
    line4 = line_separator + "\n"
    line5 = str{candidates[x]} {str(percent_votes[x])} ({str(number_votes[x])}) + "\n"
    line6 = line_separator + "\n"
    line7 = "Winner: " + str(winner_cdt) + "\n"
    line8 = line_separator
    textfile.writelines([line1, line2, line3, line4, line5, line6, line7, line8])
    textfile.close