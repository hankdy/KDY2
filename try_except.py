"""

예외처리(exception)
try ~ except

예외:
    - 잘못된 동작을 했을떄
    - 실행 할 때 발생
    - 프로그램이 종료
    
예외처리:
    - 비정상적으로 인해서 프로그램이 중단없이 실행 가능하도록 처리
    
"""

# %%


# 0으로 나누었을 경우

x = 10
y = 0

z = x / y
print("z:", z)

# %%

import sys

x = 10
y = 0

if y == 0:
    print('0으로 나눌 수 없습니다.')
    sys.exit(0)  #프로그램을 종료
    
z = x / y

print("z:", z)

# %%


"""
예외처리:
오류가 발생했을 때 프로그램을 종료시키지 않게 하고
사용자로 하여금 상황을 인지할 수 있도록 처리한다.
그리고 흐름을 정상적으로 진행한다.

"""

x = 10
y = 0
z = 0

try :
    z = x / y
    print("z:", z)
except ZeroDivisionError as e:
    print("[예외발생]", e) # division by zero
    
print("작업완료")



#%%

file = open("없는파일.txt", 'r')

#%%

try :
    file = open("./없는파일.txt", 'r')
except FileNotFoundError as e:
    print("[예외발생]", e)
    print("존재하지 않는 파일입니다.")
    
    
    
# %%
"""
try 의 명령문들 중에서 예외가 발생하면
해당하는 위치에서 except로 이동하여 처리후 
예외 구문을 빠져 나간다.
그러므로 예외가 발생한 위치 다음의 명령은 실행되지 않는다.

"""

x = 10
y = 0
z = 0

try :
    z = x / y
    file = open("./없는파일.txt", 'r')
    print("정상처리")
except ZeroDivisionError as e:
    print("[예외발생] 나누기 오류:", e) # division by zero

except FileNotFoundError as e:
    print("[예외발생] 나누기 오류:", e)
    
print("작업완료")