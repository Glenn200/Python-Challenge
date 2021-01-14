
import os, csv

# Data Source
csvpath = os.path.join('Resources', 'budget_data.csv')

budget = []
with open(csvpath) as csvfile:
    # Split  data at commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #declare variables
    tmonths = 0
    tprofit = 0
    ginc_profit = 0
    gdec_profit = 0
    n_profit = 0
    profit = 0
    comp_profit = 0
    pmonth = 0


    # Next line Skips Header Row
    next(csvreader)
	# Loop through the data
    for r in csvreader:
    	
        # Total Number of months included in Dataset
        tmonths += 1
        # The net total amount of "Profit/Losses" over the entire period
        tprofit = tprofit + int(r[1])
        # The net total amount of "Profit/Losses" over the entire period
        #change between each items
        #prevmonth
        #curmonth
        #on row 1 prevmonth = curmonth  B2 = B2
        #change = curmonth - prevmonth 
        # if profit != 0:
        n_profit = n_profit + int(r[1])
        # else:
        #profit = int(r[1]) - int(r[1])
        #n_profit = n_profit + profit
		#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

		#The greatest increase in profits (date and amount) over the entire period

		#The greatest decrease in losses (date and amount) over the entire period
		#comp_profit
        print(tmonths)
        print(tprofit)
        
        # print(profit)
        print(n_profit)

# The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

 #The greatest decrease in losses (date and amount) over the entire period

 #change between each items
 #sum changes
 #Total number of changes
 #divide sum by total changes
