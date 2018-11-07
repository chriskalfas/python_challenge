import os
import csv
csvpath=os.path.join("documents","resources","budget_data.csv")

#translate csv into readable file WITH integers column for P&L
with open(csvpath) as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    header = next(readcsv)

#Create variables and open ranges for data
    total = 0
    dates = []
    pls = []
    
#Create for loop to append count and sum
    for row in readcsv:
        date = row[0]
        pl = int(row[1])
        dates.append(date)
        pls.append(pl)
        
    print("Financial Analysis")
    print("------------------------------------")
        
    time_cnt = len(dates)
    print("Amount of time: " + str(time_cnt) + " months.")
        
    pls_sum = sum(pls)
    print("Total profit and losses: $" + str(pls_sum))
    
    avg_chg = (pls_sum/time_cnt)
    print("Average change in profit and loss/month: $" + "%.2f" % round(avg_chg,2))
    
    max_inc = max(pls)
    print("Largest increase in a month: $" + str(max_inc))
    
    max_dec = min(pls)
    print("Largest decrease in a month: $" + str(max_dec))