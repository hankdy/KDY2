# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 합을 구하라.

cnt = 0
sum = 0
max = 100

while cnt < max:
    cnt += 1
    sum += cnt
    print(f'cnt={cnt}, sum={sum}')

print('sum=', sum)