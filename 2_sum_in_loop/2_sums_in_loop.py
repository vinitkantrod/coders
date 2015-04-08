noi = raw_input()
no = int(noi)
sum = []
for i in range(no):
    s=0
    a,b = raw_input().split(' ')
    print i
    a=int(a)
    b=int(b)
    s = a+b
    sum.append(s)
print(" ".join(str(x) for x in sum))

