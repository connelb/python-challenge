""" Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
------------------------- """


import os
import csv

my_csv_path_1 = os.path.join("raw_data", "election_data_1.csv")
my_csv_path_2 = os.path.join("raw_data", "election_data_2.csv")

output_path = os.path.join("output", "results.txt")

poll_results = {}


def analyze_data(my_csv_path):
    with open(my_csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        candidates = set()
        counter = 0
        my_result = {}
        next(csv_reader, None)

        for row in csv_reader:
            #Voter ID,County,Candidate
            my_result[row[2]] = ({"Voter ID":row[0],"County":row[1],"Candidate":row[2] })

        candidates = [v["Candidate"] for k,v in my_result.items()]

        for candidate in candidates:
            print(my_result[candidate])





      

""" Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206) """


"""         # Skip the first row of the csv
        next(csv_reader, None)
        my_counter = 0




        # Loop through rows
        for row in csv_reader:
            my_counter += 
            
            
            my_sum = float(row[1]) + my_average

            if float(row[1]) > my_rolling_increase:
                my_rolling_increase = float(row[1])
                my_rolling_increase_date = row[0]

            if float(row[1]) < my_rolling_decrease:
                my_rolling_decrease = float(row[1])
                my_rolling_decrease_date = row[0]

        my_average = (my_sum/my_counter)
        my_average = float(format(my_average, '.2f'))
        total_votes = my_counter

    financial_analysis = ({
        "Total Months": my_counter,
        "Total Revenue": my_sum,
        "Average Revenue Change": my_average,
        "Greatest Increase in Revenue": my_rolling_increase,
        "Greatest Increase in Revenue date": my_rolling_increase_date,
        "Greatest Decrease in Revenue": my_rolling_decrease,
        "Greatest Decrease in Revenue date": my_rolling_decrease_date
    })

    return financial_analysis """


def print_results(financial_analysis):
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:{float(financial_analysis['Total Months'])}")
    print(f"Total Revenue: ${financial_analysis['Total Revenue']}")
    print(
        f"Average Revenue Change: ${financial_analysis['Average Revenue Change']}")
    print(
        f"Greatest Increase in Revenue: {financial_analysis['Greatest Increase in Revenue date']} (${financial_analysis['Greatest Increase in Revenue']})")
    print(
        f"Greatest Decrease in Revenue:{financial_analysis['Greatest Decrease in Revenue date']} (${financial_analysis['Greatest Decrease in Revenue']})")



""" def update_csv_file(financial_analysis):
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
        writer.writerows(financial_analysis) """


def update_txt_file(financial_analysis):
    temp = []
    temp.append("Financial Results: \n")

    for k,v in financial_analysis.items():
        temp.append(k+":"+ str(v) +"\n")

    with open(output_path, "wt",newline="") as outputfile:
        outputfile.writelines(temp)


def main():
    """main function."""
    analyze_data(my_csv_path_1)
    #print_results(financial_analysis)
    #update_txt_file(financial_analysis)


if __name__ == "__main__":
    main()
