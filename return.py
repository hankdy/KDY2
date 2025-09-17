"""
함수(function)
함수 정의와 호출은 전달되는 순서, 자료형을 맞춰야 한다.
반환값 : 
    - 반환값은 0개 이상
    - 형식:
        - return
        - return 값
        - return 값1 , 값2
"""

def add(a, b):
    return a + b

#%%

def mul(a, b):
    c = a * b
    return c


#%%

print(add(1, 2))
print(add(10, 20))

#%%

print(mul(1, 2))
print(mul(10, 20))

#%%

print(add('abc', 'def'))
print(mul('*', 10))

#%%

