import os
import csv
csvpath=os.path.join('Resources','budget_data.csv')

# Set variables
Counter = 0
Total_sum = 0
Greatest_increase = 0
Greatest_decrease = 0
Greatest_increase_date = 0
Greatest_decrease_date= 0
Previous_profit = 0
Changes = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)    #pull out header row 
    firstrow = next(csvreader)
    Previous_profit = int(firstrow[1])
    Counter += 1
    Total_sum = int(firstrow[1])

    for row in csvreader:
# Counter is updating the month count
        Counter += 1
# Total sum is the total profit or losses
        Total_sum = Total_sum + int(row[1])
# Changes in Profit and loss 
        if Previous_profit != 0:
            Changes.append(int(row[1]) - Previous_profit)
# Update Greatest_decrease and Greatest_increase
        if (int(row[1]) - Previous_profit) < 0:
            if Greatest_decrease > int(row[1]) - Previous_profit:
                Greatest_decrease = int(row[1]) - Previous_profit
                Greatest_decrease_date = row[0] 
        else:
            if Greatest_increase < int(row[1]) - Previous_profit:
                Greatest_increase = int(row[1]) - Previous_profit
                Greatest_increase_date = row[0]
        Previous_profit = int(row[1])
 # The average of those changes
Change_Total = 0
for Change in Changes:
    Change_Total += Change
Average = Change_Total/len(Changes)
# The total number of months included in the dataset
print(f'Total Months: {Counter}')
# The net total amount of "Profit/Losses" over the entire period
print(f'Total: $ {Total_sum}')
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print (f'Average Change : $ {Average}')
print(f'Greatest Increase in Profits : {Greatest_increase_date} $ {Greatest_increase}')
print(f'Greatest Decrease in Profits : {Greatest_decrease_date} $ {Greatest_decrease}')


    # Open a text file for writing the results
with open("financial_analysis.txt", "w") as file:
    # Write financial analysis to the file
    file.write(f"Financial Analysis\n\n")
    file.write(f"---------------------------\n\n")
    file.write(f"Total Months: {Counter}\n\n")
    file.write(f"Total: {Total_sum}\n\n")
    file.write(f"Average of changes:{Average}\n\n")
    file.write(f"Greatest increase: {Greatest_increase_date} {Greatest_increase}\n\n")
    file.write(f"Greatest decrease: {Greatest_decrease_date} {Greatest_decrease}\n\n")