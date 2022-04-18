#求算pi
from random import *
from math import sqrt
dots = eval(input("请输入点数目："))
ans = 0
for i in range(dots):
    x,y = random(),random()
    dis = sqrt(x**2+y**2)
    if dis<=1.0:
        ans = ans+1
pi = 4 * (ans/dots)
print(pi)
