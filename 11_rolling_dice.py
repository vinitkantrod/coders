import random
import math
a = []
no = raw_input()
for i in range(int(no)):
    r=raw_input()
    r = float(r)
    r = r*6
    r = math.floor(r)
    r = int(r)
    a.append(r+1)
print(' '.join((str(e)) for e in a))
