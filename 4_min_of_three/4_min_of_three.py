noi = raw_input()
no = int(noi)
min = []
for i in range(no):
    a,b,c = raw_input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a<b:
        if a<c:
            min.append(a)
        else:
            min.append(c)
    elif b<c:
        min.append(b)
    else:
        min.append(c)
print(' '.join(str(x) for x in min))
