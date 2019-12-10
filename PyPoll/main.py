#modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

#lists to store data
voter = []
candidates = []
vote_count = []
election_data = ['1', '2']


#open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    #For loop through rows and save data to list
    for row in csvreader:

        #include candidate name and voter for total count
        voter.append(float(row[0]))
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_count.append(1)


        
#calculate total votes
total_votes = len(voter)
percentages = []
maxvotes = vote_count[0]
maxindex = 0

#create for loop to determinate percentages and winner
for count in range(len(candidates)):
    vote_percentage = vote_count[count]/total_votes * 100
    percentages.append(vote_percentage)
    if vote_count[count] > maxvotes:
        maxvotes = vote_count[count]
        maxindex = count

#identify winner
winner = candidates[maxindex]

#calculate percentages
percentages = [round(i, 2) for i in percentages]


print("Election Results")

print("-------------------------")

print(f"Total Votes: {total_votes}")

print("-------------------------")

for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")

print("-------------------------")

print(f"Winner: {winner}")

print("-------------------------")

#export a text file with results
f = open("pypoll.txt", "w")

#write results to text file
f.write("Election Results")
f.write("\n----------------------")
f.write(f"\nTotal Votes: {total_votes}")
f.write("\n----------------------")
for count in range(len(candidates)):
    f.write(f"\n{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
f.write("\n----------------------")
f.write(f"\nWinner: {winner}")
f.write("\n----------------------")

f.close()