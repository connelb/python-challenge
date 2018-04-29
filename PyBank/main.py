"""•The total number of months included in the dataset
•The total amount of revenue gained over the entire period
•The average change in revenue between months over the entire period
•The greatest increase in revenue (date and amount) over the entire period
•The greatest decrease in revenue (date and amount) over the entire period"""

import os
import csv

my_csv_path_1 = os.path.join("../budget_data_1.csv")
my_csv_path_2 = os.path.join("../budget_data_2.csv")

with open(my_csv_path_1, newline="") as csvfile1:
    csv_reader1 = csv.reader(csvfile1, delimiter=",")

    # Skip the first row of the csv
    next(csv_reader1, None)

    # Loop through rows
    for row in csv_reader1:
        print(row)

"""
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
"""