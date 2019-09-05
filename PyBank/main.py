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
    dates = []
    profitloss_change = []

    for date, profitloss in bank_budget_data:
        sum_profit_loss += int(profitloss) # add each new "Profit/Loss" to the one before
        dates.append(date)  # use this to count the total number of months with len function in print statement
        change = int(profitloss) - int(prev_profitloss)
        profitloss_change.append(change)
        prev_profitloss = profitloss # put new profitloss into previous for the next iteration
        #print(str(date), int(profitloss), change)
    total_months = len(dates)
    max_increase = max(profitloss_change) # used below for boolean
    min_increase = min(profitloss_change)

    #Delete the first row because changes subtracted off the first row
    del dates[0] 
    del profitloss_change[0]

    #New list store change data
    new_bank_data = zip(dates, profitloss_change)
    sum_profitloss_change = 0

    #New lists to connect max value with month and min value with month
    max = []
    min = []

    for date, plchange in new_bank_data:
        sum_profitloss_change += plchange
        average_profitloss = sum_profitloss_change/(len(dates))
        if plchange == max_increase:
            max = [date, plchange]
        if plchange == min_increase:
            min = [date, plchange]
    max_date = str(max[0])
    max_change = int(max[1])
    min_date = str(min[0])
    min_change = int(min[1])
   

#Print data to terminal
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", total_months)
print("Total: $", str(sum_profit_loss))
print("Average Change: $", "{:.2f}".format(average_profitloss))
print("Greatest Increase in Profits: ", max_date, "($", max_change,")")
print("Greatest Decrease in Profits: ", min_date, "($", min_change,")")

#Print data to file
with open('output.txt', 'w') as file:
    print("Financial Analysis", file=file)
    print("-------------------------------", file=file)
    print("Total Months: ", total_months, file=file)
    print("Total: $", str(sum_profit_loss), file=file)
    print("Average Change: $", "{:.2f}".format(average_profitloss), file=file)
    print("Greatest Increase in Profits: ", max_date, "($", max_change, ")", file=file)
    print("Greatest Decrease in Profits: ", min_date, "($", min_change, ")", file=file)