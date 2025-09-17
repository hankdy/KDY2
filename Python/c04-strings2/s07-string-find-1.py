# -*- coding: utf-8 -*-

# 문자열 함수

# 문자열의 위치 : find()
# 처음 만나는 문자열의 위치
# 결과
#   성공 : 0부터
#   실패 : -1(찾지 못하면)

s = "Python is the best choice, version 3.18"
print("0123456789" * 4)
print(s)

#%%

print(s.find('3')) # 35

#%%

# 문자 한개 탐색
ipos = s.find('i')
kpos = s.find('k')

print(f"'{s}'.find('i') : ", ipos) # 7, is ...
print(f"'{s}'.find('k') : ", kpos) # -1

#%%

# 문자열 탐색
print(f"'{s}'.find('is') : ", s.find('is'))   # 7
print(f"'{s}'.find('the') : ", s.find('the')) # 10

#%%

# [문제]
# 문자열을 연속해서 찾기.
# 문자열 변수(s)에서 지정된 문자열('t')의 위치를 모두 찾아라.
# 단. find() 함수를 이용하라.
# 정답: 2 10 17

s = "Python is the best choice"
#%%

print("0123456789" * 4)
print(s)

# 찾을 문자열
findstr = 't'
print(f"문자열 ('{s}')에서 문자열('{findstr}')의 갯수는?", s.count(findstr))

#%%

# [해결1] 슬라이싱
t1 = s.find(findstr)
t2 = s[t1+1:].find(findstr) + t1 + 1
t3 = s[t2+1:].find(findstr) + t2 + 1
print(t1,t2,t3) # 2 10 17

#%%

# 분할: 검증
t1 = s.find(findstr)
s1 = s[t1+1:]  # 슬라이싱
t2 = s1.find(findstr) + t1 + 1 # 이전위치
s2 = s[t2+1:]  # 슬라이싱 
t3 = s2.find(findstr) + t2 + 1 # 이전위치
print(t1,t2,t3) # 2 10 17

#%%

# [해결2] find() 함수의 시작위치
# str.find(sub[, start[, end]])
# 결과 = 문자열.find(탐색문자열, 시작위치[, 종료위치])

t1 = s.find(findstr)
t2 = s.find(findstr, t1 + 1) # 다음위치
t3 = s.find(findstr, t2 + 1) # 다음위치
print(t1,t2,t3) # 2 10 17


#%%

# [문제2]
# 전화번호(010-1234-5678)에서 하이픈(-)을 기준으로 번호를 추출하라.
# 단: 문자열.find() 메서드를 이용하라.

tel = "010-1234-5678"
tfs = '-'

# 첫 번째 번호
s1 = tel.find(tfs)
t1 = tel[:s1]

# 두 번째 번호
s2 = tel.find(tfs, s1+1)
t2 = tel[s1+1:s2]

# 세 번째 번호
s3 = tel.find(tfs, s2+1)
# t3 = tel[s2+1:s3] # -1은 맨 마지막 요소('8')를 제외
t3 = tel[s2+1:]

print("위치:", s1, s2, s3) # 3, 8, -1
print("번호:", t1, t2, t3) # 010 1234 5678












