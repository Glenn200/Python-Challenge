
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
    gminc = ""
    gmdec = ""
    gdec_profit = 0
    n_profit = 0
    profit = 0
    comp_profit = 0
    pmonth = 0
    avgchng = 0

    # Next line Skips Header Row
    next(csvreader)
	# Loop through the data
    for r in csvreader:
        # Total Number of months included in Dataset
        tmonths += 1
        # The net total amount of "Profit/Losses" over the entire period
        tprofit = tprofit + int(r[1])
        #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        if pmonth != 0:
        	
        	profit = int(r[1]) - pmonth
        	n_profit = n_profit + (int(r[1]) - pmonth) #change between each items
        	pmonth = int(r[1]) #set prevmonth for curmonth
        	#The greatest increase in profits (date and amount) over the entire period
        	if n_profit > ginc_profit:
        		ginc_profit = n_profit
        		gminc = r[0]
        	#The greatest decrease in losses (date and amount) over the entire period
        	if n_profit < gdec_profit:
        		gdec_profit = profit
        		gmdec = r[0]
        else:
            pmonth = int(r[1])  #First loop prevmonth = curmonth
            #ginc_profit = n_profit
            #gminc = r[0]
            #gdec_profit = n_profit
            #gmdec = r[0]
    avgchng = n_profit/(tmonths-1)
		#The greatest increase in profits (date and amount) over the entire period

		#
		#comp_profit

	# The net total amount of "Profit/Losses" over the entire period

	#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

	#The greatest increase in profits (date and amount) over the entire period

	#The greatest decrease in losses (date and amount) over the entire period
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:  " + str(int(tmonths)))
    print("Total: $" + str(int(tprofit)))
    #print(profit)
    print("Average Change: $" + str(round(avgchng,2)))
    print("Greatest Increase in Profits: " + gminc + " ($" + str(int(ginc_profit)) + ")")
    print("Greatest Decrease in Profits: " + gmdec + " ($" + str(int(gdec_profit)) + ")")
    
