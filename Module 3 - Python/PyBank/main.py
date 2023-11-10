import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    print(type(csvreader))

    csv_header = next(csvreader)

    total_profit = 0
    count_of_rows = 0
    month = []
    profit_difference = []
    
    # All interation over the csv.reader file needs to be done in the same for loop as it can only be iterated over once.
    for row in csvreader:
        total_profit += int(row[1])
        count_of_rows += 1
        if row[0] == "Jan-10":
            month.append(row[0])
            profit_start = int(row[1])
            last_month = profit_start
        elif row[0] == "Feb-17":
            month.append(row[0])
            profit_end = int(row[1])
            new_month = int(row[1]) - last_month #@TODO Need to figure out how to get the difference in profit
            profit_difference.append(new_month)
            last_month = int(row[1])
        else:
            month.append(row[0])
            new_month = int(row[1]) - last_month #@TODO Need to figure out how to get the difference in profit
            profit_difference.append(new_month)
            last_month = int(row[1])
        
    max_month = month[profit_difference.index(max(profit_difference)) + 1]
    min_month = month[profit_difference.index(min(profit_difference)) + 1]
    
    output_file = ["Financial Analysis", "----------------------------", f'Total Months: {count_of_rows}', \
        f'Total: {total_profit}', f'Average Change: ${round((profit_end - profit_start)/(count_of_rows - 1), 2)}', \
        f'Greatest Increase in Profits: {max_month} (${max(profit_difference)})', \
        f'Greatest Decrease in Profits: {min_month} (${min(profit_difference)})']

    output_path = os.path.join("Analysis", "pybank.txt")

    with open(output_path, "w") as pybank:
        for string in output_file:
            print(string)
            pybank.write(string)
            pybank.write('\n')
    


#    print("Financial Analysis")
#    print("----------------------------")
#    print(f'Total Months: {count_of_rows}')
#    print(f'Total: {total_profit}')
#    print(f'Average Change: ${round((profit_end - profit_start)/(count_of_rows - 1), 2)}')
#    print(f'Greatest Increase in Profits: {max_month} (${max(profit_difference)})')
#    print(f'Greatest Decrease in Profits: {min_month} (${min(profit_difference)})')