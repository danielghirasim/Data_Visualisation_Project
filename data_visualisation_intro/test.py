import csv

with open ('test.csv') as f:
    reader = csv.reader(f)
    headings = next(reader)


    for index,headings in enumerate(headings):
        print(index,headings)