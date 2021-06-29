import csv

with open(r'test.csv', 'a', newline='') as csvfile:
    fieldnames = ['Record','Temperature']
    record = "rec2"
    temp = 32
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writerow({'Record':record, 'Temperature':temp})