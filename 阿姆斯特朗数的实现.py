#判断是否为阿姆斯特朗数：
num=int(input("请输入一个数:"))
sum=0
n=len(str(num))
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if sum==num:
    print(num,"是阿姆斯特朗数")
else: print("不是阿姆斯特朗数")
#输出阿姆斯特朗数：
Da=int(input("请输入最大值:"))
Xiao=int(input("请输入最小值:"))
for num in range(Xiao,Da):
    sum=0                 #初始化sum
    n=len(str(num))       #  指数
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**n
        temp//=10
    if sum==num:
        print(num)