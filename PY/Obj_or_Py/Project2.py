import csv, os
print(os.getcwd())
with open('/Users/ims_schulacc/Desktop/Python_School/PY/Obj_or_Py/email-password-recovery-code.csv', 'r') as file:
    reader = csv.reader(file)
    for content in reader:
        if content == "9012":
            for x in content:
                print()