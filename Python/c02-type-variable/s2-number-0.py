# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 11:23:05 2025

@author: Solerox
"""

# 숫자 자료형 : 정수, 실수
# 연산(계산)을 위한 자료형

#%%

# 정수
print(5)   # 양의 정수: 부호 생략 가능
print(+5)
print(-10) # 음의 정수 

#%%

# 실수
print(3.14)
print(0.1234)

#%%

# 사칙연산 : +, -, *, /, //, %
print(5 + 3)         # 8
print(5+3)           # 8
print(float(5+3))    # 8   : 실수로 자료형 변환
print(6 / 3)         # 2.0 : 실수 나누기
print(int(6 / 3))    # 2   : 정수로 자료형 변환
print(6 // 3)        # 2   : 정수 나누기

#%%

# 나누기
print(10 / 3)        # 3.3333333333333335, 오차 발생
print(10 // 3)       # 2 : 정수 나누기, 몫

#%%

# 나머지 연산자 : %
print(10 % 3)  # 나머지: 1


#%%
print(3 * (3 + 1)) # 12 = 3 * 4
print(3 * 3 + 1)   # 10 = 9 + 1

#%%

# P43: 1분 퀴즈
# 다음의 숫자 자료형 -10을 출력하기 위한 방법으로 알맞은 것은?
"""
1. print(- + 10)
2. print(-10)
3. print("-10")
4. print(10-)
"""

#%%

print(- + 10) # -10
print(-10)    # -10: 정답
print("-10")  # -10: 문자열 출력
print(10-)    # 문법오류: SyntaxError: invalid syntax

#%%

# type() : 자료형을 확인하는 함수
print(type(- + 10)) # int: integer(정수)
print(type(-10))    # int
print(type("-10"))  # str: string(문자열)

#%%

# 양수를 음수로 바꾸기
# 1. minus(-) 부호를 앞에 붙인다.
# 2. -1을 곱한다.
x = 10
y = -x
z = x * -1

print(x, y, z) # 10 -10 -10
print(x, y, z, sep='')    # 10-10-10
print(x, y, z, sep=',')   # 10,-10,-10
print(x, y, z, sep=', ')  # 10, -10, -10
print(x, y, z, sep='/')   # 10/-10/-10



