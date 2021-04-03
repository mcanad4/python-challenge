#import modules
import os
import csv

#path to file
csv_path = os.path.join('Resources','PyBank.csv')

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header_row = next(csvreader)

    months = sum(1 for line in csvfile)
    
    reader = csv.DictReader(csvfile)
    total = sum(int(row[1]) for row in reader)
#    print(total)

    average = total / months
#    print(average)

# output data to print once above functions work
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {months}")
    print(f"Total: {total}")
    print(f"Average Change: {average}")
#    print(f"Greatest Increase in Profit: {month_total}")
#    print(f"Greatest Decrease in Profit: {month_total}")