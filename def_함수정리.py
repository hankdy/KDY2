"""
def 함수명 (파라미터)
    실행문
    return 리턴값

매개변수와 인자
매개변수(parameter): 함수에 입력으로 전달된 값을 받는 변수, 함수 정의부에 기술
인자(arguments) : 함수를 호출할 때 전달하는 입력값, 함수 호출부에 기술

"""

#%% 


# 함수정의 : 한 번만 기술한다.
# 함수이름 : hello
# 파라미터 : none
# 리턴밸류 : none

def hello():
    print("[hello]" , end = ':')
    print("hello, world!")
    

#%%

#함수호출
#함수를 여러번 계속 호출할 수 있다.

hello()
hello()
