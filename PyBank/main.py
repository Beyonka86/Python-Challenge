import os
import csv

budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')
budget_data_out = os.path.join('.', 'analysis', 'budget_analysis.txt')


#init variables
total_months = 1
revenue_total = 0
revenue = []
previous_revenue = 0
revenue_change = 0
month_change = []
greatest = ["", -9999999]
least = ["", 9999999]
revenue_list = []
revenue_average = 0

#open csv file
with open(budget_data_csv) as in_file:
    reader = csv.reader(in_file)

    header = next(reader)

    row = next(reader)
   
    revenue_total = revenue_total + int(row[1])
    previous_revenue = float(row[1])

    #Loop through rows
    for row in reader:

        #calculate total number of months       
        total_months = total_months + 1
        
 #calculate total over period       
        revenue_total = revenue_total + int(row[1])

 #calculate the average change       
        revenue_change = float(row[1]) - previous_revenue
        previous_revenue = float(row[1])
        revenue_list = revenue_list + [revenue_change]
        month_change = [month_change] + [row[0]]

        #calculating Greatest Increase in Profits
        if revenue_change > greatest[1]:
            greatest[1] = revenue_change
            greatest[0] = row[0]

        #calculating Greatest Decrease in Profits
        if revenue_change < least[1]:
            least[1] = revenue_change
            least[0] = row[0]
revenue_average = sum(revenue_list) / len(revenue_list)


        

output = (
    f"Financial Analysis\n"
    f"------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${revenue_total}\n"
    f"Average Change: ${round(revenue_average, 2)}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${int(greatest[1])})\n"
    f"Greatest Decrease in Profits: {least[0]} (${int(least[1])})"
                                     )

print(output)
with open(budget_data_out,"w") as out_file:
    out_file.write(output)



