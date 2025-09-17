a = []
# 리스트형
print(type(a), a)

#%%

b = [1,2,3]
c = ['a','b','c','d']
d = [1.0, 2.0, 3.14]


# 리스의 길이는 요소의 갯수

print(f"길이 :  {len(b)} : {b}")
print(f"길이 :  {len(c)} : {c}")
print(f"길이 :  {len(d)} : {d}")

#%%

e = ["홍길동" , 34, "조선"]

print(f"길이 :  {len(e)} : {e}")

#%%

ll = [1,3,5,[7,9],e]

print(f"길이 :  {len(ll)} : {ll}")

print(ll[0])
print(ll[1])
print(ll[2])
print(ll[3])
print(ll[4])

l3 = ll[3]
l4 = ll[4]

print(l3[1])
print(l4[2])

#%%

ll.insert(0, [2,3,4,5])

print(ll)

#%%

