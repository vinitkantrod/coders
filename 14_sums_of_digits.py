no = raw_input()
aa = []
for i in range(int(no)):
    a,b,c = raw_input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d = a*b+c
    sm=0
    e=int(d)
    for j in range(len(str(d))):
        r = int(e)%10
        e = e/10
        sm += r
    aa.append(sm)

print(' '.join((str(k)) for k in aa))
        
