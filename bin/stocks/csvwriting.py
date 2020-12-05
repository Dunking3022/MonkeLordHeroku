import csv
import datetime
import random
stock = 10
filename = input()
with open(filename,'w+') as csvfile:
    a = datetime.datetime( day = 1,month = 11,year = 2020, hour = 0)
    forout = a.strftime('%d/%m/%y %H:%M:%S')
    a.strftime('%d/%m/%y %H:%M:%S')
    print(a)
    handle = csv.writer(csvfile)
    j = "YO"
    i = 0
    for _ in range(720*2):
        handle.writerow((str(forout),stock))
        print(a,stock)
        a = a + datetime.timedelta(hours = 12)
        forout = a.strftime('%d/%m/%y %H:%M:%S')
        stock += random.randint(-10,10)