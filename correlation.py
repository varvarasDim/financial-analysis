import csv
import datetime
from datetime import datetime, timedelta
import pandas as pd



def normalize_values(filename):
    csv_values_dates = []
    csv_values_perc = []

    with open(filename, 'r') as file:
        csvreader = csv.reader(file,  delimiter=',')
        for row in csvreader:
                if row[1] == 'Senaste':
                    continue
                else:
                    csv_values_dates.append(row[0])
                    csv_values_perc.append(row[1])

    csv_values_perc.reverse()
    csv_values_dates.reverse()

    print(csv_values_dates)
    print(csv_values_perc)
    positive_ones = []
    negative_ones = []

    coefficient = 1
    total = 0
    counter = 0
    max = 0
    min = 1000000000000
    listSize = len(csv_values_dates)
    for x in range(0,listSize - 104):
        difference = (float(csv_values_perc[x+104].replace("'","").replace(',','.'))-float(csv_values_perc[x].replace("'","").replace(',','.')))/float(csv_values_perc[x].replace("'","").replace(',','.'))
        total = total + difference
        if (difference > max):
            max = difference
        if (difference < min):
            min = difference
        counter = counter +1
        print("date" + csv_values_dates[x] + " diff: " + str(difference))
        if difference>=0:
             positive_ones.append(str(csv_values_dates[x]) + " " + str(difference))
        else:
             negative_ones.append(str(csv_values_dates[x]) + " " + str(difference))
            
             
    print("Positive #:" + str(len(positive_ones)))
    print("Negative #:" + str(len(negative_ones)))

    avg = total/counter
    print('AVG------------')
    print(avg)
    print('MAX------------')
    print(max)
    print('MIN------------')
    print(min)





USAINDEX = normalize_values("./LP68022608 Historiska data.csv")




        
