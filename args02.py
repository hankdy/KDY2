# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 14:32:44 2025

@author: kangde
"""

def tots(*vals): #동일한 자료구조일때 좋다.
    print(f"[tots] type({type(vals)}), {vals}, {len(vals)}")
    tot = 0
    for val in vals: # 튜플에서 요소를 하나씩 꺼내서 연산을 수행
        tot += val
    return tot

#%%

print(tots(10))
print(tots(10,20))
print(tots(10,20,30))

#%%

totx = 0
totx += (99,)

#%%



