import csv

# Data to be written to CSV
data = [
    ["SN", "Name", "Country", "Contribution", "Year"],
    [1, "Linus Torvalds", "Finland", "Linux Kernel", 1991],
    [2, "Tim Berners-Lee", "England", "World Wide Web", 1990],
    [3, "Guido van Rossum", "Netherlands", "Python", 1991]
]

# Specify the filename
filename = "contributors.csv"

# Writing to CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Writing the data
    writer.writerows(data)

print(f"Data has been written to {filename}")


