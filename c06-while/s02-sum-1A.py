# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 합을 구하라.

cnt = 1     # 증가값
max = 100   # 종료값
sum = 0     # 합

while cnt <= max:    # 1,2,3, .... 99, 100
    sum += cnt
    print(f'cnt={cnt}, sum={sum}')
    cnt += 1 # 1씩 증가

print('합은?', sum)