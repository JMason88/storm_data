import io
from urllib import request
import csv


response = request.urlopen('https://dq-content.s3.amazonaws.com/251/storm_data.csv')
reader = csv.reader(io.TextIOWrapper(response))

writer = csv.writer(open("storm_data.csv", "w"))
for row in reader:
    writer.writerow(row)
