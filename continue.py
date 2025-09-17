
lists = [1,2,4,6,-1,8,-2,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]
    
    if val < 0:
        print(f'리스트에 마이너스({val}) 값을 계산하지 않음')
        
    else: 
        tot += val
        print(f">[cnt={cnt}] val = {val}, tot = {tot}")
        
    cnt += 1
    
print('리스트의 합: ', tot)

#%%


lists = [1,2,4,6,-1,8,-2,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]
    
    if val > 0:
        tot += val
        print(f">[cnt={cnt}] val = {val}, tot = {tot}") 
        
    else: 
        print(f'리스트에 마이너스({val}) 값을 계산하지 않음')
        
    cnt += 1
    
print('리스트의 합: ', tot)


#%%


lists = [1,2,4,6,-1,8,-2,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]
    
    if val < 0:
        print(f'리스트에 마이너스({val}) 값을 계산하지 않음')
        cnt += 1
        continue
        
    tot += val
    print(f">[cnt={cnt}] val = {val}, tot = {tot}")
    cnt += 1
        
print('리스트의 합: ', tot)


#%%

lists = [1,2,4,6,-1,8,-2,10]
cnt = 0
tot = 0

while cnt < len(lists):
    val = lists[cnt]
    cnt += 1
    
    if val < 0:
        # print(f'리스트에 마이너스({val}) 값을 계산하지 않음')
        continue

    tot += val
    print(f">[cnt={cnt}] val = {val}, tot = {tot}")   
    
print('리스트의 합: ', tot)