import os
import csv

budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')
budget_data_out = os.path.join('.', 'analysis', 'budget_analysis.txt')

#init variables
total_months = 0

with open(budget_data_csv) as in_file:
    reader = csv.reader(in_file)

    header = next(reader)
    
    for row in reader:
        total_months = total_months + 1


        

output = (
    f"Financial Analysis\n"
    f"------------------------------------------------\n"
    f"Total Months: {total_months}\n"
)

print(output)
with open(budget_data_out,"w") as out_file:
    out_file.write(output)



# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

