"""
문자열 인덱싱 
문자열은 연속된 문자들의 연속된 집합

참조 : 특정한 위치의 문자를 본다(읽음)
시작위치 : 0부터 시작
참조방법 : 문자열 [인덱스]
참조범위 : 0 ~ n -1, n = len(문자열)
제약사항 : 참조는 할 수 있지만 바꿀 수 없다( read - only )

문자열 길이 함수 : len()
문자열 길이 = len(문자열)
"""

#%%
#  문자열의 길이(length)

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(len(s))

#%%

print(s[0],s[1], "..." , s[24], s[25])
print(s[0],s[1], "..." , s[len(s)-2], s[len(s)-1])

#%%

s1 = s
print("s:", id(s))
print("s1:", id(s1))

#%%

s += '.'
print("s :", id(s))

#%%
print(id(s))
s = "abcdefghijklmnopqrstu"
print(id(s), s, len(s))