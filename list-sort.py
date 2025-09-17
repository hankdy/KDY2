lst = [4,7,3,10,99,22]

print(lst)

#%%
# 정렬

lst.sort()

print(lst)

#%%

lst.append('end')
print(lst)

# 문자열과 숫자는 혼용되어 있으면 요소의 정렬은 불가능

#%%

lstr = ['한글', 'x', 'start', 'a', 'end']
lstr.sort()
print(lstr)


#%%

# reverse = true 는 내림차순

lstr = ['한글', 'x', 'start', 'a', 'end']
lstr.sort(reverse=True)
print(lstr)

lstr.reverse()
print(lstr)