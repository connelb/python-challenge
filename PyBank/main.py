"""•The total number of months included in the dataset
•The total amount of revenue gained over the entire period
•The average change in revenue between months over the entire period
•The greatest increase in revenue (date and amount) over the entire period
•The greatest decrease in revenue (date and amount) over the entire period"""

import os
import csv

my_csv_path_1 = os.path.join("raw_data","budget_data_1.csv")
my_csv_path_2 = os.path.join("raw_data","budget_data_2.csv")


with open(my_csv_path_1, newline="") as csvfile1:
    csv_reader1 = csv.reader(csvfile1, delimiter=",")

    # Skip the first row of the csv
    next(csv_reader1, None)
    my_counter = 0
    my_sum = 0.0
    my_average = 0.00
    my_rolling_increase = 0
    my_rolling_increase_date = ""
    my_rolling_decrease = 0
    my_rolling_decrease_date = ""

    # Loop through rows
    for row in csv_reader1:
        my_counter += 1
        my_sum = float(row[1]) + my_average

        if float(row[1])> my_rolling_increase:
            my_rolling_increase = float(row[1])
            my_rolling_increase_date = row[0]
        
        if float(row[1])< my_rolling_decrease:
            my_rolling_dncrease = float(row[1])
            my_rolling_decrease_date = row[0]

    my_average = my_sum/my_counter

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:{my_counter}" )
print(f"Total Revenue: ${my_sum}")
print(f"Average Revenue Change: ${my_average}")
print(f"Greatest Increase in Revenue: {my_rolling_increase_date} (${my_rolling_increase})")
print(f"Greatest Decrease in Revenue:{my_rolling_decrease_date} (${my_rolling_decrease})")
#print(f"Greatest Decrease in Revenue: Aug-12 ($-652794)

"""
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
"""