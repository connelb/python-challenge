import os
import csv

my_csv_path_1 = os.path.join("raw_data", "employee_data1.csv")
my_csv_path_2 = os.path.join("raw_data", "employee_data2.csv")

output_path = os.path.join("output", "employees.csv")


def remap_data(my_csv_path):

    with open(my_csv_path, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        new_employees = []

        next(csv_reader, None)

        for row in csv_reader:
            first_name = row[1].split(" ")[0]
            last_name = row[1].split(" ")[1]
            parse_date_year = row[2].split("-")[0]
            parse_date_month = row[2].split("-")[1]
            parse_date_day = row[2].split("-")[2]
            new_date_format = f"{parse_date_month}/{parse_date_day}/{parse_date_year}"
            masked_ssn = f"***-**-{row[3].split('-')[2]}"
            lookup_state = us_state_abbrev[row[4]]

            new_employee = ({
                "Emp ID": row[0],
                "First Name": first_name,
                "Last Name": last_name,
                "DOB": new_date_format,
                "SSN": masked_ssn,
                "State": lookup_state
            })
            new_employees.append(new_employee)

    return new_employees


def update_csv_file(remapped_employee_data):
    with open(output_path, "w", newline="") as outputfile:
        fieldnames = [
            "Emp ID",
            "First Name",
            "Last Name",
            "DOB",
            "SSN",
            "State"
        ]
        writer = csv.DictWriter(outputfile, fieldnames)
        writer.writeheader()
        writer.writerows(remapped_employee_data)


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


def main():
    """main function."""
    new_employees_data = remap_data(my_csv_path_1)
    update_csv_file(new_employees_data)


if __name__ == "__main__":
    main()
