# 반복문(while)

lst = [2,4,6,8,10]
# lst = []

cnt = 0
# list.pop() 자료를 마지막에서 하나씩 꺼냄
# 꺼낸 후 list에서는 자료가 삭제됨
while lst:
    cnt += 1
    print(f'cnt={cnt}, lst={lst.pop()}')

print('lst:', lst)
