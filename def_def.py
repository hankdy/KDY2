
def score(name): # 외부함수(정의)
    print(f"[score] name({name})")
    
    def minmax(*args): # 내부 함수(정의)
        min = args[0]
        max = args[0]
        
        for val in args:
            if val < min:
                min = val
            if val > max:
                max = val

                
        return name, min, max # 외부 함수에서 받은 이름, 최소값, 최대값
    
    return minmax

# name 이라는 값의 인자를 받아서 minmax 값을 구하는 식
# [0] 번째서부터 for 문을 통해 반복해가며 최소, 최대값을 구하는 식


#%%

# 전용함수

mfunc = score("[중간고사]")
lfunc = score("[기말고사]")

print(mfunc(70,80,90))
print(mfunc(88,99,100))

print(lfunc(80,90,100))
print(lfunc(90,77,65))