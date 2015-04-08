import math

noi = raw_input()
no = int(noi)
div=[]
for i in range(no):
    a,b = raw_input().split()
    d= float(a)/float(b)
    d=round(d)
    div.append(int(d))
print(' '.join(str(x) for x in div))
