# -*- coding: utf-8 -*-

# 예외처리(Exception)
# try ~ except
# 
# 예외:
#   - 잘못된 동작을 했을 때 
#   - 실행할 때 발생
#   - 프로그램이 종료
# 
# 예외처리:
#   - 비정상적 상황으로 인해서 프로그램이 중단없이 실행 가능하도록 처리

#%%

# 0으로 나누었을 경우
x = 10
y = 0
z = x / y # 종료: ZeroDivisionError: division by zero
print("z:", z)

#%%

import sys

x = 10
y = 0

if y == 0:
    print('0으로 나눌 수 없습니다.')
    sys.exit(0) # 프로그램을 종료

z = x / y 
    
print("z:", z)

#%%

# 예외처리:
# 오류가 발생했을 때 프로그램을 종료시키지 않게 하고
# 사용자로 하여금 상황을 인지할 수 있도록 처리한다.
# 그리고 흐름을 정상적으로 진행한다.
x = 10
y = 0

try:
    z = x / y
    print("z:", z)
except ZeroDivisionError as e:
    print("[예외발생] ", e) #  division by zero
    
print("작업완료")    


    
