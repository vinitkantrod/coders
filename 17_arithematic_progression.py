no = raw_input()
v = []
for i in range(int(no)):
    a,b,n = raw_input().split()
    a = int(a)
    aa = a
    b = int(b)
    n = int(n)
    nadd = 0
    for i in range(n):
        add = aa + (i*b)
        nadd += add
    v.append(nadd)
print(' '.join((str(e)) for e in v))
    
