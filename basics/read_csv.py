
file = open("basics/basic_csv.csv","r")
file_arr = []
for x in file:
    file_arr.append(x.split())
print(file_arr)


import csv
with open("basics/basic_csv.csv", "r") as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)