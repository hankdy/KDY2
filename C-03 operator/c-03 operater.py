a = {4,5,6,7}

b = {1,2,3,4}

print(a - b) # 차집합
print(a & b) # 교집합
print(a | b) # 합집합

#%%

a = True
b = False

print(a or b)   # 둘중에 하나라도 true 라면 true 값
print(a and b)  # 둘다 true 여야 true 가 나온다
print(not a)    # not true 니까 결과값 false


#%%

# XOR : a, b 의 값이 다르면 참, 같으면 거짓

# 원본 : 1010 1110
# 암호 : 1010 1010
# ------------------
# xor  : 0000 0100
# 암호 : 1010 1010
# -----------------
# 해독 : 1010 1110

# ??????????????
