import csv
with open('output.csv','r') as filename:
    for line in filename:
        print(line.strip())