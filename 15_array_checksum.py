no = raw_input()
a = []
inp = raw_input().split()[:int(no)]
inp = map(int,inp)
r=0
for j in inp:
    r += j
    r = (r*113)%10000007

print r
