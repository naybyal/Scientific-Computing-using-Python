import csv

with open('contributors.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
