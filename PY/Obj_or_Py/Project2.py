import csv
with open('/Users/ims_schulacc/Desktop/Python_School/PY/Obj_or_Py/eggs.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)