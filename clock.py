import time

while True:
  now = time.strftime("%c")
  print("current date and time ") + time.strftime("%c")
  time.sleep(1)