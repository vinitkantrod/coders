a = int(raw_input())
b,c = raw_input().split()
c=int(c)
while b != '%':
    if b == '+':
        a = a + c
    elif b == '-':
        a = a - c
    elif b == '*':
        a = a * c
    elif b == '/':
        a = a / c
    b,c = raw_input().split()
    c=int(c)
a = a % c
print a
    
