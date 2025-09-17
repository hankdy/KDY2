
cnt = 1
tot = 0

while True:
    
    tot += cnt 
    print(f'cnt={cnt}, tot = {tot}')
    if cnt >= 100:
        break  
    cnt += 1
    
print('tot=', tot)   

#%%

cnt = 1
tot = 0

while cnt <= 100 :
    tot += cnt 
    print(f'cnt={cnt}, tot = {tot}')
    cnt += 1
    
print('tot=', tot)   


#%%

lst = [2,4,6,8,10]

while lst:
    print(lst.pop())
    
print('lst:', lst)

#%%

lst = [2,4,6,8,10]
cnt = 0

while lst:
    cnt += 1
    print(f'cnt ={cnt}, lst = {lst.pop()}')
    
print('lst:', lst)


#%%

lst = [2,4,6,8,10]
cnt = 0

while lst:
    cnt += 1
    print(f'cnt ={cnt}, lst = {lst.pop(0)}')
    
print('lst:', lst)


#%%

lists = [2,4,6,8,10]
cnt = 0
tot = 0
lex = len(lists)

while cnt < lex:
    val = lists[cnt]
    tot += val
    print(f"[cnt={cnt}] cal = {val}, tot = {tot}")
    cnt += 1
    
print(f'lists={lists}')
print(f'tot={tot}')


#%%

lists = [2,4,6,8,10]
cnt = 0
tot = 0
lex = len(lists)

while True :
            
    val = lists[cnt]
    tot += val
    print(f"[cnt={cnt}] cal = {val}, tot = {tot}")    
    cnt += 1
    
    if cnt > lex:
        break
    
print(f'lists={lists}')
print(f'tot={tot}')

#%%

