import csv

with open('data.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    list = []
    for row in reader:
        list.append(dict(row))
    print(list)