import random
notenlist = []

for x in range(20):
  note = random.uniform(1, 6)
  note = round(note, 1)
  notenlist.append(note)

print(sorted(notenlist))

