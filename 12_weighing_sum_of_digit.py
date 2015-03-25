no = raw_input()

a = []
n = ((raw_input().split()[:int(no)]))
n = map(int,n)
for i in n:
    i = str(i)
    h=0
    j=0
    for ch in i:
        h += int(ch)*(j+1)
        j = j+1
    a.append(h)
print(' '.join((str(e)) for e in a))
