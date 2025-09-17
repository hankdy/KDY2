lst = []

lst.append(9)
lst.append(8)
lst.append(7)

print(lst)

lst.append(6)
print(lst)

#%%

# 리스트 자료형에 여러개를 추가하고자 할 때 사용.
lst.extend([5,0,12])

print(lst)

lst.extend([5,0,12,[4,5,6]])

print(lst)


