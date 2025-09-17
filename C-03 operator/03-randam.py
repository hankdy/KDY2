from random import random, randint, randrange
from math import *


# 랜덤 (random) : 난수

# 0이상 1미만의 실수인 난수 생성
# # 0 <= random() < 1
# r = random()
# print(r)

# # %%
# 문제
# 1부터 6까지의 난수를 발생 시켜라.

r = randrange(1, 7,)

print(r)


# #%%

# rn = random()
# print(rn)

# rf = rn * 6
# print(rf)

# rx = floor(rn*6)
# print(rx)

# sx = rx + 1
# print(sx)

# #%%

# t = random()
# print(t)

# tt = t * 11
# print(tt)

# ti = floor(tt)
# print(ti)

# tc = ti + 10
# print(tc)

#%%
r = randint(10,20)
print(r)



#%%

rmin = 10
rmax = 20
rx = rmax - rmin + 1
rn = random()
rt = rn * rx + rmin
rr = floor(rt)

print("최솟값:" , rmin)
print("최대값:" , rmax)

print("난수값: " , rn)
print("최종값: ", rt)

print("보정값:" , rr)
