n=int(input('n='))
m=int(input('m='))
p=0
t=0
r=0

if (n<m):
    t=n
    n=m
    m=t

p=n*m
while (m!=0):
    r=n%m
    n=m
    m=r

print ('最大公约数是:%d ' % (n))
print ('最小公倍数是:%d' % (p/n))