import csv

with open('contributors.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
