b=[38,95,1,63,654,46,78,26,11,25,3,66,84,45,8,23,79,100]
low=b[0]
high=b[17]
num=int(input("请输入数字:"))
if num in b:
    while True:
        arr=int((low+high)/2)
        if num==arr:
            print("存在此数字")
            break
        elif num>arr:
            low=arr+1
        elif num<arr:
            high=arr-1
else:
    print("无该数字")
