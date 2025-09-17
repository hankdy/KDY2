# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 09:04:23 2025

@author: Solerox
"""

# 셋(set) 자료형
# 집합 자료형
#   - 중복을 허용하지 않음
#   - 순서를 보장하지 않음(무작위)

#%%

asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.update({'한국', '홍콩', '태국'}) # 한 번에 여러개의 요소를 넣음
print(asia)

# {'태국', '중국', '한국', '홍콩', '베트남'}

#%%

asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.add('한국')
asia.add('홍콩')
asia.add('태국')
print(asia)

# {'태국', '베트남', '중국', '한국', '홍콩'}

#%%

# 연구과제
asia = {'한국', '중국', '일본'}
asia.add('베트남')
asia.add('중국')
asia.remove('일본')
asia.update('한국', '홍콩', '태국') 
print(asia)

# {'한', '홍', '베트남', '태', '중국', '콩', '한국', '국'}

