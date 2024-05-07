import csv 
import os 


path = "C:\\Users\\Lenovo\\Documents\\Students.csv"
with open(path, 'r', encoding="utf-8") as file:
    rows = csv.reader(file, delimiter=",")
    headers = next(rows)
    print(f"The header: {headers}")
    for row in rows:
        print(row)

""" Create a csv file in """

headers = ["Date", "Open", "High", "Low", "Close", "Volume"]
apple = [
    [
        "1984-09-07",
        "0.4158",
        "0.4208",
        "0.4107",
        "0.4158",
        "23669718",
    ],
    [
        "1984-09-10",
        "0.4158",
        "0.4170",
        "0.4058",
        "0.4133",
        "18371562",
    ],
    [
        "1984-09-11",
        "0.4170",
        "0.4283",
        "0.4170",
        "0.4208",
        "43321235",
    ],
]

dir_csv = "Files_csv"

def create_csv(path = "C:\\Users\\Lenovo"):

    if not os.path.exists(dir_csv):
        path = os.path.join(path, dir_csv)
        os.mkdir(path)
        os.chdir(path)

    with open('names.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        writer.writerows(apple)
        print("File has been created Successfully!")

create_csv()

    


