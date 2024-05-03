import datetime
 
dt1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
dt2 = datetime.datetime(2021, 2, 20, 10, 25, 0)
"""
Desired formats:

2021-04-20
20-04-2021
04-2021
April-2021
20 April, 2021
2021-04-20 11:30:00
04/20/21 11:30:00
20(Tue) April 2021
"""
date1 = datetime.datetime(2021,4,20,11,30,0)
formats = ["%Y-%m-%d", "%d-%m-%Y", "%m-%Y", "%B-%Y", "%d %B, %Y", "%Y-%m-%d %H:%M:%S", "%m/%d/%y %H:%M:%S", "%d(%a) %B %Y"]
results = []

for format_str in formats:
    str_format = date1.strftime(format_str)
    results.append(str_format)

""" Using Now the strptime() Methode"""


date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'
 
dt1 = datetime.datetime.strptime(date_str_1, '%d %B %Y')
dt2 = datetime.datetime.strptime(date_str_2, '%d/%m/%Y')
dt3 = datetime.datetime.strptime(date_str_3, '%d-%m-%Y')
 
print(dt1)
print(dt2)
print(dt3)
print(dt2 - dt1)
print(results)