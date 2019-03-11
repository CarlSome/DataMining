import  random
import numpy as np

n = 5000    # 重复次数
r = 1.0     # 圆的半径
count = 0   # 随机点落在圆内的次数
list = []   # 用于存储每轮结果的元组

for i in range(0,20):   # 重复20次
    for ii in range(0,n):   # 每次取样n个
        x = random.uniform(0,1) # 随机x坐标
        y = random.uniform(0,1) # 随机y坐标
        if x*x + y*y <= 1.0:    # 根据坐标判断是否在圆内
            count += 1

    list.append((count/float(n)) * 4)   # 计算一次π，存入元组
    count = 0

print(np.mean(list))    # 均值
print(np.var(list))     # 方差

