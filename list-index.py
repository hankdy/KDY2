# 리스트에 요소의 값이 있는 위치
# 인덱스 = 리스트.index(값)
# 가장 먼저 찾은 위치를 리턴

lst = ['DB', 'LG', 'SM', 'LG', 'IBM', '삼성']

print(lst)

value = 'LG'
index = lst.index(value)
found = (value == lst[index])

print('value: ' , value)
print('index: ' , index)
print('found: ' , found)

#%%

# 찾지 못하면?
# 예외가 발생하면 강제 종료된다.

notfound = lst.index('현대')


