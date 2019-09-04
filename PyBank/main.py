import os
import csv

bank_data_csv = os.path.join("/Users/dianeshomefolder/Documents/Code/UA Bootcamp Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")

# Open and read csv
with open(bank_data_csv, newline="") as file_object:
    bank_budget_data = csv.reader(file_object, delimiter = ',')

    # Read the header row first
    bank_budget_header = next(bank_budget_data)
    print(f"Bank Budget Header: {bank_budget_header}")

    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    #for line in bank_data_header:
        #print(row)
