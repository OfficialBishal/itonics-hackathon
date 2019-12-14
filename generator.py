import csv
from random import *

feildnames=['curiculum','Athletic']
writer=csv.DictWriter(open('data/students.csv','w'),fieldnames=feildnames)

i=0
writer.writerow(dict(zip(feildnames,feildnames)))
while(i<3):
    value1=uniform(0,1)
    value2=uniform(0,1)
    writer.writerow(dict([
        ('curiculum',value1)
        #('Athletic',value2)
    ]))
while(i<3):
    value1=uniform(0,1)
    value2=uniform(0,1)
    writer.writerow(dict([
        ('athletic ',value2)
        #('Athletic',value2)
    ]))