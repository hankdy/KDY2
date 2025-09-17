a = 10
b = 3
f = a / b
print(f)

# 오차 발생 16자리 까지는 보정
# IEEE 754 규약


#%%

# 정수나누기 : //

a = 10
b = 3
c = 4
d = a // b
e = a & b
print(d) #3 몫을 표현
print(e) #1 나머지를 표현

#%%


m, n = divmod(a,c)
print("divmod({0}, {1}) -> 몫({2}), 나머지({3})".format(a,c,m,n))
