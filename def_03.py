from random import randint

ko = randint(1,100)
eng = randint(1,100)
math = randint(1,100)


def total(ko, eng, math):
    return ko + eng + math

print(total(ko, eng, math))
print(total(ko, eng, math)/3)

#%%

def total(k, e , m):
    return k + e + m

def average(tot, cnt):
    return(tot / cnt)

tot = total(70,80,90)
avg = average(tot, 3)

print('총점:', tot)
print('평균: ', avg)


#%%
