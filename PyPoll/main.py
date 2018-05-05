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
        poll_results = {}
        next(csv_reader, None)

        for row in csv_reader:
            # Voter ID,County,Candidate
            #print([row[2] for row in csv_reader])
            total = total + 1
            poll_results[row[2]] = (
                {"Voter ID": row[0], "County": row[1], "Candidate": row[2]})

        candidates = [v["Candidate"] for k, v in poll_results.items()]
        poll_results["total"] = total
        poll_results["candidates"] = candidates
        #for candidate in candidates:
            #poll_results[candidate] = count votes per candidate then dive by total and get %
    return poll_results


def print_results(poll_results):
    print("Election Results")
    print("----------------------------")
    print("Total Votes:"+str(poll_results["total"]))
    print("----------------------------")
    print(poll_results["candidates"][0]+': '+str(len(poll_results)))
    print(poll_results["candidates"][1]+': '+str(len(poll_results)))
    print(poll_results["candidates"][2]+': '+str(len(poll_results)))
    print(poll_results["candidates"][3]+': '+str(len(poll_results)))
    print(len(poll_results[poll_results["candidates"][0]]))


def update_txt_file(poll_results):
    temp = []
    temp.append("Poll Results: \n")

    for k, v in poll_results.items():
        temp.append(k+":" + str(v) + "\n")

    with open(output_path, "wt", newline="") as outputfile:
        outputfile.writelines(temp)


def main():
    """main function."""
    poll_results_data = analyze_data(my_csv_path_1)
    print_results(poll_results_data)
    update_txt_file(poll_results_data)


if __name__ == "__main__":
    main()
