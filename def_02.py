def hellocnt(msg, cnt):
    print(f"[hellox] msg({msg}), cnt({cnt}")
    for n in range(cnt):
        print(f"[{n}]: {msg}")
        
        
#%%

hellocnt("hello, world.", 10)

#%%

"""
함수 정의에 리턴값이 없는데 
함수 호출에서 리턴을 받으면?
리턴 : none
"""

rt = hellocnt("hello, world.", 10)
print("리턴:", rt)


#%%

rt = hellocnt("msg", 10)
print("리턴:", rt)

#%%