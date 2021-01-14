{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Dependencies\n",
    "import os, csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<module 'ntpath' from 'C:\\\\ProgramData\\\\Anaconda3\\\\lib\\\\ntpath.py'>\n",
      "budget_data.csv\n"
     ]
    }
   ],
   "source": [
    "# Data Source\n",
    "#csvpath = os.path.join('Resources','budget_data.csv')\n",
    "csvpath = ('budget_data.csv')\n",
    "print(os.path)\n",
    "print(csvpath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'budget_data.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-112128f11a31>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Open data source\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsvpath\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mcsvfile\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m    \u001b[1;31m# Split  data at commas\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m    \u001b[0mcsvreader\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcsv\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcsvfile\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdelimiter\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m','\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'budget_data.csv'"
     ]
    }
   ],
   "source": [
    " #Open data source\n",
    "with open(csvpath) as csvfile:\n",
    "    # Split  data at commas\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    \n",
    "    #declare variables\n",
    "    tmonths = 0\n",
    "    tprofit = 0\n",
    "    ginc_profit = 0\n",
    "    gdec_profit = 0\n",
    "    n_profit = 0\n",
    "    profit = 0\n",
    "    comp_profit = 0\n",
    "    pmonth = 0\n",
    "\n",
    "\n",
    "    # Next line Skips Header Row\n",
    "    next(csvreader)\n",
    "\t# Loop through the data\n",
    "    for r in csvreader:\n",
    "    \t\n",
    "        # Total Number of months included in Dataset\n",
    "        tmonths += 1\n",
    "        # The net total amount of \"Profit/Losses\" over the entire period\n",
    "        tprofit = tprofit + int(r[1])\n",
    "        # The net total amount of \"Profit/Losses\" over the entire period\n",
    "        #change between each items\n",
    "        #prevmonth\n",
    "        #curmonth\n",
    "        #on row 1 prevmonth = curmonth  B2 = B2\n",
    "        #change = curmonth - prevmonth \n",
    "        # if profit != 0:\n",
    "        n_profit = n_profit + int(r[1])\n",
    "        # else:\n",
    "        #profit = int(r[1]) - int(r[1])\n",
    "        #n_profit = n_profit + profit\n",
    "\t\t#Calculate the changes in \"Profit/Losses\" over the entire period, then find the average of those changes\n",
    "\n",
    "\t\t#The greatest increase in profits (date and amount) over the entire period\n",
    "\n",
    "\t\t#The greatest decrease in losses (date and amount) over the entire period\n",
    "\t\t#comp_profit\n",
    "        print(tmonths)\n",
    "        print(tprofit)\n",
    "        \n",
    "        # print(profit)\n",
    "        print(n_profit)\n",
    "\n",
    "# The net total amount of \"Profit/Losses\" over the entire period\n",
    "\n",
    "#Calculate the changes in \"Profit/Losses\" over the entire period, then find the average of those changes\n",
    "\n",
    "#The greatest increase in profits (date and amount) over the entire period\n",
    "\n",
    " #The greatest decrease in losses (date and amount) over the entire period\n",
    "\n",
    " #change between each items\n",
    " #sum changes\n",
    " #Total number of changes\n",
    " #divide sum by total changes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
