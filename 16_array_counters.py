import collections
aaa = []

no,rang = raw_input().split()
arr = raw_input().split()[:int(no)]
a = dict((i,arr.count(i)) for i in arr)
aa = (a.keys()
ab = aa.sort()
print ab
for key in ab:
    aaa.append(a[key])
print(' '.join((str(e)) for e in aaa))
