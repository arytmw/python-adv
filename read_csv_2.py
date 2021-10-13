import csv

filename = input("Enter CSV file to read: ")

file_content = open(filename,'r')

csvfile = csv.DictReader(file_content)

for line in csvfile:
    print(line)
