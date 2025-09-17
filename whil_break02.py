lists = [2,4,6,8,9,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]
    if val % 2:
        print('브레이크...')
        break
    tot += val
    print(f"[cnt={cnt} val = {val}, tot = {tot}")
    cnt += 1
else: 
   print('홀수가 없습니다.')
    
print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}')

#%%

lists = [2,4,6,8,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]
    if val % 2 == 1:
        print('브레이크...')
        break
    tot += val
    print(f"[cnt={cnt} val = {val}, tot = {tot}")
    cnt += 1
else: 
   print('홀수가 없습니다.')
    
print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}')


#%%

lists = [2,4,6,8,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]

    if val % 2:
        print('브레이크...')
        break

    tot += val
    print(f"[cnt={cnt}] val = {val}, tot = {tot}")
    cnt += 1

else: 
   print('홀수가 없습니다.')
    
print(f'인덱스 0부터 {cnt-1}까지의 짝수의 합은? {tot}')

#%%


lists = [2,4,6,8,10]
cnt = 0
tot = 0


while cnt < len(lists):
    val = lists[cnt]
    
    if val < 0:
        print('리스트에 마이너스(-1) 값이 있어서 처리를 종료했습니다.')
        break
        
    tot += val
    print(f">[cnt={cnt}] val = {val}, tot= {tot}")
    cnt += 1
    
else: 
    print("리스트에 마이너스( -1) 값이 없습니다.")
    print("데이터를 정상적으로 처리했습니다.")
    
print('리스트의 합:', tot)

#%%

