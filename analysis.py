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

    #print(csv_values_dates)
    #print(csv_values_perc)
    positive_ones = []
    negative_ones = []

    weeks_duration = 104
    coefficient = 1
    total = 0
    counter = 0
    max = 0
    min = 1000000000000
    listSize = len(csv_values_dates)
    for x in range(0,listSize - weeks_duration):
        difference = (float(csv_values_perc[x+weeks_duration].replace("'","").replace(',','.'))-float(csv_values_perc[x].replace("'","").replace(',','.')))/float(csv_values_perc[x].replace("'","").replace(',','.'))
        total = total + difference
        if (difference > max):
            max = difference
        if (difference < min):
            min = difference
        counter = counter +1
        #print("date" + csv_values_dates[x] + " diff: " + str(difference))
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




print('Usa')
USAINDEX = normalize_values("./LP68022608 Historiska data.csv")
print('Europa')
EUROPAINDEX = normalize_values("./0P0000KBNA Historiska data.csv")
print('Avanza')
AVANZAINDEX = normalize_values("./0P0001ECQR Historiska data.csv")
print('Nordnet')
NORDNETINDEX = normalize_values("./0P0001K6NH Historiska data.csv")
print('Global')
GLOBALINDEX = normalize_values("./0P0000YVZ3 Historiska data.csv")
print('Japan')
JAPANINDEX = normalize_values("./0P00000L2Y Historiska data.csv")





        
