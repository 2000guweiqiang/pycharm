for weight in range(1,40):
    m=s=n=1
    while(s<weight):
        m *= 3
        s += m
        n += 1
print("最少需要%d个砝码"%n)

last=0
a=[]
for weight in range(1,40):
    if(weight>=3*last):
        last = weight
        a.append(last)
print(a)

