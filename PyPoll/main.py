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
        total = 0
        my_result = {}
        next(csv_reader, None)

        for row in csv_reader:
            # Voter ID,County,Candidate
            #print([row[2] for row in csv_reader])
            total = total + 1
            my_result[row[2]] = (
                {"Voter ID": row[0], "County": row[1], "Candidate": row[2]})

        candidates = [v["Candidate"] for k, v in my_result.items()]

        for candidate in candidates:
            for k, v in my_result.items():
                temp = 0 
                if (k == candidate):
                    temp =+
                 temp1 = ({count: temp}) 
            
               
                    print(f"{candidate}: {}")
                    Rogers: 36.0% (223236)


def print_results(financial_analysis):
    print("Election Results")
    print("----------------------------")
    print("Total Votes:")
    print("----------------------------")


def update_txt_file(financial_analysis):
    temp = []
    temp.append("Financial Results: \n")

    for k, v in financial_analysis.items():
        temp.append(k+":" + str(v) + "\n")

    with open(output_path, "wt", newline="") as outputfile:
        outputfile.writelines(temp)


def main():
    """main function."""
    analyze_data(my_csv_path_1)
    # print_results(financial_analysis)
    # update_txt_file(financial_analysis)


if __name__ == "__main__":
    main()
