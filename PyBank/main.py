import os
import csv

budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')
budget_data_out = os.path.join('.', 'analysis', 'budget_analysis.txt')


#init variables
total_months = 0
revenue_total = 0
revenue = []
previous_revenue = 0
revenue_change = 0
month_change = []
greatest = ["", 9999999]
least = ["", 0]
revenue_list = []
revenue_average = 0

#open csv file
with open(budget_data_csv) as in_file:
    reader = csv.reader(in_file)

    header = next(reader)

    row = next(reader)
    
    #Loop through rows
    for row in reader:

        #calculate total number of months       
        total_months =+ total_months
        
 #calculate total over period       
        revenue_total = revenue_total + int(row["Profit/Losses"])

 #calculate the average change       
        revenue_change = float(row["Profit/Losses"]) - previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_list = revenue_list + [revenue_change]
        month_change = [month_change] + [row["Date"]]

        #calculating Greatest Increase in Profits
        if revenue_change > greatest[1]:
            greatest[1] = revenue_change
            greatest[0] = row["Date"]

        #calculating Greatest Decrease in Profits
        if revenue_change < least[1]:
            least[1] = revenue_change
            least[0] = row["Date"]
revenue_average = sum(revenue_list) / len(revenue_list)


        

output = (
    f"Financial Analysis\n"
    f"------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${revenue_total}\n"
    f"Average Change: ${revenue_average}\n"
    f"Greatest Increase in Profits: {greatest[0], {greatest}}\n"
    f"Greatest Decrease in Profits: {least[0], {least[1]}}"
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

