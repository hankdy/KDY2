sn ="12345678901234567890"

print(sn[::2])
print(sn[1::2])

#%%

"""
%s : 문자열
%c : 문자
%d : 정수
%f : 실수
%o : 8진수
%x : 16진수
%% : Literal %(문자 %자체)

"""

#%%

# 정수 %d

num = 99
print("이 숫자는 정수 %d 입니다." % num)
print("이 숫자는 정수 {} 입니다." .format(num))
print(f"이 숫자는 정수 {num} 입니다.")

#%%

# 문자열 #s

name = "홍길동"
age = 34

userfmt = "이름이 %s인 사람의 나이는 %d 세 입니다."%(name, age)

print(userfmt)

#%%

# % 를 문자 그대로 출력하기 위해서는?
# '#%%' 와 같이 연속해서 기술한다.

sv = 50

print("오늘 눈이 올 확률은 %d %% 입니다." %sv)

