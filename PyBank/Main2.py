# Import Dependencies
import os, csv
# Data Source
csvpath = os.path.join('Resources', 'budget_data.csv')
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
	        #change between each month profit/loss
        	profit = int(r[1]) - pmonth
            #net total amount of "Profit/Losses" over the entire period and used to calulate avg change
        	n_profit = n_profit + (int(r[1]) - pmonth) 
        	#The greatest increase in profits (date and amount) over the entire period
        	if profit > ginc_profit:
        		ginc_profit = profit
        		gminc = r[0]
        	#The greatest decrease in losses (date and amount) over the entire period
        	if profit < gdec_profit:
        		gdec_profit = profit
        		gmdec = r[0]
        else:
            pmonth = int(r[1])  #First loop prevmonth = curmonth
        #Update prevmonth for curmonth for next loop
        pmonth = int(r[1])
    # Average of Profit/Losses
    avgchng = n_profit/(tmonths-1)
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:  " + str(int(tmonths)))
    print("Total: $" + str(int(tprofit)))
    print("Average Change: $" + str(round(avgchng,2)))
    print("Greatest Increase in Profits: " + gminc + " ($" + str(int(ginc_profit)) + ")")
    print("Greatest Decrease in Profits: " + gmdec + " ($" + str(int(gdec_profit)) + ")")
csvpath = os.path.join('Resources', 'budget_data_output.csv'
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])"