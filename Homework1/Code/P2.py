import  random
import numpy as np

n = 100     # 重复次数
count = 0   # 随机点落在范围内的次数
list = []   # 用于存储每轮结果的元组

for i in range(0,100):  # 重复100次
    for ii in range(0,n):   # 每次取样n个
        x = random.uniform(0,1) # 随机x坐标
        y = random.uniform(0,1) # 随机y坐标
        if x * x * x > y:   # 根据随机坐标判断随机点是否在范围内
           count += 1

    list.append(count/float(n)) # 将得到的积分值放入元组内
    count = 0

print(np.mean(list))    # 均值
print(np.var(list))     # 方差

