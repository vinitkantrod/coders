
v = []
n=raw_input()
n=int(n)

for i in range(n):
        temp = []
        a,b,c = raw_input().split()
        temp.append(a)
        temp.append(b)
        temp.append(c)
        temp = list(map(int,temp))
        temp.sort()
        v.append(temp[1])

print(" ".join((str(e)) for e in v))
