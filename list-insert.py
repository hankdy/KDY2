# 리스트에 요소 삽입 : insert

lst = [3, 5, 7]

lst.append(9)
print(lst)

# 0번째 위치에 값을 넣고 기존의 내용은 뒤로 밀림

pos = 0
val = 1

lst.insert(pos,val)

print(lst)

# insert()를 이용해서 맨 마지막에 요소를 삽입

pos = len(lst)
val = 00
lst.insert(pos,val)

print(lst)


lst.insert(0,4)

print(lst)

#%%
# 변경 하지 않을 것 같으면 직접적으로 값을 지정해주는것이 낫고
# 자주 변경될 것 같은 함수에는 변수값을 지정해주는 것이 낫다.