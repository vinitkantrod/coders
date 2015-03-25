no = raw_input()
v = []
for i in range(int(no)):
    a,b = raw_input().split()
    b = float(b)
    a = float(a)
    bmi = a/b**2
    if bmi < 18.5:
        v.append("under")
    elif bmi >= 18.5 and bmi < 25.0:
        v.append("normal")
    elif bmi >= 25.0 and bmi < 30.0:
        v.append("over")
    else:
        v.append("obese")
        
print(' '.join(v))
