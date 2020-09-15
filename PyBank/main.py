import os
import csv

csvpath = os.path.join('budget_data.csv')

total_month = 0
total_profit = 0
greatest_increase_amount = 0
greatest_increase_date = ""
greatest_decrease_amount = 0
greatest_decrease_date = ""

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        total_month += 1
        total_profit += int(row[1])
        if int(row[1]) >=greatest_increase_amount:
            greatest_increase_amount = int(row[1])
            greatest_increase_date = row[0]
        if int(row[1]) <= greatest_decrease_amount:
            greatest_decrease_amount = int(row[1])
            greatest_decrease_date = row[0]

average_change = round(total_profit/total_month, 2)

print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_month))
print("Total Revenue: $" + str(total_profit))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Profit: $" + str(greatest_increase_amount) + greatest_increase_date)
print("Greatest Decrease in Profit: $" + str(greatest_decrease_amount) + greatest_decrease_date)

output = open("output.txt", "w")
output.write("Financial Analysis \n")
output.write("------------------------ \n")
output.write("Total Months: " + str(total_month) + "\n")
output.write("Total Revenue: $" + str(total_profit) + "\n")
output.write("Average Change: $" + str(average_change) + "\n")
output.write("Greatest Increase in Profit: $" + str(greatest_increase_amount) + greatest_increase_date)
output.write("\n")
output.write("Greatest Decrease in Profit: $" + str(greatest_decrease_amount) + greatest_decrease_date)
output.write("\n")