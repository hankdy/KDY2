# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:01:12 2025

@author: kangde
"""


def score(name): # 외부함수(정의)
    print(f"[score] name({name})")
    
    def totavg(*args): # 내부 함수(정의)
        tot = 0      # 총점
        avg = 0.0    # 평균
        
        for val in args:
            tot += val
            
        avg = round(tot / len(args),2)
        return name, tot, avg # 외부 함수에서 받은 이름, 최소값, 최대값
    
    return totavg

# name 이라는 값의 인자를 받아서 minmax 값을 구하는 식
# [0] 번째서부터 for 문을 통해 반복해가며 최소, 최대값을 구하는 식


#%%

# 전용함수

mfunc = score("[중간고사]")
lfunc = score("[기말고사]")

print(mfunc(70,80,90))
print(mfunc(88,99,100))

print(lfunc(80,90,100))