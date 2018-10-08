import os, time
from datetime import *

today = str(date.today())
print(today[-1])

print(int(today[-1]) % 2)

now = datetime.now()
now_format = now.strftime("%Y-%m-%d %H:%M:%S")
print(now_format)

