# Modules
import os
import csv
import statistics

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#lists to store data
date = []
profitloss = []

#open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    #For loop through rows
    for row in csvreader:
        profitloss.append(int(row[1]))
        date.append(str(row[0]))

#calculate difference in P&L
change = [x-y for x,y in zip(profitloss[1:], profitloss)]

#total amount of months
total_months = len(date)

#calculate amounts needed to create financial analysis
netTotal = sum(profitloss)
avgChange = round(statistics.mean(change), 2)

#Find maximum change value and date
maxincome = max(change)
maxindex = change.index(maxincome)
maxdate = date[maxindex + 1]

#Find minimum change value and date
minincome = min(change)
minindex = change.index(minincome)
mindate = date[minindex + 1]

#calculate total number of months in data set
total_months = len(date)

print("Financial Analysis")

print("-----------------------------")

print(f"Total Months: {total_months}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${avgChange}")
print(f"Greatest Increase in Profits: {maxdate} ({maxincome})")
print(f"Greatest Decrease in Profits: {mindate} ({minincome})")

#export a text file with results

#export a text file with results
f = open("pybank.txt", "w")

#write results to text file
f.write("Financial Analysis")

f.write("\n----------------------")

f.write(f"\nTotal Months: {total_months}")
f.write(f"\nTotal: ${netTotal}")
f.write(f"\nAverage Change: ${avgChange}")
f.write(f"\nGreatest Increase in Profits: {maxdate} ({maxincome})")
f.write(f"\nGreatest Decrease in Profits: {mindate} ({minincome})")

f.close()

    
    
     
