

# %%
# [문제] 내부 함수를 이용해서 총점, 평균을 구하는 함수를 정의하라.
# 중간고사, 기말고사 전용 함수를 만들어라.

tots = 0
# average = tots / 

def score(name):
    print(f"[score] name({name})")
    
    def tot(*args):
        tota = 0
        
        for tots in args:
            tota += tots
            
            
        return name, tota
        
       

    return tot

#%%

mfunc = score("[중간고사]")        
lfunc = score("[기말고사]") 

print(mfunc(90,80,70))
print(lfunc(80,70,70))

