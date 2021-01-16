import os, csv

csvpath = 'election_data.csv'
with open(csvpath, 'r') as csvfile:
    # Split  data at commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Declare variables
    tvotes = 0
    vdata= []
    # Loop through the data
    next(csvreader)
    for r in csvreader:
        # Total Number of months included in Dataset
        tvotes =+1
        vdata.append(r)
        # if wstlrname == r[0]: #name of the wrestler
        #    print(wstlrname)
        #    prt_pctg(r) #list
        ##print(r)


# The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

 #The greatest decrease in losses (date and amount) over the entire period