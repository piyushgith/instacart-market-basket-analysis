#!/usr/bin/python
import csv
import random
import pandas as pd

start = pd.Timestamp.now()

records=9000000

print("Making %d records\n" % records)

fieldnames=['id','name','age','city','temp','remarks']
writer = csv.DictWriter(open("people.csv", "w", newline=''), fieldnames=fieldnames)

names=['Deepak', 'Sangeeta', 'Geetika', 'Anubhav', 'Sahil', 'Akshay']
cities=['Delhi', 'Kolkata', 'Chennai', 'Mumbai']
remarks=['Good','Excellent','outstanding','Cool']

writer.writerow(dict(zip(fieldnames, fieldnames)))
for i in range(0, records):
  writer.writerow(dict([
    ('id', i),
    ('name', random.choice(names)),
    ('age', str(random.randint(24,26))),
    ('city', random.choice(cities)),
    ('temp', ''),
    ('remarks', random.choice(remarks))    
    ]))
  
print('File has been created!! ')
# code
print(pd.Timestamp.now()-start)