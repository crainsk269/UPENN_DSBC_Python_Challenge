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


# Print to csv file
results_path = "Analysis/PyPoll_Results.csv"
with open(results_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([str(f"Total Votes:{str(total_votes)} ")])
    csvwriter.writerow(["----------------------------------"])
    for x in range(len(candidates)):
        csvwriter.writerow([str(f"{candidates[x]} {str(percent_votes[x])} ({str(number_votes[x])})")])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([str(f"Winner:{str(winner_cdt)} ")])
    csvwriter.writerow(["----------------------------------"])
    csvfile.close
