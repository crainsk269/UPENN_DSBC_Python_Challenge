# Analyze the financial records of your company
import csv

# Create Variables
title = "Financial Analysis"
line_separator = "----------------------------------"
total_months = 0
total_pnl = 0
current_pnl = 0
average_change = 0
monthly_dates = []
monthly_change = []

# Set Variable for file path
budget_path = 'Resources/budget_data.csv'

# Open CSV file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    prior_pnl = next(csvreader)
    total_months += 1
    total_pnl += int(prior_pnl[1])
    current_pnl = int(prior_pnl[1])
    
    for row in csvreader:
        monthly_dates.append(row[0])
        average_change = int(row[1]) - current_pnl
        monthly_change.append(average_change)
        current_pnl = int(row[1])
        total_months += 1
        total_pnl = total_pnl + int(row[1])
        avg_change = round(sum(monthly_change) / len(monthly_change),2)

    # Greatest Increase and Decrease Amount and Month
    greatest_increase = max(monthly_change)
    greatest_decrease = min(monthly_change)

    greatest_increase_index = monthly_change.index(greatest_increase)
    greatest_decrease_index = monthly_change.index(greatest_decrease)

    greatest_increase_date = monthly_dates[greatest_increase_index]
    greatest_decrease_date = monthly_dates[greatest_decrease_index]

        
# Print Results
print(title)
print(line_separator)
print(f'Total Months: {total_months}')
print(f'Total: ${total_pnl}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')


# Print to text file
PyBank_text = "Analysis/PyBank_Results.txt"

with open(PyBank_text, 'w') as textfile:
    line1 = title + "\n"
    line2 = line_separator + "\n"
    line3 = "Total Months: " + str(total_months) + "\n"
    line4 = "Total: $" + str(total_pnl) + "\n"
    line5 = "Average Change: $" + str(avg_change) + "\n"
    line6 = "Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" + "\n"
    line7 = "Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")"
    textfile.writelines([line1, line2, line3, line4, line5, line6, line7])
    textfile.close