from datetime import datetime
from datetime import date
import time as t

today = date.today()

now = datetime.now()
print("Today's date:", today)

while True:
  t.sleep(1)
  current_time = now.strftime("%H:%M:%S")
  print("Current Time =", current_time)


