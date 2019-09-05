import os
import csv

bank_data_csv = os.path.join("/Users/dianeshomefolder/Documents/Code/UA Bootcamp Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")

# Open and read csv
with open(bank_data_csv, newline="") as file_object:
    bank_budget_data = csv.reader(file_object, delimiter = ',')

    # Read the header row first
    bank_budget_header = next(bank_budget_data)
    # print(f"Bank Budget Header: {bank_budget_header}") - used to check code

    # Read through each "Date" and "Profit/Loss" row after the header
    prev_profitloss = 0
    sum_profit_loss = 0
    num_months = []
    profitloss_change = []
    for date, profitloss in bank_budget_data:
        sum_profit_loss += int(profitloss) # add each new "Profit/Loss" to the one before
        num_months.append(date)  # use this to count the total number of months with len function in print statement
        change = int(profitloss) - int(prev_profitloss)
        profitloss_change.append(change)
        prev_profitloss = profitloss # put new profitloss into previous for the next iteration
        print(str(date), int(profitloss), change)
        

#Print data to terminal
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", len(num_months))
print("Total: $" + str(sum_profit_loss))
#print("Average Change: $", str(su)))
print("Greatest Increase in Profits: ", str(date), max(profitloss_change))
print("Greatest Decrease in Profits: ", str(date), min(profitloss_change))

