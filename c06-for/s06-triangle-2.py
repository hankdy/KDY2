# 반복문(for)

# [문제]
# 아래와 같이 피라미드 형태로 출력을 하라.
#   - 다중 루프(for)를 이용하라
#   - 문자열 곱하기를 이용하라.
'''
1:    *
3:   ***
5:  *****
7: *******
9:*********
'''

#%%

# 다중 루프(for)
for n in range(1, 10, 2):   # 1, 3, 5, 7, 9
    x = (9 - n) // 2
    print(f"{n}:", end='')
    for m in range(x):      # 공백출력
        print(' ', end='')
    for m in range(n):      # '*' 출력
        print('*', end='')
    print()
        

#%%

# 문자열 곱하기
# 다중 루프(for)
for n in range(1, 10, 2):   # 1, 3, 5, 7, 9
    x = (9 - n) // 2
    print(f"{n}:", end='') # 숫자 출력
    print(' ' * x, end='') # 공백 출력
    print('*' * n)         # '*'  출력

    
    
    
    
    
