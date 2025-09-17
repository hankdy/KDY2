# scores = [200,70,80,-70,90,100,90,90]
# total = 0
# faultcnt = 0


# for score in scores :
#     if score < 0 or score > 100:
#         faultcnt += 1
#         continue
#     total += score
    
# cnt = len(scores) - faultcnt

# average = round( total / cnt, 3 )

# print(f"잘못된 점수의 갯수: {faultcnt}")
# print(f"총점 = {total}, 평균 = {average}")

# #%%
# n = 10
# ten = range(n)

# print(ten)

# for cnt in ten:
#     print(cnt, end="")
    
    
# #%%

# for cnt in range(10):
#     print(cnt)
    
    
# #%%

# n = 10 + 1
# sum = 0

# for cnt in range(n):
#     sum += cnt
#     print(f"cnt={cnt}, sum = {sum}")
    
# print('sum=', sum)


#%%

s = 1
n = 100
l = n + 1
sum = 0

for cnt in range(s, l):
    sum += cnt
    print(f"cnt={cnt}, sum = {sum}")
    
print('sum=', sum)


#%%

# 수열의 합

n  = 100
tot = n * (n+1) / 2
print('tot=', tot)

#%%

ctx = sum == tot
print(f'sum({sum}) == ({tot}) ?', ctx)


#%%

# 1부터 10까지의 연속된 수에서 홀수만 출력하라.
for cnt in range(1, 11, 2):
    print(f"{cnt}")
    
#%%

# 2부터 10까지의 연속된 수에서 짝수만 출력하라.
for cnt in range(2, 11, 2):
    print(f"{cnt}")
    
    
    
#%%

# 1부터 10까지의 연속된수에서 홀수의 합과 짝수의 합을 각각 구하라.

total = 0
n = 1

for cnt in range(1, 11, 2):
    cnt += n
    print(cnt)
    
print(total)
    


#%%

sn = 1
en = 10
os = 0
es = 0

for n in range(sn, en + 1):
    if n % 2 == 0:
        es += n
    else :
        os += n
        
print(f"({sn}) 부터 ({en}) 까지 수에서 홀수의 합은 ({os}) 이다.")
print(f"({sn}) 부터 ({en}) 까지 수에서 짝수의 합은 ({es}) 이다.")


#%%

sn = 1
en = 10
os = 0
es = 0

for n in range(sn, en + 1):
    m = n // 2 * 2
    if n == m:
        es += n
    else :
        os += n
        
print(f"({sn}) 부터 ({en}) 까지 수에서 홀수의 합은 ({os}) 이다.")
print(f"({sn}) 부터 ({en}) 까지 수에서 짝수의 합은 ({es}) 이다.")

#%%

# 1부터 10까지 증가하면서 * 을 동일한 라인에 출력

ten = range(10)

for i in ten:
    if 0 < i < 10:
        print("*")
        
#%%

for x in range(1,6):
    print(x, end =":")
    for y in range(x):
        print("*", end ='')
    print()
    
#%%

for x in range(1,6):
    print(x , end = ':')
    print('*' * x)


#%%

a = 1
b = 10

for x in range(a, b+1, 2):
    print(x, end =":")
    print('*' * x)

#%%

a = 1
b = 10

for x in range(a, b + 1, 2):
    spaces = (b - x) // 2
    print(f"{x}: " + ' ' * spaces + '*' * x)


#%%

for n in range(1, 10, 2):
    x = (9 -n) //2
    print(f"{n}:", end = '')
    for m in range(x):
        print(' ', end="")
    for m in range(n):
        print('*', end = "")
    
    
#%%


for n in range(1, 10, 2):
    x = (9 -n) //2
    print(f"{n}:", end = '')
    print(' '* x,  end = "")
    print('*'* n)
    
    
#%%


b = range(1, 10)
c = range(1, 10)

for n in b: 
    n *= 2 
    print(f'2 * {n//2} = {n}')
    
    
#%%
    
ds = 2
de = 9
dl = 3

for x in range(ds, de+1, dl):
    for d in range(dl):
        dx = x + d
        if dx > de:
            break
        ds = f"[{dx}단]"
        print(f"{ds:^14}", end="")
    print()
    
    for y in range(1, 10):
        for n in range(dl):
            m = x + n
            if m > de:
                break
            z = m * y 
            s = f"[{m}]*[{y}] = [{z:>2}]"
            print(f"{s:^15}", end="")
        print()
    print(' ')
    
    

