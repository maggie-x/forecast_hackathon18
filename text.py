
import os.path
import csv

magic = 'out'

if not os.path.exists(os.path.join(magic+'.csv', magic.strip())):
    if not os.path.exists(magic+'.csv'):
        
        l = ['hello','how','are','you']

        with open("out.csv","w") as f:
            wr = csv.writer(f,delimiter="\n")
            wr.writerow(l)