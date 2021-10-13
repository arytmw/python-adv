import pandas # sudo pip3.6 install pandas

filename = input("Enter CSV file to read: ")

csvfile = pandas.read_csv(filename)
print(csvfile)
