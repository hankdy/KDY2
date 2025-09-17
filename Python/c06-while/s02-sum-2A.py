# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 홀수의 합을 구하라.

cnt = 1
sum = 0

while cnt < 100: # 1,3,5,7,9 ... 99
    sum += cnt
    print(f'cnt={cnt}, sum={sum}')
    cnt += 2

print('sum=', sum)