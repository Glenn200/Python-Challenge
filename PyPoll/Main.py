#references
#https://www.numpyninja.com/post/how-to-format-strings-using-print-in-python
#https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
#https://stackoverflow.com/questions/27633976/updating-list-with-a-for-loop
#https://stackoverflow.com/questions/4081217/how-to-modify-list-entries-during-for-loop
#https://tutorialdeep.com/knowhow/loop-over-python-list-variable/
#https://stackoverflow.com/questions/14819849/create-lists-of-unique-names-in-a-for-loop-in-python

#Dependencies
import os, csv

# Data pathe and file name
csvpath = os.path.join('Resources', 'election_data.csv')

#Declare variables
tvotes = 0
cvotes = []
cands = []
#create a variable to hold the voting information, name and number of votes
with open(csvpath, 'r') as csvfile:
    # Split  data at commas
    reader = csv.reader(csvfile, delimiter = ',')
    # Loop through the data skipping header row
    next(reader)
    for r in reader:
        tvotes += 1
        if r[2] in cands:
            #If candidate in list increment vote for candidate
            cvotes[cands.index(r[2])] += 1
        else:
            # Add Candidates not in list and initalize first vote
            cands.append(r[2])
            cvotes.append(1)          
# Output to Console
print("---------------------------------------")
print("Election Results")   
print("---------------------------------------")
print("Total Votes :" + str(tvotes))    
print("---------------------------------------")
for i in range(len(cands)):
    print(cands[i] + ': ' + '%.2f'%(cvotes[i] / tvotes*100) + '% (' + str(cvotes[i]) + ')')
#+ ")")#+ ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("---------------------------------------")
print("The winner is: " + cands[cvotes.index(max(cvotes))])
print("---------------------------------------")

#output to text file.
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(tvotes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(cands)):
        text.write(cands[i] + ': ' + '%.2f'%(cvotes[i] / tvotes*100) + '% (' + str(cvotes[i]) + ')\n')
    text.write("---------------------------------------\n")
    text.write("The winner is: " + cands[cvotes.index(max(cvotes))] + "\n")
    text.write("---------------------------------------\n")