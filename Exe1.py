import datetime
from datetime import time
 
 
d1 = datetime.date(2021, 1, 1)
d2 = datetime.date(2021, 7, 31)
d3 = datetime.date(1990, 5, 7)
t1  = time(12,00,00)
t2 = time(6,30,00)
t3 = time(9,15,00)
dt = datetime.datetime(2020, 6,20,11,30,00)
date1 = datetime.date(2020, 7, 21)
date2 = datetime.date(2020, 12, 31)
num_of_days = (date2 - date1).days
 
print(d1,"\t",t1)
print(d2,"\t",t2)
print(d3,"\t",t3)
print(dt)
print("Number of days between date :{} and date :{} is : {} days".format(date1, date2, num_of_days))