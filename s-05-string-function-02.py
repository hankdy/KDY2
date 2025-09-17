

# 문자열 함수

# 문자열의 위치 : find()
# 처음 만나는 문자열의 위치

# 결과 
#  성공 : 0부터
#  실패 : -1(찾지 못하면)
 
s = "Python is the best choice"
print("0123456789" * 4)
print(s)

#%%

# 문자 한개 탐색

ipos = s.find("i")
kpos = s.find("k")

print(f"'{s}'.find('i) : " , ipos) # 7, is ...
print(f"'{s}'.find('k) : " , kpos) # -1

#%%

# 문자열 탐색
print(f"'{s}'.find('is') : " , s.find('is'))

#%%

s = "python is the best choice"
findstr = 't'
t1 = s.find(findstr)
t2 = s[t1+1:].find(findstr) + 3
t3 = s[t2+1:].find(findstr) + 11
print(t1,t2,t3)
# print(f"'{s}'.find('t') :", s.find("t")) 



