import os
import csv

election_data_csv = os.path.join('.', 'Resources', 'election_data.csv')
election_data_out = os.path.join('.', 'analysis', 'election_data.txt')


#init variables
total_votes = 0
candidates = []
popular_candidate = []
count_vote = []
percent_vote = []
candidates_votes = []

#open csv file
with open(election_data_csv) as in_file:
    reader = csv.reader(in_file)

    header = next(reader)

    row = next(reader)

    for i in range(len(set(popular_candidate))):
        print(popular_candidate[i] + ": " + str(percent_vote[i]) +"% (" + str(count_vote[i])+ ")")

    #Loop through rows
    for row in reader:

        #calculate total number of months       
        total_votes = total_votes + 1
        
        #setting candidates names to list
        candidates.append(row[2])

        #setting up unique candidates name
    for x in set(candidates):
        popular_candidate.append(x)

        #calculatind total number of votes per candidates
        v = candidates.count(x)
        candidates_votes.append(v)


        #getting the percent for the votes
        z = (v/total_votes)*100
        percent_vote.append(z)
    
    

winner_vote = max(candidates_votes)
winner = popular_candidate[candidates_votes.index(winner_vote)]
    
       

output = (
    f"Election Results\n"
    f"------------------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------------------------------\n"
    f"--------------------------------------------------\n"
    f"The winner is: {winner}\n"
    f"---------------------------------------------------"
)

print(output, end="")

with open(election_data_out,"w") as out_file:
    out_file.write(output)

