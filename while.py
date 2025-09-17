# 반복문(while)

# 3번 반복, 반복회수를 기술하라.

print('나무를 1번 찍는다.')
print('나무를 2번 찍는다.')
print('나무를 3번 찍는다.')

#%%

tree = 0
n = 10

while tree < n :
    tree += 1
    print(f"나무를 {tree}번 찍는다.")
    if tree == n :
        print("나무가 넘어간다.")

    
#%%

for n in range(3):
    print(f'나무를 {n}번 찍는다.')
    
#%%

count = 1
print('나무를 {0}번 찍는다.'.format(count))

count = 2
print('나무를 {0}번 찍는다.'.format(count))

count = 3
print('나무를 {0}번 찍는다.'.format(count))

#%%

# 초깃값 지정

count = 0

count += 1
print(f'나무를 {count}번 찍는다.')

count += 1
print(f'나무를 {count}번 찍는다.')

count += 1
print(f'나무를 {count}번 찍는다.')


#%%

"""
while 조건식:
    실행문1
    실행문2
    
"""

#%%

count = 1
while count <= 100:
    print('나무를 {0}번 찍는다.'.format(count))
    count += 1
    if count == 101:
        break
print("나무를 1개 획득하였습니다.")
    
# print('count=' , count)
# print('The END')

#%%

what = "커피"
count = 10
fmt = '{0} {1}번 볶는다.'
n = 1
while n <= count:
    print(fmt.format(what, n))
    n += 1

print("작업을 {0} 번 완료 했습니다.". format(count))

#%%

number = 0
n = 100
total = 0

while number < n :
    number += 1
    print(f"{number} 입니다.")
    total += number

print(f"전체 총합은 {total} 입니다.")

#%%

cnt = 1
max = 100
sum = 0

while cnt <= max :
    sum += cnt 
    print(f'cnt = {cnt}, sum = {sum}')
    cnt += 1  # 1씩 증가
    
print('합은?' , sum)

#%%

cnt = 1
max = 100
sum = 0

while cnt <= max :
    sum += cnt
    cnt += 1
    if cnt % 2 == 0:
        sum -= cnt
        print(f"cnt = {cnt}, sum = {sum}")

        
print("합은? :", sum)
    
#%%

cnt = 1
sum = 0

while cnt <= 100: 
    sum += cnt
    print(f"cnt = {cnt}, sum = {sum}")
    cnt += 2
    
print('sum=', sum)

#%%

cnt = 0
sum = 0

while cnt <= 100: 
    sum += cnt
    print(f"cnt = {cnt}, sum = {sum}")
    cnt += 2
    
print('sum=', sum)

#%%

cnt = 1
sum = 0
mmm = 0

while cnt <= 100 :
    x = cnt % 2
    if x == 0:
        sum += cnt
    else: 
        mmm += cnt
        
    print(f"[cnt = {cnt}] x({x}), 홀수합({mmm}), 짝수합({sum})")
    
    cnt += 1

print("짝수의 합?: ", sum)
print("홀수의 합?: ", mmm)


#%%

cnt = 1
sum = 0
mmm = 0

while cnt <= 10 :
    x = cnt - cnt // 2 * 2
    if x == 0:
        sum += cnt
    else: 
        mmm += cnt
        
    print(f"[cnt = {cnt}] x({x}), 홀수합({mmm}), 짝수합({sum})")
    
    cnt += 1

print("짝수의 합?: ", sum)
print("홀수의 합?: ", mmm)