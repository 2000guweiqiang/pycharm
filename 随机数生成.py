#随机整数：
import random
x=random.randint(0,1000)#random.randint(a,b)用于生成一个指定范围内的整数
print(x)

#随机偶数：
import random
x=random.randrange(0,1000,2)#random.randrange()方法返回指定递增基数集合中的一个随机数,基数缺省值为1
print(x)

#随机浮点数
import random
x=random.uniform(1,3)
print(x)
import random
x=random.random()
print(x)