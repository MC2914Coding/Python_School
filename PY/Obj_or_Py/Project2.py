import csv
with open('/Users/ims_schulacc/Desktop/Python_School/PY/Obj_or_Py/email-password-recovery-code.csv', 'r') as file:
    reader = csv.reader(file)
    for content in reader:
        print(content, "\n")