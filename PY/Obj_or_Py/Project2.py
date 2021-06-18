import csv, os
print(os.getcwd())
with open('/Users/ims_schulacc/Desktop/Python_School/PY/Obj_or_Py/email-password-recovery-code.csv') as file:
    reader = csv.reader(file, delimiter=";")
    for content in reader:
        #print(content[1])
        if content[1] == '9346':
            for values in content:
                print(values)