# 반복문(while)


# [문제]
# 반복문(while)을 사용하여 1부터 100까지 홀수의 합과 짝수의 합을 각각 구하라.
# 1부터 100까지 숫자는 1씩 증가한다. (1,2,3,4,5,.... 99, 100)

cnt = 1  # 증가값
even = 0 # 짝수의 합
odd = 0  # 홀수의 합

while cnt <= 100:
    x = cnt % 2 # 2로 나눈 수의 나머지 값(x)
    if x == 0:  # 짝수
        even += cnt
    else:   # 홀수
        odd += cnt

    print(f"[cnt={cnt}] x({x}), 홀수합({odd}), 짝수합({even})")        

    cnt += 1

print('짝수의 합?', even)
print('홀수의 합?', odd)