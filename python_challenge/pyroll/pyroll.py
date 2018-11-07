import os
import csv
csvpath=os.path.join("documents","resources","election_data.csv")
#translate csv into readable file 
with open(csvpath) as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    header = next(readcsv)
#Create variables and open ranges for data
    total = 0
    votes = []
    candidates = []
#Create for loop to append count 
    for row in readcsv:
        vote = row[0]
        candidate = row[2]
        votes.append(vote)
       
    print("Election Results")
    print("------------------------------------")
        
    num_votes = len(votes)
    print("Number of Votes: " + str(num_votes))
    print('------------------------------------')