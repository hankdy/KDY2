# 문자열 나누기: split

ss = "Python is the best choice"
sp = ss.split() # 공백

print(type(sp), sp) # ['Python', 'is', 'the', 'best', 'choice']

#%%

print(sp[0]) # Python
print(sp[1]) # is
print(sp[2]) # the
print(sp[3]) # best
print(sp[4]) # choice

#%%

# 리스트에서 각 요소의 값을 추출
print('-' * 30)
for item in sp: 
    print(item)

#%%

# 리스트에서 각 요소의 인덱스와 값을 추출
print('-' * 30)
for idx, item in enumerate(sp):
    print(f"sp[{idx}] : {item}, {sp[idx]}")

