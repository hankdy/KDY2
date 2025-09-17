
# 문자열 관련 함수들(functions)
# - 문자열 객체 멤버 함수, 또는 메서드(method)
# - 메서드 : 특정 객체에 종속되어 있는 전용 함수

# 결과 = 문자열 .함수()
# cnt = str.count("x")

# 문자열 전용 메서드(method)
# count(), find(), index(), join(), upper(), lower()
# lstrip(), rstrip(), strip(), replace(), split()

# string methods
# http://docs.python.org/3/library/stdtypes.html#string-methods


#%%

# 문자열 함수

# 문자 개수 세기 : count()

s = "hello world."
l = "l"
c = s.count(l)

print(f"문자열('{s}')에 문자 ('{l}')은 ({c}))개 있다.")
print(f"문자열(\"{s}\")에 문자 ('{l}')은 ({c}))개 있다.")

#%% 

tel = "010-1234-5678"
telcnt = tel.count('-')
print(f"'{tel}'.count('-'): {telcnt}개")

#%%

# 문자열을 변수에 담지 않고 직접 함수를 지정하여 처리
spcnt = "welcome to korea".count(' ')
print("공백 갯수: ", spcnt)


#%%

# 문자열에서 빈문자열의 갯수는?

wct = "welcome to korea"
cnt = wct.count("")
print("문자열의 길이: ", len(wct))  # 16
print("빈 문자열의 갯수: ", cnt)    # 17 = len(str) + 1