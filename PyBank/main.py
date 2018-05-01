"""•The total number of months included in the dataset
•The total amount of revenue gained over the entire period
•The average change in revenue between months over the entire period
•The greatest increase in revenue (date and amount) over the entire period
•The greatest decrease in revenue (date and amount) over the entire period"""

import os
import csv

my_csv_path_1 = os.path.join("raw_data", "budget_data_1.csv")
my_csv_path_2 = os.path.join("raw_data", "budget_data_2.csv")

output_path = os.path.join("output", "financial_analysis.csv")

financial_analysis = {}

def analyze_date(my_csv_path):
    with open(my_csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")

        # Skip the first row of the csv
        next(csv_reader, None)
        my_counter = 0
        my_sum = 0.0
        my_average = 0.00
        my_rolling_increase = 0
        my_rolling_increase_date = ""
        my_rolling_decrease = 0
        my_rolling_decrease_date = ""

    
        # Loop through rows
        for row in csv_reader:
            my_counter += 1
            my_sum = float(row[1]) + my_average

            if float(row[1]) > my_rolling_increase:
                my_rolling_increase = float(row[1])
                my_rolling_increase_date = row[0]

            if float(row[1]) < my_rolling_decrease:
                my_rolling_decrease = float(row[1])
                my_rolling_decrease_date = row[0]

        my_average = (my_sum/my_counter)
        #my_average = float(format(my_average, '.2f'))


    financial_analysis = ({
        "Total Months": my_counter,
        "Total Revenue": my_sum,
        "Average Revenue Change": my_average,
        "Greatest Increase in Revenue": my_rolling_increase,
        "Greatest Increase in Revenue date": my_rolling_increase_date,
        "Greatest Decrease in Revenue": my_rolling_decrease,
        "Greatest Decrease in Revenue date": my_rolling_decrease_date
    })

    financial_analysis1 = [my_counter,my_sum,my_average,my_rolling_increase,my_rolling_increase_date,my_rolling_decrease,my_rolling_decrease_date]
    
    return financial_analysis

def print_results(financial_analysis):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:{float(financial_analysis['Total Months'])}")
    print(f"Total Revenue: ${financial_analysis['Total Revenue']}")
    print(f"Average Revenue Change: ${financial_analysis['Average Revenue Change']}")
    print(
        f"Greatest Increase in Revenue: {financial_analysis['Greatest Increase in Revenue date']} (${financial_analysis['Greatest Increase in Revenue']})")
    print(
        f"Greatest Decrease in Revenue:{financial_analysis['Greatest Decrease in Revenue date']} (${financial_analysis['Greatest Decrease in Revenue']})")

def update_csv_file(financial_analysis):
    with open(output_path, "w", newline="") as outputfile:
        fieldnames = [
            "Total Months",
            "Total Revenue",
            "Average Revenue Change",
            "Greatest Increase in Revenue",
            "Greatest Increase in Revenue date",
            "Greatest Decrease in Revenue",
            "Greatest Dncrease in Revenue date",
        ]
        writer = csv.DictWriter(outputfile, fieldnames)
        writer.writeheader()
        writer.writerows(financial_analysis)

def update_txt_file(financial_analysis):
    print(financial_analysis)

    
    with open(output_path, "wt", newline="") as outputfile:
        y = []
        for x in financial_analysis:
            print(x)
            y.append(x+'\n')
        outputfile.writelines(y)


def main():
    """main function."""
    financial_analysis = analyze_date(my_csv_path_1)
    print_results(financial_analysis)
    update_txt_file(financial_analysis)


if __name__ == "__main__":
    main()