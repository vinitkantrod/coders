no = raw_input()
a = []
x = raw_input().split()[:int(no)]
for i in x:
    count = 0
    i=int(i)
    while i!=1:
        if i%2 == 0:
            i = i/2
            count=count+1
        else:
            i = i*3 +1
            count= count+1
    a.append(count)
print(' '.join((str(e)) for e in a))
