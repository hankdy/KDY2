# 반복문(while)

# 복리이자 계산
# 원금 10만원, 이자가 연10%, 만기 10년, 복리로 계산하라.

interest = 0.1
last = 10
total = 100000
cnt = 1

while cnt <= last:
    total = total + (total*interest)
    print(f'cnt={cnt}, total={total}')
    cnt += 1

print(total)

# 259374.24601000003

