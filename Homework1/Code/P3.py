import  random
import numpy as np

n = 500     # 采样次数
vol = 0     # 体积
list = []   # 用于存储每轮结果的元组
e = 2.71828 # 自然常数

for i in range(0,100):  # 重复100次
    for ii in range(0,n):   # 每轮采样n个
        x = random.uniform(2,4) # 随机x坐标
        y = random.uniform(-1,1)# 随机y坐标
        xS = pow(x, 2)
        yS = pow(y,2)
        # 大致计算体积(底面积x高)
        vol += 2*2 * ((yS * pow(e,-yS) + xS*xS * pow(e,-xS))/ (x*pow(e,-xS)))

    list.append(vol/float(n))   # 将得到的积分值放入元组内
    vol = 0

print(np.mean(list))    # 均值
print(np.var(list))     # 方差