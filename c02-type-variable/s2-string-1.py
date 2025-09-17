# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 12:32:06 2025

@author: Solerox
"""

# 문자열: 문자들의 집합
# 작은 따옴표(')로 묶음
# 큰 따옴표(")로 묶음

s1 = "안녕"    # 큰 따옴표
s2 = '하세요'  # 작은 따옴표
print(s1, s2)   # 안녕 하세요
print("s1, s2") # s1, s2

#%%

# 문자열 곱하기 : 문자열을 지정된 숫자만큼 반복해서 붙인다.
h1 = '*' * 20
h2 = '-' * 20
print('1234567890' * 2) # 12345678901234567890
print('====================')
print('=' * 20)
print(h1)               # **********
print(h2)               # ----------

#%%

# 따옴표 혼용
sx = "철수는 영수에게 '어디에 가니?'라고 물었다."
print(sx)

#%%

# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# print("철수는 영수에게 "어디에 가니?"라고 물었다.")

print('철수는 영수에게 "어디에 가니?"라고 물었다.')
print("철수는 영수에게 \"어디에 가니?\"라고 물었다.")

# SyntaxError: unterminated string literal (detected at line 42)
# print('I don't want to go school')
print('I don\'t want to go school.')
            
print("I don't want to go school.")

#%%

# 문자열의 시자과 끝은 작은 따옴표로 기술해야 한다.
# SyntaxError: unterminated string literal (detected at line 1)
# print('작은 따옴표")
# print("큰 따옴표')


    